# Fine-Tuned Model Results

Model: `distilbert-base-uncased`

## 1

### Changes

None - first run.

### Epoch Metrics

```
Epoch	Training Loss	Validation Loss	    Accuracy
1	    1.107224	    1.101052	        0.406250
2	    1.077689	    1.072052	        0.406250
3	    1.049528	    1.028136	        0.406250
```

### Classification Report

```
🎯 Fine-tuned model accuracy: 0.438

Per-class metrics (fine-tuned model):
                    precision    recall  f1-score   support

 artistic_critique       0.44      1.00      0.61        14
external_narrative       0.00      0.00      0.00        12
 fandom_expression       0.00      0.00      0.00         6

          accuracy                           0.44        32
         macro avg       0.15      0.33      0.20        32
      weighted avg       0.19      0.44      0.27        32
```

### Confusion Matrix

[TODO]

## 2

### Changes

None - just full re-run.

### Epoch Metrics

```
Epoch	Training Loss	Validation Loss	    Accuracy
1	    0.998683	    1.009229	        0.593750
2	    0.989659	    0.991120	        0.562500
3	    0.949870	    0.953905	        0.593750
```

### Classification Report

```
🎯 Fine-tuned model accuracy: 0.594

Per-class metrics (fine-tuned model):
                    precision    recall  f1-score   support

 artistic_critique       0.52      0.93      0.67        14
external_narrative       0.86      0.50      0.63        12
 fandom_expression       0.00      0.00      0.00         6

          accuracy                           0.59        32
         macro avg       0.46      0.48      0.43        32
      weighted avg       0.55      0.59      0.53        32
```

### Confusion Matrix

[TODO]

## 3

### Changes

(Gemini-assisted)

Default hyperparameters didn't work well for my small dataset:

- 70% train split; 200 total samples -> 140 training samples
- `per_device_train_batch_size=16` -> 140 / 16 ~ 9 steps per epoch
- `num_train_epochs=3` -> ~27 training steps
- `warmup_steps=50` (>`27`) -> `learning_rate` never reaches `2e-5`

```
training_args = TrainingArguments(
    # ... other args the same ...
    num_train_epochs=6,
    warmup_steps=5,
    logging_steps=5,
)
```

### Epoch Metrics

```
Epoch	Training Loss	Validation Loss	    Accuracy
1	    0.994059	    0.966342	        0.593750
2	    0.849816	    0.903359	        0.687500
3	    0.759418	    0.842064	        0.656250
4	    0.643652	    0.797794	        0.687500
5	    0.554433	    0.772834	        0.687500
6	    0.493413	    0.763705	        0.687500
```

### Classification Report

```
🎯 Fine-tuned model accuracy: 0.688

Per-class metrics (fine-tuned model):
                    precision    recall  f1-score   support

 artistic_critique       0.60      0.86      0.71        14
external_narrative       0.83      0.83      0.83        12
 fandom_expression       0.00      0.00      0.00         6

          accuracy                           0.69        32
         macro avg       0.48      0.56      0.51        32
      weighted avg       0.57      0.69      0.62        32
```

### Confusion Matrix

[TODO]

## 4 ⭐

### Changes

Use the empirically derived optimal number of epochs:

### Epoch Metrics

```
Epoch	Training Loss	Validation Loss	    Accuracy
1	    0.000000	    3.044901	        0.687500
2	    0.000000	    3.073071	        0.687500
3	    0.000000	    3.141945	        0.687500
4	    0.000000	    3.205523	        0.687500
5	    0.000000	    3.246663	        0.687500
6	    0.000000	    3.277053	        0.687500
7	    0.000000	    3.294574	        0.687500
8	    0.000000	    3.300982	        0.687500
9	    0.000000	    3.308626	        0.687500
10	    0.000000	    3.309492	        0.687500
```

### Classification Report

```
🎯 Fine-tuned model accuracy: 0.844

Per-class metrics (fine-tuned model):
                    precision    recall  f1-score   support

 artistic_critique       0.81      0.93      0.87        14
external_narrative       0.91      0.83      0.87        12
 fandom_expression       0.80      0.67      0.73         6

          accuracy                           0.84        32
         macro avg       0.84      0.81      0.82        32
      weighted avg       0.85      0.84      0.84        32
```

### Confusion Matrix

### Wrong Predictions

```
Wrong predictions: 5 / 32

--- #1 ---
Text:      "He Said She Said" ~ Taylor on TIWWCHNT

Me: https://youtu.be/4sTHw7HEfHo
True:      artistic_critique
Predicted: external_narrative  (confidence: 1.00)

--- #2 ---
Text:      DANCING WITH OUR HANDS TIED IS A BANGERRRR
True:      fandom_expression
Predicted: artistic_critique  (confidence: 0.87)

--- #3 ---
Text:      In two to three years I would like to see how would we look back at this album.
True:      external_narrative
Predicted: artistic_critique  (confidence: 0.53)

--- #4 ---
Text:      So when's her tour...?
True:      external_narrative
Predicted: fandom_expression  (confidence: 0.58)

--- #5 ---
Text:      NOT Future's verses are better than Taylor's I'm dead
True:      fandom_expression
Predicted: artistic_critique  (confidence: 1.00)
```
