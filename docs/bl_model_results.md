# Baseline Model Results

Model: `llama-3.3-70b-versatile`

## 1

### Changes

None - first run.

### Classification Report

```
🎯 Baseline accuracy: 1.000  (evaluated on 32/32 parseable responses)

Per-class metrics (baseline):
                    precision    recall  f1-score   support

 artistic_critique       1.00      1.00      1.00        14
external_narrative       1.00      1.00      1.00        12
 fandom_expression       1.00      1.00      1.00         6

          accuracy                           1.00        32
         macro avg       1.00      1.00      1.00        32
      weighted avg       1.00      1.00      1.00        32
```

## 2

### Changes

Fixed copy-paste error where the `fandom_expression` label definition was the same as `external_narrative`.

### Classification Report

```
🎯 Baseline accuracy: 0.968  (evaluated on 31/32 parseable/non-skipped responses)

Per-class metrics (baseline):
                    precision    recall  f1-score   support

 artistic_critique       0.93      1.00      0.97        14
external_narrative       1.00      0.91      0.95        11
 fandom_expression       1.00      1.00      1.00         6

          accuracy                           0.97        31
         macro avg       0.98      0.97      0.97        31
      weighted avg       0.97      0.97      0.97        31
```
