# ai201-project3-takemeter

For the CodePath course AI201: Applications of AI Engineering

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

Label distribution:

```
artistic_critique     89
external_narrative    84
fandom_expression     40
```

Classification report:

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
