import datetime
import json
import math
import re

from webvtt import Caption, WebVTT


class VTT:
    def __init__(self, **kwargs):
        self.polly_response = kwargs.get("PollyResponse")
        self.filename = kwargs.get("Filename")
        self.audio_length_in_ms = kwargs.get("AudioLengthInMs")
        self.format = kwargs.get("Format", "vtt")
        self.vtt = WebVTT()

    def remove_ssml_tags(self, text):
        return re.sub(r"\<[^>]*>", "", text)

    def to_sentences(self, response):
        return [
            json.loads(sentence.decode("utf8"))
            for sentence in response["AudioStream"].iter_lines()
        ]

    def format_vtt_time(self, msecs):
        minutes = math.floor(msecs / 60000)
        seconds = math.floor((msecs % 60000) / 1000)
        millis = int(msecs % 1000)
        return f"{minutes:02}:{seconds:02}.{millis:03}"

    def write(self, **kwargs):
        filename = f"{self.filename}.{self.format}"
        sentences = self.to_sentences(self.polly_response)
        for i in range(0, len(sentences)):
            start = sentences[i]["time"]
            if i == len(sentences) - 1:
                end = self.audio_length_in_ms - 200
            else:
                end = sentences[i + 1]["time"]
            sentence = self.remove_ssml_tags(sentences[i]["value"])
            caption = Caption(
                self.format_vtt_time(start),
                self.format_vtt_time(end),
                [sentence],
            )
            self.vtt.captions.append(caption)

        with open(filename, "w") as vf:
            if self.format == "srt":
                self.vtt.write(vf, format="srt")
            else:
                self.vtt.write(vf, format="vtt")
        print(
            f"{filename} written successfully.\nTotal Audio Length: {str(datetime.timedelta(seconds=self.audio_length_in_ms/1000))}\n# of Sentences: {len(sentences)}"
        )
