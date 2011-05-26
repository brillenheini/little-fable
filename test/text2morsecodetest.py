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

import unittest
import text2morse_code

class MorseCodeTestCallback (text2morse_code.MorseCodeCallback):

    morseText = ""

    def __init__(self):
        '''
        Constructor
        '''
        
    def onDot(self):
        self.morseText += '.'
        
    def onDash(self):
        self.morseText += '-'
    
    def onPause(self):
        self.morseText += ' '
    
    def onLongPause(self):
        self.morseText += '=='


class Test(unittest.TestCase):

    callback = MorseCodeTestCallback()
    generator = text2morse_code.TextToMorseCode(callback)
    
    def setUp(self):
        self.callback.morseText = ""

    def test_a(self):
        self.generator.text2morseCode('a')
        self.assertEqual(".-", self.callback.morseText)
        
    def test_b(self):
        self.generator.text2morseCode('b')
        self.assertEqual("-...", self.callback.morseText)
        
    def test_c(self):
        self.generator.text2morseCode('c')
        self.assertEqual("-.-.", self.callback.morseText)
        
    def test_d(self):
        self.generator.text2morseCode('d')
        self.assertEqual("-..", self.callback.morseText)
        
    def test_e(self):
        self.generator.text2morseCode('e')
        self.assertEqual(".", self.callback.morseText)
        
    def test_f(self):
        self.generator.text2morseCode('f')
        self.assertEqual("..-.", self.callback.morseText)
        
    def test_g(self):
        self.generator.text2morseCode('g')
        self.assertEqual("--.", self.callback.morseText)
        
    def test_h(self):
        self.generator.text2morseCode('h')
        self.assertEqual("....", self.callback.morseText)
        
    def test_i(self):
        self.generator.text2morseCode('i')
        self.assertEqual("..", self.callback.morseText)
        
    def test_j(self):
        self.generator.text2morseCode('j')
        self.assertEqual(".---", self.callback.morseText)
        
    def test_k(self):
        self.generator.text2morseCode('k')
        self.assertEqual("-.-", self.callback.morseText)
    
    def test_l(self):
        self.generator.text2morseCode('l')
        self.assertEqual(".-..", self.callback.morseText)
        
    def test_m(self):
        self.generator.text2morseCode('m')
        self.assertEqual("--", self.callback.morseText)
        
    def test_n(self):
        self.generator.text2morseCode('n')
        self.assertEqual("-.", self.callback.morseText)
        
    def test_o(self):
        self.generator.text2morseCode('o')
        self.assertEqual("---", self.callback.morseText)
        
    def test_p(self):
        self.generator.text2morseCode('p')
        self.assertEqual(".--.", self.callback.morseText)
        
    def test_q(self):
        self.generator.text2morseCode('q')
        self.assertEqual("--.-", self.callback.morseText)
        
    def test_r(self):
        self.generator.text2morseCode('r')
        self.assertEqual(".-.", self.callback.morseText)
        
    def test_s(self):
        self.generator.text2morseCode('s')
        self.assertEqual("...", self.callback.morseText)
        
    def test_t(self):
        self.generator.text2morseCode('t')
        self.assertEqual("-", self.callback.morseText)
        
    def test_u(self):
        self.generator.text2morseCode('u')
        self.assertEqual("..-", self.callback.morseText)
        
    def test_v(self):
        self.generator.text2morseCode('v')
        self.assertEqual("...-", self.callback.morseText)
        
    def test_w(self):
        self.generator.text2morseCode('w')
        self.assertEqual(".--", self.callback.morseText)
        
    def test_x(self):
        self.generator.text2morseCode('x')
        self.assertEqual("-..-", self.callback.morseText)
        
    def test_y(self):
        self.generator.text2morseCode('y')
        self.assertEqual("-.--", self.callback.morseText)
        
    def test_z(self):
        self.generator.text2morseCode('z')
        self.assertEqual("--..", self.callback.morseText)
        
    def test_1(self):
        self.generator.text2morseCode('1')
        self.assertEqual(".----", self.callback.morseText)
        
    def test_2(self):
        self.generator.text2morseCode('2')
        self.assertEqual("..---", self.callback.morseText)
        
    def test_3(self):
        self.generator.text2morseCode('3')
        self.assertEqual("...--", self.callback.morseText)
        
    def test_4(self):
        self.generator.text2morseCode('4')
        self.assertEqual("....-", self.callback.morseText)
        
    def test_5(self):
        self.generator.text2morseCode('5')
        self.assertEqual(".....", self.callback.morseText)
        
    def test_6(self):
        self.generator.text2morseCode('6')
        self.assertEqual("-....", self.callback.morseText)
        
    def test_7(self):
        self.generator.text2morseCode('7')
        self.assertEqual("--...", self.callback.morseText)
        
    def test_8(self):
        self.generator.text2morseCode('8')
        self.assertEqual("---..", self.callback.morseText)
        
    def test_9(self):
        self.generator.text2morseCode('9')
        self.assertEqual("----.", self.callback.morseText)
        
    def test_0(self):
        self.generator.text2morseCode('0')
        self.assertEqual("-----", self.callback.morseText)
        
    def test_ae(self):
        self.generator.text2morseCode(u'ä')
        self.assertEqual(".- .", self.callback.morseText)
        
    def test_oe(self):
        self.generator.text2morseCode(u'ö')
        self.assertEqual("--- .", self.callback.morseText)
        
    def test_ue(self):
        self.generator.text2morseCode(u'ü')
        self.assertEqual("..- .", self.callback.morseText)
        
    def test_sz(self):
        self.generator.text2morseCode(u'ß')
        self.assertEqual('... --..', self.callback.morseText)
        
    def test_space(self):
        self.generator.text2morseCode(u'e e')
        self.assertEqual(".==.", self.callback.morseText)
        
    def test_hello_world(self):
        self.generator.text2morseCode(u'Hello World')
        self.assertEqual(".... . .-.. .-.. ---==.-- --- .-. .-.. -..", self.callback.morseText)
        
    def test_fable(self):
        self.generator.text2morseCode(u'„Ach“, sagte die Maus, „die Welt wird enger mit jedem Tag.')
        self.assertEqual('.- -.-. ....==... .- --. - .==-.. .. .==-- .- ..- ...==-.. .. .==.-- . .-.. -==.-- .. .-. -..==. -. --. . .-.==-- .. -==.--- . -.. . --==- .- --.==', self.callback.morseText)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_a']
    unittest.main()