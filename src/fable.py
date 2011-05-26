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

from QTKit import NSImage
from QTKit import QTMakeTime
from QTKit import QTMovie
from QTKit import QTTime

TIME_SCALE = 3

dot = QTMakeTime(1, TIME_SCALE)
dash = QTMakeTime(3, TIME_SCALE)
gap_inter = QTMakeTime(1, TIME_SCALE)
gap_letter = QTMakeTime(3, TIME_SCALE)
gap_word = QTMakeTime(7, TIME_SCALE)

black = NSImage.alloc().initByReferencingFile_("black.jpg")
white = NSImage.alloc().initByReferencingFile_("white.jpg")

def morse_dot(movie):
    movie.addImage_forDuration_withAttributes_(white, dot, {'QTAddImageCodecType': "jpeg"})
    movie.addImage_forDuration_withAttributes_(black, gap_inter, {'QTAddImageCodecType': "jpeg"})

def morse_dash(movie):
    movie.addImage_forDuration_withAttributes_(white, dash, {'QTAddImageCodecType': "jpeg"})
    movie.addImage_forDuration_withAttributes_(black, gap_inter, {'QTAddImageCodecType': "jpeg"})

def main():
    movie, error = QTMovie.alloc().initToWritableFile_error_("../fable.mov", None)
    movie.addImage_forDuration_withAttributes_(black, gap_word, {'QTAddImageCodecType': "jpeg"})

    morse_dot(movie)
    morse_dash(movie)
    morse_dot(movie)

    movie.updateMovieFile()

if __name__ == "__main__":
    main()
