import math
import wave

import boto3
import librosa

class Polly:
    def __init__(self, **kwargs):
        self.client = boto3.client("polly")
        self.defaults = {
            "Engine": "neural",
            "LanguageCode": "en-US",
            "OutputFormat": "pcm",
            "SampleRate": "16000",
        }

    def connect(self):
        try:
            response = self.client.describe_voices()
            return True
        except Exception as e:
            return False

    def synthesize(self, base_filename, **params):
        resp, filename, length = self.synthesize_speech(base_filename, **params)
        resp_sm = self.synthesize_speech_marks(**params)
        return resp_sm, filename, length

    def synthesize_speech(self, base_filename, **params):
        request_params = {**self.defaults, **params}
        response = self.client.synthesize_speech(**request_params)
        filename = f'{base_filename}.{self.get_file_type(request_params["OutputFormat"])}'
        if request_params["OutputFormat"] == "pcm":
            frames = []
            stream = response["AudioStream"]
            frames.append(stream.read())
            with wave.open(filename, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(int(request_params["SampleRate"]))
                wf.writeframes(b"".join(frames))
                wf.close()
        else:
            with open(filename, "wb") as file:
                file.write(response["AudioStream"].read())
        print(f"{filename} written successfully.")
        return response, filename, self.get_audio_length_in_ms(filename)

    def synthesize_speech_marks(self, **params):
        params["OutputFormat"] = "json"
        params["SpeechMarkTypes"] = ("sentence",)
        request_params = {**self.defaults, **params}
        return self.client.synthesize_speech(**request_params)

    def get_audio_length_in_ms(self,filename):
      y, sr = librosa.load(filename)
      return 1000*librosa.get_duration(y=y, sr=sr)

    def get_file_type(self, format):
        if format == "pcm":
            return "wav"
        if format == "ogg_vorbis":
            return "ogg"
        if format == "mp3":
            return "mp3"
