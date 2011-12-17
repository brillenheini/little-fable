Takt | Kleine Fabel
===================

Create a QuickTime movie with morse code from a text file.

	usage: src/fable.py fable.txt fable.mov

The movie was used to control the
[BIX Media Facade](http://www.museum-joanneum.at/en/kunsthaus/bix-media-facade/projects/taktkleine-fabel) during summer 2011 in Graz.

A video of the BIX Media Facade sending Morse code: [http://youtu.be/QrKcgiC0AH4](http://youtu.be/QrKcgiC0AH4)
The text is Franz Kafka's [A Little Fable](http://de.wikipedia.org/wiki/Kleine_Fabel).
More information on the project: [http://www.zweintopf.net/Main/TaktKleineFabel](http://www.zweintopf.net/Main/TaktKleineFabel)

Idea by [zweintopf.net](http://www.zweintopf.net/).


Implementation
--------------

The movie is created with Apple's QTKit using the PyObjC bridge, so the script
only works on a Mac.


License
-------

The source code of little-fable is licensed under the MIT X11 license.
