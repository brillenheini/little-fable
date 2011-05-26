#! /usr/bin/env python

# Copyright (C) 2011 Harald Okorn, Stefan Schweizer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Little Fable.


"""

import sys

from QTKit import NSImage
from QTKit import QTAddImageCodecType
from QTKit import QTMakeTime
from QTKit import QTMovie
from QTKit import QTTime

from morse import MorseCodeCallback
from morse import TextToMorseCode

TIME_SCALE = 3

dot = QTMakeTime(1, TIME_SCALE)
dash = QTMakeTime(3, TIME_SCALE)
gap_inter = QTMakeTime(1, TIME_SCALE)
gap_letter = QTMakeTime(3, TIME_SCALE)
gap_word = QTMakeTime(7, TIME_SCALE)

black = NSImage.alloc().initByReferencingFile_("src/black.jpg")
white = NSImage.alloc().initByReferencingFile_("src/white.jpg")

attrs = {QTAddImageCodecType: "jpeg"}

class MorseVideoCallback(MorseCodeCallback):
    def __init__(self, movie):
       self._movie = movie

    def onDot(self):
        self._movie.addImage_forDuration_withAttributes_(white, dot, attrs)
        self._movie.addImage_forDuration_withAttributes_(black, gap_inter, attrs)

    def onDash(self):
        self._movie.addImage_forDuration_withAttributes_(white, dash, attrs)
        self._movie.addImage_forDuration_withAttributes_(black, gap_inter, attrs)

    def onPause(self):
        self._movie.addImage_forDuration_withAttributes_(black, gap_letter, attrs)

    def onLongPause(self):
        self._movie.addImage_forDuration_withAttributes_(black, gap_word, attrs)
        self._movie.updateMovieFile()

def main():
    if len(sys.argv) != 3:
        print "usage: fable.py infile outfile"
        return

    with open(sys.argv[1], "r") as f:
        text = f.read()

    movie, error = QTMovie.alloc().initToWritableFile_error_(sys.argv[2], None)
    movie.addImage_forDuration_withAttributes_(black, gap_word, attrs)

    parser = TextToMorseCode(MorseVideoCallback(movie))
    parser.text2morseCode(text)

    movie.updateMovieFile()

if __name__ == "__main__":
    main()
