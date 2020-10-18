from MorseTree import *

def letterToRank( letter ) :
    return ord( letter ) - ord( "A" )

def rankToLetter( rank ) :
    return chr( ord( "A" ) + rank )

def letterToMorse( letterToCode ) :
    return (morseTree[letterToRank( letterToCode )][3])

def MorseToLetter( morseToDecode,  posTreeMorse = morseStart, posMorseToDecode = 0 ):
    if (posMorseToDecode >= len( morseToDecode )) :
        return morseTree[posTreeMorse][0]
    if (morseToDecode[posMorseToDecode] == "."):
        return MorseToLetter( morseToDecode, letterToRank( morseTree[posTreeMorse][1] ), posMorseToDecode + 1 )
    elif (morseToDecode[posMorseToDecode] == "-"):
        return MorseToLetter( morseToDecode, letterToRank( morseTree[posTreeMorse][2] ), posMorseToDecode + 1 )
    return " "

for i in range( 26 ):
    print( str(rankToLetter(i)) + ":" +letterToMorse(rankToLetter(i)) +  ":" + MorseToLetter( letterToMorse( rankToLetter( i ) ) ) )