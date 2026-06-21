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
7. Download [`data/data.csv`](./data/data.csv).
8. Run all the cells, and upload `data.csv` when prompted in Section 1.

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

## Evaluation Report

### Metrics

#### Baseline

**Accuracy**: 0.968

|                      | Precision | Recall | F1   |
| -------------------- | --------- | ------ | ---- |
| `artistic_critique`  | 0.93      | 1.00   | 0.97 |
| `external_narrative` | 1.00      | 0.91   | 0.95 |
| `fandom_expression`  | 1.00      | 1.00   | 1.00 |

#### Fine-Tuned

**Accuracy**: 0.844

|                      | Precision | Recall | F1   |
| -------------------- | --------- | ------ | ---- |
| `artistic_critique`  | 0.81      | 0.93   | 0.87 |
| `external_narrative` | 0.91      | 0.83   | 0.87 |
| `fandom_expression`  | 0.80      | 0.67   | 0.73 |

### Confusion Matrix

For fine-tuned model only.

| True v Predicted >   | `artistic_critique` | `external_narrative` | `fandom_expression` |
| -------------------- | ------------------- | -------------------- | ------------------- |
| `artistic_critique`  | 13                  | 1                    | 0                   |
| `external_narrative` | 1                   | 10                   | 1                   |
| `fandom_expression`  | 2                   | 0                    | 4                   |

### Misclassifications

Pulled from [`docs/ft_model_results.md`](./docs/ft_model_results.md#wrong-predictions).

These 3 wrong classifications shed light on the tricky boundaries between `fandom_expression` and the other two labels made even fuzzier by the model's imperfect tone identification of posts, which is a key deciding factor for `fandom_expression`.

#### 1

```
Text:      DANCING WITH OUR HANDS TIED IS A BANGERRRR
True:      fandom_expression
Predicted: artistic_critique  (confidence: 0.87)
```

The post uses slang, all caps, and letter repetition - all of which are typical of a `fandom_expression`. However, the model understandably predicted it as `artistic_critique` because underneath the hype, the post is complementing a song on the album. The model seems to miss the post's highly informal tone and instead focuses mostly on the content (so much so that it is 87% confident on the wrong label), which led it to predict `artistic_critique` over `fandom_expression`.

#### 2

```
Text:      NOT Future's verses are better than Taylor's I'm dead
True:      fandom_expression
Predicted: artistic_critique  (confidence: 1.00)
```

This post complements one artist's lyrics over another artist's lyrics in one song, but more importantly, it uses the rhetorical (and all-caps) "NOT" and informal humorous expression ("I'm dead"). The model incorrectly predicted `artistic_critique` with certainty because the post contains some lyrical comparison and doesn't use all caps, but it does subtly use an overall informal and humorous tone that should've tipped the balance in favor of `fandom_expression`.

#### 3

```
Text:      So when's her tour...?
True:      external_narrative
Predicted: fandom_expression  (confidence: 0.58)
```

This example is different than the other two: the model was only about half certain, and the model _did_ predict `fandom_expression` when it shouldn't have. This example is especially tricky because it bears the traits of a `fandom_expression`: it's short and begins with the informal/conversational "so". This is most likely why the classifier predicted `fandom_expression` - the traits of an `external_narrative` ("tour") were outnumbered by those for `fandom_expression`. This is yet again a tone misidentification issue.

### Sample Classifications

### Classifier Reflection

## Other Takeaways

## Spec Reflection

### Divergence

In `planning.md`, I originally opted for a stricter post selection process. In fact, I wanted each sample post collected from the megathread to be from unique users to ensure that the dataset maximizes different linguistic styles (each person has a distinct "way" of speaking). However, when collecting the samples, I reached the bottom of the megathread much sooner than I had expected:

- The 2.4k comment count in the thread's original post includes sub-replies too, which are forbidden as per my spec.
- Most likely there weren't 200+ unique posters in that thread.
- A significant amount of direct posts came from deleted accounts - again forbidden in my spec.

These factors strained my goal of collecting 200+ samples, so somewhere in the middle of the data collection process, I lifted the unique-users restriction. Luckily, I still ended up collecting samples from 169 unique users (see [`data/data_overview.ipynb`](./data/data_overview.ipynb)).

### Assistance

Despite the surprise divergence, the spec especially helped me in this project by getting me to plan and tighten my label definitions before data collection and annotation. This allowed me to annotate most samples with certainty. However, as with most real-world data, there were some challenging surprises, which (together with the [stress testing](./docs/stress_testing.md)) brought me to iterate on the label definitions and ambiguity resolution guidelines to address such cases in the future.

## AI Usage

- **Classification ideas**: After reading 30-40 posts in the megathread myself, I was struggling to find classification groups. I gave Gemini the link to the megathread and asked it to propose some labels with reasoning. On its first go, it essentially returned the 3 basic classification groups this project now uses, but the original label names were a bit clunky and hyper-specific: `sonic_lyrical_critique` and `persona_industry_context` (I found `fandom_expression` fitting from the beginning). These two sounded like they were listing attributes ("sonic or lyrical critique" and "persona or industry context"), which could be especially problematic with edge cases later on. I offered new, more general-sounding label names like `compositional_critique` and `meta_discussion` and my decision for choosing them. The AI then reasoned why these new labels were inadequate in their own ways (`compositional_critique` associates a bit too much with note arrangement and `meta_discussion` is a bit too fuzzy, including both moderator-type posts and celebrity news). It then counter-offered two more labels - and yes, these ended up being `artistic_critique` and `external_narrative`. I was happy with this result because the final three labels were concise and balanced breadth with specificity.
- **Annotation assistance**: I used Claude Code to pre-annotate 25 samples in the data. These samples are marked as `"claude_code"` in the `"annotators"` column. I did this for two reasons: to attempt to speed up my workflow (it didn't help that much), and to test my label definitions and ambiguity resolution guidelines (which was a success). I reviewed the AI annotations, ready to update the annotation myself if needed. However, to my surprise, all of its annotations matched what I would have given, so no re-prompt or manual override was needed.
- **Identify patterns in misclassified samples**: After classification, I again used Claude Code to find patterns in the 5 misclassifications by the fine-tuned model. It was moderately helpful, but it would've made a bigger difference had there been many more misclassifications to synthesize. I agreed with the model's heads-up about the tone-blindness when it came to `fandom_expression`, later finding my own patterns and writing [Misclassifications](#misclassifications) section myself.

---

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
