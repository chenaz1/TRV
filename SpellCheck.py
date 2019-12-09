
from tinydb import TinyDB, Query
from spellchecker import SpellChecker
import re
from collections import Counter
#db = TinyDB('db.json')
#db.insert({'int' 1, 'char' 'a'})
#db.insert({'int' 1, 'char' 'b'})
dir(SpellChecker)
spell = SpellChecker()
myPet=dogg #example for a word with wrong spelling
correctWord=spell.correction(myPet) #dogg-dog

def checkWord(word,wordAfterCorrect)
    
    param word word from the user
    param wordAfterCorrect word from the user after spell check
    return true if the words match else false
    
    if len(word)len(wordAfterCorrect)
        for i in range(len(word))
            if word[i]!=wordAfterCorrect[i]
                return False
    if len(word)  len(wordAfterCorrect)
            for i in range(len(wordAfterCorrect))
                if word[i] != wordAfterCorrect[i]
                 return False
    return True

#answerExist=checkAnswer(correctWord)    #checkAnswer checking if correctWord is exist in the database


