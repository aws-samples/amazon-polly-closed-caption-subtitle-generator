import os

from setuptools import setup

# Declare your non-python data files:
# Files underneath configuration/ will be copied into the build preserving the
# subdirectory structure if they exist.
data_files = []
for root, dirs, files in os.walk("configuration"):
    data_files.append(
        (os.path.relpath(root, "configuration"), [os.path.join(root, f) for f in files])
    )

setup(
    name="SubtitleGeneratorForPolly",
    version="0.1.3",
    # declare your packages
    packages=["polly_vtt"],
    install_requires=["boto3", "click", "librosa", "pyaml", "webvtt-py"],
    entry_points="""
        [console_scripts]
        polly-vtt=polly_vtt:main.main
    """,
)
