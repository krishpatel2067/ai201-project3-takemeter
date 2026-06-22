import os
import re
from pathlib import Path
from dotenv import load_dotenv

import gradio as gr
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer

load_dotenv()


def find_best_checkpoint(base_dir: str) -> str:
    checkpoints = list(Path(base_dir).glob("checkpoint-*"))
    if not checkpoints:
        raise FileNotFoundError(f"No checkpoint-* directories found in '{base_dir}'")
    return str(max(checkpoints, key=lambda p: int(re.search(r"\d+", p.name).group())))


MODEL_PATH = os.environ.get("MODEL_DIR") or find_best_checkpoint("takemeter-model")

tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

LABELS = ["artistic_critique", "external_narrative", "fandom_expression"]


def classify(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1).squeeze().tolist()
    predicted = LABELS[int(torch.argmax(logits))]
    confidences = {label: round(prob, 4) for label, prob in zip(LABELS, probs)}
    return predicted, confidences


demo = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(lines=5, placeholder="Enter a post to classify..."),
    outputs=[
        gr.Textbox(label="Predicted Label"),
        gr.Label(label="Confidence Scores"),
    ],
    title="TakeMeter Classifier",
    description="Classifies a social media post as artistic critique, external narrative, or fandom expression.",
)

if __name__ == "__main__":
    demo.launch()
