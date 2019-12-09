import unittest

import self as self
from spellchecker import SpellChecker
dir(SpellChecker)
spell = SpellChecker()


def checkWord(word,wordAfterCorrect):
    """
    param word: word from the user
    param wordAfterCorrect: word from the user after spell check
    return: true if the words match else false
   """
    if len(word)<=len(wordAfterCorrect):
        for i in range(len(word)):
            if word[i]!=wordAfterCorrect[i]:
                return False
    if len(word) > len(wordAfterCorrect):
            for i in range(len(wordAfterCorrect)):
                if word[i] != wordAfterCorrect[i]:
                 return False
    return True



class testSpellCheck(unittest.TestCase):
    def test_checkWord(self):
        word="example"
        word2=spell.correction(word) #example
        self.assertTrue(checkWord(word,word2)) #true

        wrong="exemple"
        fixed=spell.correction(wrong)#example
        self.assertFalse(checkWord(wrong,fixed))#false

unittest.main()
