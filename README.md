audio-offset-finder, Calder White Fork
======================================

This fork uses the same underlying methods as the original root.
I was attempting to process multiple audio files on a 2 hour clip and the
original fork loads + processes the same 2 hour clip each time. So, I created an object
for this exact purpose called `OffsetFinder`. This is exclusive to the python module.
Using `OffsetFinder` you can find the offset on multiple sub-clips using the same pre-processed data
from the large, original clip.

Installation
============

```
pip install git+https://github.com/CalderWhite/audio-offset-finder.git
```

Usage
=====

```python
from audio_offset_finder import OffsetFinder


finder = OffsetFinder("file1.mp3")

# load + processes the large original file
finder.init()

# find the offset of the smaller clip within the finder.
# If the score is less than 9-10, the offset is no good.
offset, score = finder.find_offset("file2.mp3")
```




Here is the rest of the original README file.

---

audio-offset-finder
===================

A simple tool for finding the offset of an audio file within another
file. 

Uses cross-correlation of standardised Mel-Frequency Cepstral Coefficients,
so should be relatively robust to noise (encoding, compression, etc).

It uses ffmpeg for transcoding, so should work on all file formats
supported by ffmpeg.


Usage
-----

    $ audio-offset-finder --help
    $ audio-offset-finder --find-offset-of file1.wav --within file2.wav
    Offset: 300 (seconds)

Testing
-------

    $ nosetests

Licensing terms and authorship
------------------------------

See 'COPYING' and 'AUTHORS' files.

The audio file used in the tests was downloaded from
[Wikimedia Commons](http://en.wikipedia.org/wiki/File:Tim_Berners-Lee_-_Today_-_9_July_2008.flac),
and was originally extracted from the 9 July 2008 
episode of the BBC [Today programme](http://www.bbc.co.uk/programmes/b00cddwc).
