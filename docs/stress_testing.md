# Stress Testing

- Done before full annotated started to tighten definitions if needed.
- Used Claude Code to generate the following 10 ambiguous samples.
- Each sample is followed by the label I assigned, reasoning for both the ambiguity and the labeling decision, and any definition tweaks if needed.
- Most of the samples focus on the `artistic_critique` and `external_narrative` boundary as it is the trickiest one (actual `fandom_expression`s are often standalone, otherwise subdued by the other two in content amount or centrality).

## Sample 1

> Gorgeous might genuinely be the best song she has ever written. Those layered harmonies in the chorus and the way her voice drops on the word "boyfriend" — I genuinely don't have words for what this does to me.

- **Label**: `artistic_critique`
- **Reasoning**: The sample is ambiguous because it mixes artistic and sonic discussion ("harmonies" and "voice drops") with heartfelt feelings ("don't have words"). However, only the last part fits `fandom_expression`, while everything up to the dash fits `artistic_expression` since it's about songwriting comparison, harmonies, and vocals.
- **Definition adjustments**: None

## Sample 2

> Refreshing Billboard every hour today and when it finally hit number 1 I screamed so loud my roommate ran in thinking something was wrong. She really said hold my beer to every single doubter.

- **Label**: `external_narrative`
- **Reasoning**: This sample mixes `external_narrative` elements ("Billboard" and "hit number 1") with personal emotion and exaggeration ("screamed so loud") common in `fandom_expression`s. However, this should be classified as `external_narrative` because the reference to the Billboard charts is strong and central to the post.
- **Definition adjustments**: Add post publisher's personal context (e.g. stories about roommates) into the definition for `external_narrative`.

## Sample 3

> The production on this album is noticeably darker and more synth-industrial than 1989, which honestly makes sense when you consider everything that went down between her, Katy, and Kim over the past two years.

- **Label**: `artistic_critique`
- **Reasoning**: This sample mixes both elements fitting both `artistic_critique` ("darker", "synth-industrial", and "1989") and `external_narrative` ("Katy, and Kim"). Because the external narrative fits into the reasoning behind the album's attributes, the former simply supports that latter, which is the true main idea of the post.
- **Definition adjustments**: Add a way to disambiguate between between `artistic_critique` and `external_narrative` labels on the basis of centrality to the post's content.

## Sample 4

> Delicate is genuinely everything. The way the synths just sort of hover around her voice like they're afraid to touch it — I don't know how to describe it, it's just deeply comforting and I've had it on loop for six hours.

- **Label**: `artistic_critique`
- **Reasoning**: This sample mixes elements from `fandom_expression` ("genuinely everything" and " on loop for six hours") and `artistic_critique` ("synths" and "voice). However, the emotions expressed (even if in slight exaggeration) are a result of the artistic choices in the song and the post publisher's observations of them.
- **Definition adjustments**: Add emotions and opinions resulting from the artistic decisions as a case for `artistic_critique`.

## Sample 5

> Pitchfork gave it a 6 and honestly the one thing they got right is that the middle section drags — This Is Why We Can't Have Nice Things through Gorgeous just doesn't land as hard as the first three tracks do.

- **Label**: `artistic_critique`
- **Reasoning**: The post mentions external reviews ("Pitchfork" and "6") while also critiquing two songs in the middle of the album. However, the cited review is used in support of the main point of the post about the strength of the two songs mentioned.
- **Definition adjustments**: Same as in [Sample 3](#sample-3).

## Sample 6

> She outsold every album released in 2017 combined in a single week and I will never not bring this up to everyone who said her career was over after the Kimye stuff.

- **Label**: `external_narrative`
- **Reasoning**: The post mentions sales and "the Kimye stuff" (fitting of `external_narrative`) as well as some exaggeration elements like "never not" (fitting of `fandom_expression`). However, most of the post content is dominated by the `external_narrative`, with the `fandom_expression` being used very lightly.
- **Definition adjustments**: Tighten `fandom_expression` definition to only include standalone expressions without any justification.

## Sample 7

> New Year's Day sounds completely out of place next to the rest of the album and I think that's exactly why it works — the contrast with the synth-heavy tracks before it makes it hit harder than it would on literally any other record, and yes I cried.

- **Label**: `artistic_critique`
- **Reasoning**: The post discusses the standout feature of a song on the album (`artistic_critique`) and includes an emotional clause at the end (`fandom_expression`). The latter comprises very little of the post's content - most of the discussion is about the mentioned song's fit in the album.
- **Definition adjustments**: None - majority-wins disambiguation protocol worked nicely in this case.

## Sample 8

> The way she built the entire snake narrative across social media for months and then flipped it into the album cover and aesthetic is honestly genius brand strategy and I'm a little obsessed with how calculated and effective the whole rollout was.

- **Label**: `external_narrative`
- **Reasoning**: This post contains elements from `external_narrative` ("social media" and "brand strategy") and `artistic_critique` ("album cover and aesthetic"). However, the latter is lightly used while the former accounts for most of the post's content.
- **Definition adjustments**: None - see [Sample 7](#sample-7).

## Sample 9

> Call It What You Want uses a very similar chord structure and emotional register to Clean, which is interesting because she went from writing that kind of raw, vulnerable introspection to releasing this whole revenge-era album after being completely eaten alive in the press.

- **Label**: `artistic_critique`
- **Reasoning**: The post is mostly `artistic_critique` ("chord structure" and "emotional register"), while referencing some current events as `external_narrative`. However, the latter is dominated by the former, not to mention it is used to support the former point.
- **Definition adjustments**: None - see [Sample 7](#sample-7).

## Sample 10

> Getaway Car was always going to be the standout — Jack Antonoff clearly poured everything into that production — but seeing it chart so high while the Taylor-Katy drama is still tabloid fodder somehow makes listening to it feel even more satisfying than it should.

- **Label**: `artistic_critique`
- **Reasoning**: This one is tricky because it first starts with `artistic_critique` ("Getaway Car" - a song - and "Jack Antonoff" - a song producer), then moves to `external_narrative` ("chart so high" and "Taylor-Katy" drama), and finally ends with `artistic_critique` ("listening to it [...] more satisfying"). However, this sandwich structure emphasizes the hierarchy of the two labels in this post: `artistic_critique` is clearly the central idea and the `external_narrative` is used to reinforce the post publisher's emotions upon listening to the song.
- **Definition adjustments**: See [Sample 3](#sample-3) and [Sample 4](#sample-4).
