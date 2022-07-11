# Subtitle Generator for Amazon Polly
## Overview
This is a Python library that allows you to simultaneously generate audio and subtitle/captioning files.

## Features
* Supports all Polly audio formats (PCM, OGG, MP3)
* Supports both VTT and SRT subtitle/captioning formats
* Supports all Polly `synthesize_speech` parameters

## Installation
The library is not yet deployed to Github, so for now clone and install from local.

` pip install .`

## Usage (Command-Line)
To run from the command-line, you simply run `polly-vtt`.

````
Usage: polly-vtt [OPTIONS] BASE_FILENAME VOICE_ID OUTPUT_FORMAT TEXT

Options:
  --caption-format TEXT  'srt' or 'vtt'
  --help                 Show this message and exit.
````

`BASE_FILENAME`: Base filename for both the audio and caption files

`VOICE_ID`: Polly voice to use (Case-sensitive)

`OUTPUT_FORMAT`: Amazon Polly output format: pcm, mp3, ogg_vorbis

`TEXT`: Full text to be digitized

`--caption-format`: Caption format: srt or vtt

### Command-Line Example

This example generates a PCM audio file along with an SRT captions file.

````bash
$ polly-vtt testfile Joanna pcm "this is a test. this is a second sentence." --caption-format srt
testfile.wav written successfully.
testfile.wav.srt written successfully.
Total Audio Length: 0:00:03.017500
# of Sentences: 2
````


## Usage (In Code)
The example below shows how to generate captions. You simply call the `generate` method and pass the `filename`, `Text`, `VoiceId` and `OutputFormat`.

The default is VTT, but you can generate SRT files if you pass `srt` as the second parameter.

This example will create six files:

* pcm_testfile.wav
* pcm_testfile.wav.vtt
* mp3_testfile.mp3
* mp3_testfile.mp3.vtt
* ogg_testfile.ogg
* ogg_testfile.ogg.srt

### Code Example

~~~~python
from polly_vtt import PollyVTT

text = "News content is shaped by its own unique characteristics. Sentences and paragraphs are usually short and highly informative because writers have to compress information into a limited space. Depending on the theme, news articles may contain relevant terminology, place names, abbreviations, people’s names, and quotes. Excellent news writing is clear, precise, and avoids ambiguity. The writing is dynamic, especially in online articles, because content may get updated multiple times per day as new information becomes available."

polly_vtt = PollyVTT()


# pcm with VTT captions
polly_vtt.generate(
    "pcm_testfile",
    Text=text,
    VoiceId="Joanna",
    OutputFormat="pcm",
)

# mp3 with VTT captions
polly_vtt.generate(
    "mp3_testfile",
    Text=text,
    VoiceId="Joanna",
    OutputFormat="mp3",
)

# ogg with SRT captions
polly_vtt.generate(
    "ogg_testfile",
    "srt",
    Text=text,
    VoiceId="Joanna",
    OutputFormat="ogg_vorbis",
)
~~~~

### Contents of `testfile.mp3.vtt`
~~~~
WEBVTT

00:00:00.000 --> 00:00:06.480
In academic writing, readers expect each paragraph to have a sentence or two that captures its main point.

00:00:06.480 --> 00:00:12.272
They’re often called “topic sentences,” though many writing instructors prefer to call them “key sentences.

00:00:12.272 --> 00:00:15.765
There are at least two downsides of the phrase “topic sentence.

00:00:15.765 --> 00:00:21.932
First, it makes it seem like the paramount job of that sentence is simply to announce the topic of the paragraph.

00:00:21.932 --> 00:00:27.600
Second, it makes it seem like the topic sentence must always be a single grammatical sentence.

00:00:27.600 --> 00:00:32.730
Calling it a “key sentence” reminds us that it expresses the central idea of the paragraph.

00:00:32.730 --> 00:00:36.520
And sometimes a question or a two-sentence construction functions as the key.
~~~~

### Contents of `testfile.ogg.srt`
~~~~
1
00:00:00,000 --> 00:00:06,480
In academic writing, readers expect each paragraph to have a sentence or two that captures its main point.

2
00:00:06,480 --> 00:00:12,272
They’re often called “topic sentences,” though many writing instructors prefer to call them “key sentences.

3
00:00:12,272 --> 00:00:15,765
There are at least two downsides of the phrase “topic sentence.

4
00:00:15,765 --> 00:00:21,932
First, it makes it seem like the paramount job of that sentence is simply to announce the topic of the paragraph.

5
00:00:21,932 --> 00:00:27,600
Second, it makes it seem like the topic sentence must always be a single grammatical sentence.

6
00:00:27,600 --> 00:00:32,730
Calling it a “key sentence” reminds us that it expresses the central idea of the paragraph.

7
00:00:32,730 --> 00:00:36,417
And sometimes a question or a two-sentence construction functions as the key.
~~~~
