from polly_vtt import PollyVTT

text = "In academic writing, readers expect each paragraph to have a sentence or two that captures its main point. They’re often called “topic sentences,” though many writing instructors prefer to call them “key sentences.” There are at least two downsides of the phrase “topic sentence.” First, it makes it seem like the paramount job of that sentence is simply to announce the topic of the paragraph. Second, it makes it seem like the topic sentence must always be a single grammatical sentence. Calling it a “key sentence” reminds us that it expresses the central idea of the paragraph. And sometimes a question or a two-sentence construction functions as the key."

polly_vtt = PollyVTT()
polly_vtt.generate(
    "testfile",
    Text=text,
    VoiceId="Joanna",
    OutputFormat="pcm",
)

polly_vtt.generate(
    "testfile",
    Text=text,
    VoiceId="Joanna",
    OutputFormat="mp3",
)

polly_vtt.generate(
    "testfile",
    "srt",
    Text=text,
    VoiceId="Joanna",
    OutputFormat="ogg_vorbis",
)
