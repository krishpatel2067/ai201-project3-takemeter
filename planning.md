# Planning

## Community

I chose a [Reddit megathread](https://www.reddit.com/r/popheads/comments/7brx3o/megathread_taylor_swift_reputation/) about Taylor Swift's 6th studio album, _reputation_. This megathread contains thousands of posts around a focused discussion that can still be cleanly categorized - a perfect candidate for a fine-tuned classification task.

It is important to classify various types of posts apart. For example, posts about the actual lyrics or music are fundamentally different than posts about the news surrounding an album drop, which are both fundamentally different than posts that merely contain emotional or hyped-up text. The first type may lead to in-depth, analytical discussion. The second type may involve stats and numbers about fame and success. The third type are often standalone statements that often wouldn't start a sub-discussion. Furthermore, different people may be interested in different categories, so from a forum's perspective, this sort of pre-categorization could pave the way for filtering options to allow users to find the types of posts they want.

## Label Definitions

- `artistic_critique` - Primarily contains analysis of the artwork itself and artistic choices (e.g., sound, composition, melody, rhythm, lyrics, genre, production, album song order, comparisons with other artistic works, etc).

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

- `external_narrative` - Primarily contains stories or discussion about the broader context (e.g., gossip, celebrity feuds/drama, Billboard charts, sales, reviews, etc.).

[**Clear Example 1**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkxpas):

> No one is going to believe me, but I have a friend whose brother's coworker briefly dated Taylor Swift. He said that on their first date they went to a restaurant and Taylor ordered two different bowls of soup and mixed them together one spoonful at a time before eating both bowls mixed together as one soup

by ComeOnAndSlang.

[**Clear Example 2**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpkc7hb):

> I haven't felt this amount of both hyped and concerned since election night exactly one year ago. Let's hope tonight doesn't end with the same feeling of utter disappointment.

by thegeecyproject.

[**Ambiguous Example**](https://www.reddit.com/r/popheads/comments/7brx3o/comment/dpke04g):

> This is the first time I've been witness to a Taylor Swift album cycle from it's very beginning til now and I have to say what a wild ride it's been. From the rumours of the RFI remix to the theory's about the snake being a dragon and how that ties into the eclipse. As someone who's big into conspiracy theories this has been a blast and I hope to god the album is good. 1989 is my favourite album of all time and I know this won't live up to it, but man I hope it's even half as good.
>
> Also please let End Game be a bop because if I'm gonna have to listen to the same Ed Sheeran song over and over on the radio, at least let it feature my queen. Also Future."

by animefangrant62.

- `fandom_expression` - Primary contains emotional assertions and visceral reactions without much logic or elaboration (e.g., hype, witty remark, meta-joke etc.)

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

There will be cases where the labeling is ambiguous. For example, a post may include both gossip from the music industry and a brief note about the lyrical structure of a song. Should that be classified as `artistic_critique` or `external_narrative`?

To resolve such cases, follow these guidelines in order:

1. Choose the label that represents the majority of the post's content. When using this criterion, there should be a clear winner.
2. If there is roughly an equal distribution of post content that can match multiple labels, `artistic_critique` takes priority over `external_narrative`, which takes priority over `fandom_expression`.

The justification:

1. If a post is overwhelmingly diving into the lyrical and musical content of a song while including just a short phrase with music industry gossip, one would summarize the post as per its artistic discussion. Thus, `artistic_critique` is the clear winner. Such cases are only ambiguous in the strictly speaking, but practically they can be easily disambiguated.
2. Sometimes, posts (especially large ones) can touch on multiple topics and span multiple labels equally. In this case, there is no clear winner by majority. Instead, one label needs to be prioritized above the rest. `artistic_critique` is often rarer and requires more effort to devise and write (especially in casual social media platforms like Reddit), so it should get the highest priority in an equal-distribution ambiguity. `fandom_expression`s are often purely about expressing opinion, affinity, or hype as per human subjectivity without clear logic, reason, or elaboration. A reader could not reasonably gain knowledge by reading it. Such posts are quite common on casual social media, and don't require much effort to post (instead relying on expressivity instincts). Thus, these should be prioritized last, leaving `external_narrative` in middle.

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

- ## AI Tool Plan

[TODO]
