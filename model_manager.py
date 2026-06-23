import os
import re
from pathlib import Path
from dotenv import load_dotenv
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer

_LABELS = ["artistic_critique", "external_narrative", "fandom_expression"]


load_dotenv()


def _find_best_checkpoint(base_dir: str) -> str:
    checkpoints = list(Path(base_dir).glob("checkpoint-*"))
    if not checkpoints:
        raise FileNotFoundError(f"No checkpoint-* directories found in '{base_dir}'")
    return str(max(checkpoints, key=lambda p: int(re.search(r"\d+", p.name).group())))


_MODEL_PATH = os.environ.get("MODEL_DIR") or _find_best_checkpoint("takemeter-model")
_tokenizer = DistilBertTokenizer.from_pretrained(_MODEL_PATH)
_model = DistilBertForSequenceClassification.from_pretrained(_MODEL_PATH)
_model.eval()


def classify(text):
    inputs = _tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    with torch.no_grad():
        logits = _model(**inputs).logits
    probs = torch.softmax(logits, dim=-1).squeeze().tolist()
    predicted = _LABELS[int(torch.argmax(logits))]
    confidences = {label: round(prob, 4) for label, prob in zip(_LABELS, probs)}
    return predicted, confidences
