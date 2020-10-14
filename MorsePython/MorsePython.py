import MorseTree
from MorseTree import *
import string
from string import *

def letterToMorse( letter ) :
    return (morseTree[ord( letter ) - ord( "A" )][3])

letter = input()
print( letterToMorse( letter ) )