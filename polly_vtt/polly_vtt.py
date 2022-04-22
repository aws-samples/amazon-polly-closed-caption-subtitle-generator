from .polly import Polly
from .vtt import VTT


class PollyVTT:
    def __init__(self, **kwargs):
        self.polly = Polly()

    def generate(self, filename, format="vtt", **polly_params):
        resp, filename, length = self.polly.synthesize("testfile", **polly_params)
        vtt = VTT(AudioLengthInMs=length, PollyResponse=resp, Filename=filename, Format=format)
        vtt.write()
