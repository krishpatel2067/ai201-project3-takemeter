# Planning

## Community

I chose a [Reddit megathread](https://www.reddit.com/r/popheads/comments/7brx3o/megathread_taylor_swift_reputation/) about Taylor Swift's 6th studio album, _reputation_. This megathread contains thousands of posts around a focused discussion that can still be cleanly categorized - a perfect candidate for a fine-tuned classification task.

It is important to classify various types of posts apart. For example, posts about the actual lyrics or music are fundamentally different than posts about the news surrounding an album drop, which are both fundamentally different than posts that merely contain emotional or hyped-up text. The first type may lead to in-depth, analytical discussion. The second type may involve stats and numbers about fame and success. The third type are often standalone statements that often wouldn't start a sub-discussion. Furthermore, different people may be interested in different categories, so from a forum's perspective, this sort of pre-categorization could pave the way for filtering options to allow users to find the types of posts they want.

## Label Definitions

- `artistic_critique` - Primarily contains analysis of the artwork itself and artistic choices (e.g., sound, composition, melody, rhythm, lyrics, genre, production, album song order, artistic evolution, comparisons with other artistic works, etc). Also includes emotions and opinions expressed because of the artwork and artistic choices. Tone must be mostly matter-of-fact with minimal to no joking, slang, caps, etc.

[**Clear Example 1**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dplxex5):

> I'm not going to go track by track because I don't want to rain on the parade of those who are loving this.
>
> So I will just say that as a longtime Taylor Swift fan, this is the album I have to sit out. Her last three albums are 9s or 10s in my book, and "Fearless" is solid too, but this... This, I just don't get.
>
> On the positive end, "Getaway Car" is the standout, IMHO. It has the best lyrics of the album -- the one moment where I see glimpses of the songwriter I've always loved. I like the chorus. The verses are OK. But I hate the bridge. Wow, am I over Bonnie & Clyde references. The bridge feels cheesy and cliche in the middle of an otherwise fairly solid song. Of what we already knew, "...Ready For It?" still has some fun, catchy moments (except the verses, which I hate), but... still not a song I love. Those verses, man.
>
> Beyond that... I am honestly just so disappointed. I even tried to go in with low expectations. But I thought there'd be something I'd love. I've listened twice and I just don't connect with this album. There isn't a single song I just unabashedly like from start to finish. Not even love, but like. I like parts of a few songs but nothing as a whole.
>
> The lyrics are weak, the production seems way overdone on many of the tracks and I just don't feel what she's going for. I don't feel much of anything most of the time, which is not something I expect from Taylor Swift. She's a masterful storyteller, able to capture any emotion or moment in song, and her music has always reached people in a deeply emotional way. I don't feel that this time. This album feels empty to me. And often cringey.
>
> I expect downvotes; it's cool, I accept it. But as a longtime Swiftie who's baffled tonight, I just needed to throw this out into the void. For those who are loving it, enjoy. I'll give it another listen another day. But I don't get this record. At all.

by MissyBee37.

[**Clear Example 2**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkwhq0):

> This album is gonna sound extremely dated in like six months, she should've stuck with a more traditional sound and stop trend chasing so much.
>
> EDIT: Getaway Car being the clear exception, amazing song. God bless Jack Antonoff.

by Number3rdInTheVoting.

[**Ambiguous Example**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpn7hlc):

> Even upon first listen, "Getaway Car" became my favorite song of the year. Its got everything I want from Taylor and Jack: 'this love couldn't last' lyrics, a propulsive beat, and Jack's 80s production. I don't care if it is really close to Out Of The Woods.

> And that outro? Jee-zus. Killed me.

by GuitarzanWSC.

- `external_narrative` - Primarily contains stories or discussion about the broader context (e.g. current events, gossip, celebrity feuds/drama, Billboard charts, sales, reviews, etc.). Includes personal context too, such as discussion about people and situations around the post publisher (e.g. mentions of family, friends, roommates; decisions to buy the album; etc.). Tone must be mostly matter-of-fact with minimal to no joking, slang, caps, etc

[**Clear Example 1**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkxpas):

> No one is going to believe me, but I have a friend whose brother's coworker briefly dated Taylor Swift. He said that on their first date they went to a restaurant and Taylor ordered two different bowls of soup and mixed them together one spoonful at a time before eating both bowls mixed together as one soup

by ComeOnAndSlang.

[**Clear Example 2**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkt8a6):

> Haven't heard it yet, but the Taylor sub is weirdly very unhappy with this. It really makes me worried if even the devotees are criticizing it. Still hopeful though!

by glasscageheart.

[**Ambiguous Example**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpke04g):

> This is the first time I've been witness to a Taylor Swift album cycle from it's very beginning til now and I have to say what a wild ride it's been. From the rumours of the RFI remix to the theory's about the snake being a dragon and how that ties into the eclipse. As someone who's big into conspiracy theories this has been a blast and I hope to god the album is good. 1989 is my favourite album of all time and I know this won't live up to it, but man I hope it's even half as good.
>
> Also please let End Game be a bop because if I'm gonna have to listen to the same Ed Sheeran song over and over on the radio, at least let it feature my queen. Also Future."

by animefangrant62.

- `fandom_expression` - Primary contains standalone emotional assertions, visceral reactions, or pure exclamations without much logic or elaboration (e.g., hype, witty remark, meta-joke, exaggeration, etc.). Sometimes can mix in artwork opinions and current event mentions, but is often distinguishable by a strong use of slang, all caps, emojis, etc.

[**Clear Example 1**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkcocf):

> I’ve already broken up with my boyfriend in preparation."

by LittleRhodey.

[**Clear Example 2**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkg9l6):

> I had a dream last night where I heard Dress and it was a complete and total BOP and it was one of the best songs she ever did
>
> Hoping my dream is true

by InfernalSolstice.

[**Ambiguous Example**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dplnquc):

> Is...is something wrong with me? Cause “This is Why We Can’t Have Nice Things” is a bop and I am LIVING for it

by weareallmoist.

## Addressing Ambiguous Edge Cases

There will be cases where the labeling is ambiguous. For example, a post may include both gossip from the music industry and a brief note about the lyrical structure of a song. Should that be classified as `artistic_critique` or `external_narrative`? Another post may be talking about album leaks but uses all caps and repeated letter (e.g. "OMGGGGG IT LEAKED") - is this `external_narrative` or `fandom_expression`?

To resolve such cases, follow these guidelines in order:

1. Don't look at content alone - check the tone too. An overly informal tone with a heavy use of slang, caps, etc. is a strong case for `fandom_expression`.
2. Choose the label that represents the at least 2/3 of the post's content. When using this criterion, there should be a clear winner.
3. If there's roughly an equal distribution of post content that can match multiple labels, and the decision is between `artistic_critique` and `external_narrative`, choose the label that forms the main idea or conclusion reached in the post. For example, if celebrity feuds are cited as the reason for a song's beat, then `artistic_critique` takes precedence. Additionally quoted content should not be used as the basis for classification. For example, if someone talks about reviews and pastes a long quote from a review site, the post is still `external_narrative` even if most of the post content may now technically be feedback-oriented due to the excerpt.
4. If there is no clear main idea or conclusion in the post, or if one of the label candidates is `fandom_expression`, use this strict prioritization: `artistic_critique` takes priority over `external_narrative`, which takes priority over `fandom_expression`.

Justification:

1. `fandom_expression`s stand out in their own way. One type of `fandom_expression`s includes social-media-slang phrases with no direct meaning (e.g. "YASS QUEEN"), which are easy to identify since they barely contain any artwork discussion, opinions, gossip on surrounding developments, etc.. Other types are more subtle, often mixing in content that should belong to the other two labels. However, such posts still uses a lighthearted tone, slang, caps, emojis, etc. to convey opinions or current event info (e.g. "This song got me DANCING!"). This guideline helps pre-filter most `fandom_expression`s correctly, leaving the decision primarily between `artistic_critique` and `external_narrative` - though some `fandom_expression`s may slip through.
2. If a post is overwhelmingly diving into the lyrical and musical content of a song while including just a short phrase with music industry gossip, one would summarize the post as per its artistic discussion. Thus, `artistic_critique` is the clear winner. Such cases are only ambiguous in the strictly speaking, but practically they can be easily disambiguated.
3. Quoted content shouldn't contribute to the labeling decision - rather, the context in which the quote was used. The point above already gives an example of a review excerpt, which is perfect to show why this guideline is needed. If a post uses celebrity news as evidence for certain lyrical choices, then clearly the celebrity news plays into the overall argument about lyrical choices. Thus, the main idea in each post is important to consider. However, this sort of analysis doesn't work well with `fandom_expression`s because these can essentially never be used as the central idea of a post - otherwise, now there is justification or elaboration, contradicting what a `fandom_expression` is. If they are used subordinately in the post, then the prioritization in the next step takes care of that.
4. Sometimes, posts (especially large ones) can touch on multiple topics and span multiple labels equally. In this case, there is no clear winner by majority. Instead, one label needs to be prioritized above the rest. `artistic_critique` is often rarer and requires more effort to devise and write (especially in casual social media platforms like Reddit), so it should get the highest priority in an equal-distribution ambiguity. `fandom_expression`s are often purely about expressing opinion, affinity, or hype as per human subjectivity without clear logic, reason, or elaboration. A reader could not reasonably gain knowledge by reading it. Such posts are quite common on casual social media, and don't require much effort to post (instead relying on expressivity instincts). Thus, these should be prioritized last, leaving `external_narrative` in middle.

## Ambiguous Examples Found During Annotation

**ID 68**:

> Okay everyone is hating on So It Goes... but honestly it is my favourite track on the album, coming from someone who isn't exactly the greatest fan of Taylor.

**Label**: `artistic_critique`

This post contains discussion about the thread itself and the post publisher generally not being a Taylor Swift fan, initially fitting `external_narrative`. However, the post also mentions a favorite song on the album, clearly `artistic_critique`. The "greatest fan" part is used to give perspective to the favorite pick, which is why `artistic_critique` wins out, dominating the others "hating on" part.

**ID 79**:

> Explicit lyrics!!

**Label**: `fandom_expression`

The post mentions that the album contains explicit lyrics. However, while it talks about the lyrical content (fitting `artistic_critique`), it is very vague and does not elaborate upon these words. Such short exclamations fit better in `fandom_expression`.

**ID 198**:

> "my mistakes have been used against me" girl what? oh ffs

**Label**: `external_narrative`

This one is especially tricky. The quote refers to Taylor Swift, after some research, the quoted words don't seem like they're lyrics from a Taylor Swift song. Instead they must be from an interview or other setting, which is outside the domain of `artistic_critique`. Yet, a classifier would easily label the post as such, thinking the quoted content is lyrics. Perhaps a more advanced model (an LLM with ample training data) would be able to pull in the necessary context to correctly classify it as `external_narrative`.

## Data Collection Plan

I will manually copy-paste suitable posts from the Reddit megathread in a CSV file, additionally storing not just the label but also the link and poster username for future discovery and uniqueness enforcement purposes.

Not all posts from the megathread will be chosen. Specifically, posts:

- Must be direct replies to the original post (no replies to replies)
- Must be unique by poster's username
- Must be loosely related to the main topic
- Must be family-friendly
- Must _not_ be by deleted users

I will collect around 200 samples, aiming to distribute the 3 labels evenly - thus, around 60-70 samples per label. Some labels may be harder to find samples for than others, leading to them being underrepresented. In such a case, I will broaden my search (e.g., scrolling much farther down) in an attempt to find a more even distribution of posts. If that doesn't work, I will consider modifying the label definitions and/or boundaries, re-labeling the samples as needed afterward.

## Evaluation Metrics

I will use the following evaluation metrics:

- **Overall accuracy** - Measure of how many overall samples the model classified correctly over the total number of samples - the simplest metric about overall classification quality, though misleading if used alone.
- **Per-class accuracy** - Measure of how many samples in each class the model correctly predicted. Gives a more complete picture than overall accuracy.
- **Precision** - Given all the samples the model predicted for a certain label, what fraction are actually in that label? High precision and low recall means that the model is conservative, needing higher confidence but under-classifying for that label.
- **Recall** - Given all the samples for a certain label, what fraction did the model classify as that label? High recall and low precision means the model is zealous, needing lower confidence and over-classifying for that label.
- **F1** - Harmonic mean of precision and recall. Since precision and recall are both difficult to nail, this single number distinguish a great classifier from a good one.

Multiple metrics are needed because relying on just one gives an incomplete picture:

- A high overall accuracy may hide disastrously bias due to data imbalance and/or low accuracy for a particular class.
- A per-class accuracy gives a better picture, but it also says nothing about the classifier's conservativeness or zealousness. [TODO]
- A high precision may simply be due to the classifier being overly conservative, perhaps classifying too few samples as a certain label and inflating the precision.
- A high recall may simply be due to the classifier being overly zealous, perhaps classifying too many samples as a certain label and inflating the recall.

## Definition of Success

In an ideal world, overall accuracy, per-class accuracy, recall, precision, and F1 would all be 1. However, this is practically not possible and is even a little suspicious. Thus, a threshold value needs to be chosen for all the metrics. Purely guessing one of the three labels leads to a baseline accuracy of 33%, so the threshold must be meaningfully greater than this to yield a useful classifier. A good value I've decided to aim for is **0.75** for all the four metrics. I would personally be satisfied with a classifier achieving this level of performance, but to deploy the classifier in the real world, I would aim for a higher threshold of around 0.9 so that users would rarely have to encounter mistakes.

## AI Tool Plan

### Label Stress-Testing

I will use AI to generate 5-10 posts that sit on the boundaries between labels to test whether the definitions are specific enough to address such ambiguous cases. This will allow me to revise my definitions if I find that I can't reasonably classify some of these generated posts.

### Annotation Assistance

Labeling all 200 samples by myself may be difficult, but I can speed that up a bit by having an LLM annotate some of the posts, especially those that are easy to classify. I will have the LLM mark its annotations by via a specific value in a specific column in the CSV data, for example "llm" for the "annotator" column. This will help me review the LLM-annotated samples and disclose easily where and how much AI helped me with this task.

### Failure Analysis

After running the classifier for the first time, identifying the failure patterns in the first place may be difficult alone, so I will ask an AI tool to surface these patterns. Perhaps there is a subtle direction to the failures (e.g. a lot of misclassified `artistic_critique`s being labeled as `external_narrative`s). I will verify the patterns the LLM identifies. Together this flow will help me speed up my failure analysis and evaluation report sections while ensuring integrity by using my own judgement for approval.
