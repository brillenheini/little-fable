# -*- coding: utf-8 -*-
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

class MorseCodeCallback(object):

    def __init__(self):
        pass
    
    def onDot(self):
        pass
        
    def onDash(self):
        pass
    
    def onPause(self):
        pass
    
    def onLongPause(self):
        pass


class TextToMorseCode(object):
    
    _spaceBefore = True

    def __init__(self, morseCodeCallback):

        self._morseCodeCallback = morseCodeCallback
        self._morseCode = {' ': self._space,
                           '\r': self._space,
                           '\n': self._space,
                           '\t': self._space,
                           'A': self._A, 
                           'B': self._B,
                           'C': self._C,
                           'D': self._D,
                           'E': self._E,
                           'F': self._F,
                           'G': self._G,
                           'H': self._H,
                           'I': self._I,
                           'J': self._J,
                           'K': self._K,
                           'L': self._L,
                           'M': self._M,
                           'N': self._N,
                           'O': self._O,
                           'P': self._P,
                           'Q': self._Q,
                           'R': self._R,
                           'S': self._S,
                           'T': self._T,
                           'U': self._U,
                           'V': self._V,
                           'W': self._W,
                           'X': self._X,
                           'Y': self._Y,
                           'Z': self._Z,
                           '0': self._0,
                           '1': self._1,
                           '2': self._2,
                           '3': self._3,
                           '4': self._4,
                           '5': self._5,
                           '6': self._6,
                           '7': self._7,
                           '8': self._8,
                           '9': self._9,
                           '0': self._0,
                           u'Ä': self._ae,
                           u'Ö': self._oe,
                           u'Ü': self._ue,
                           u'ß': self._sz}
    
    def _space(self):
        if not self._spaceBefore:
            self._morseCodeCallback.onLongPause();
            self._spaceBefore = True

    def _A(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _B(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _C(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _D(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _E(self):
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _F(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _G(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _H(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _I(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _J(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _K(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _L(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _M(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _N(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _O(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _P(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _Q(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
        
    def _R(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _S(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
    
    def _T(self):
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _U(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _V(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _W(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _X(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _Y(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
    
    def _Z(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False

    
    def _1(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
        
    def _2(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False

    def _3(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
        
    def _4(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
        
    def _5(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
        
    def _6(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
        
    def _7(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
        
    def _8(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
        
    def _9(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDot();
        self._spaceBefore = False
        
    def _0(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onDash();
        self._spaceBefore = False
        
    def _ae(self):
        self._A()
        self._morseCodeCallback.onPause()
        self._E()
        
    def _oe(self):
        self._O()
        self._morseCodeCallback.onPause()
        self._E()

    def _ue(self):
        self._U()
        self._morseCodeCallback.onPause()
        self._E()
        
    def _sz(self):
        self._S()
        self._morseCodeCallback.onPause()
        self._Z()
    
        
    def text2morseCode(self, text):
        self._spaceBefore = True
        for c in text.upper():
            if c in self._morseCode:
                morseFunction = self._morseCode[c]
            else:
                morseFunction = self._space
                
            if (not self._spaceBefore) and (morseFunction != self._space):
                self._morseCodeCallback.onPause()
            morseFunction()
    
    