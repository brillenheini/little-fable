'''
Created on May 26, 2011

@author: hokorn
'''


'''
Created on May 26, 2011

@author: hokorn
'''

class MorseCodeCallback(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    
    def onDot(self):
        pass
        
    def onDash(self):
        pass
    
    def onPause(self):
        pass
    
    def onLongPause(self):
        pass


class TextToMorseCode(object):
    '''
    classdocs
    '''
    
    def _space(self):
        self._morseCodeCallback.onLongPause();

    def _A(self):
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDash();
    
    def _B(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDot();
    
    def _C(self):
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDot();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDash();
        self._morseCodeCallback.onPause();
        self._morseCodeCallback.onDot();
    
    def _D(self):
        pass
    
    def _E(self):
        pass
    
    def _F(self):
        pass
    
    def _G(self):
        pass
    
    def _H(self):
        pass
    
    def _I(self):
        pass
    
    def _J(self):
        pass
    
    def _K(self):
        pass
    
    def _L(self):
        pass
    
    def _M(self):
        pass
    
    def _N(self):
        pass
    
    def _O(self):
        pass
    
    def _P(self):
        pass
    
    def _Q(self):
        pass
    
    def _R(self):
        pass
    
    def _S(self):
        pass
    
    def _T(self):
        pass
    
    def _U(self):
        pass
    
    def _V(self):
        pass
    
    def _W(self):
        pass
    
    def _X(self):
        pass
    
    def _Y(self):
        pass
    
    def _Z(self):
        pass
    
    


    def __init__(self, morseCodeCallback):
        '''
        Constructor
        '''
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
                           'Z': self._Z}
        
    def text2morseCode(self, text):
        i = 0
        for c in text.upper():
            morseFunction = self._morseCode[c]()
            i = i + 1
            if (morseFunction != self._space) and (i < len(text)):
                self._morseCodeCallback.onPause()
    
    