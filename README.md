# TakeMeter

_Krish A. Patel_

_CodePath AI201: Applications of AI Engineering Project 3 (Summer 2026)_

[TODO] Intro - community, what was given, what I did (annotation, reports)

## Tech Stack

## Setup

[TODO] ADD THE IPYNB

### Google Colab Notebook

1. Download the [] Jupyter notebook.
2. Go to [Google Colab](https://colab.research.google.com/).
3. Go to **File** > **Upload notebook**, and select the downloaded notebook.
4. Go to **Runtime** > **Change runtime type**, and make sure that **Hardware accelerator** is set to **T4 GPU**. Click **Save**.
5. Get a free [Groq](https://console.groq.com/keys) API key.
6. Go to **Secrets** (key icon on the left), set "GROQ_API_KEY" to your Groq API key, and enable **Notebook access**.

### (Optional) See Data Overview

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run all the cells in [`data/data_overview.ipynb`](./data/data_overview.ipynb).

## Labels

## Results

### Baseline

### Fine-Tuned

## Other Takeaways

## Notes

- Got me to read Reddit posts for once!
- https://www.reddit.com/r/popheads/comments/7brx3o/megathread_taylor_swift_reputation/
- Post selection criteria:
  - Only immediate replies, not replies of replies
  - No deleted posts
  - Only family friendly posts
- Labels: `artistic_critique`, `external_narrative`, `fandom_expression`
- Ambiguity resolution - priority levels due to post effort and abundance for each label
- Stress testing conclusion:
  - Boundary btwn `artistic_critique` and `external_narrative` much more critical to sharpen
  - More frequent ambiguities in that boundary
  - `fandom_expression` is the unique one because
    - Its tone is completely different - raw emotion, not meditative or explicative
    - It is often standalone or gets dominated in content or centrality by the other two
- Had to use Google Sheets since CSV extension automatically squeezed text into one paragraph
- Annotating 200 samples:
  - Unique username constraint very limiting
  - Reached the bottom of the 2.9k-comment megathread
  - Got close with the data (started recognizing the usernames and posts)
  - Links couldn't be copied in plaintext, collapsing a part chunk of context behind some posts
  - Lesson learned - data is _highly_ unclean - even in a thread of 2.4 comments, it was difficult to find 200 good ones

- Zero-shot baseline:

Classification report:

Fixed! A simple copy-paste error that caused the LLM to skip the general instructions and immediately resort to the ambiguity resolution steps, which turned out to be so algorithmic that it got perfect accuracy on the 32 samples.

- Fine-tuned:
  - No hyperparams changed at first (works well for 100-500 samples)
  - But needed to due to abnormally low accuracy
  - Optimal number of epochs experiment - took 25 min to run
    - Distilbert already returned the best epoch's metrics, so plateaus would be more common than dips

Results comparison:

```
==================================================
RESULTS COMPARISON
==================================================
Model                               Accuracy
---------------------------------------------
Zero-shot baseline (Groq)              0.968
Fine-tuned DistilBERT                  0.844
---------------------------------------------

Fine-tuning regression: 0.124
```

Eval results:

```
{
  "baseline_accuracy": 0.9677,
  "finetuned_accuracy": 0.8438,
  "improvement": -0.124,
  "test_set_size": 32,
  "label_map": {
    "artistic_critique": 0,
    "external_narrative": 1,
    "fandom_expression": 2
  },
  "model": "distilbert-base-uncased"
}
```
