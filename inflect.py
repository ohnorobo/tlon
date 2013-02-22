#!/usr/bin/python


alterations =
   {"k'" : ["p'", "ʃ'", "k'", ""],
    "q'" : ["t'", "ʃ'", "q'", ""],
    "k" :  ["p" , "ʃ" , "k" , ""],
    "g" :  ["b" , "ʒ" , "g" , ""],
    "q" :  ["t" , "ç" , "q" , ""],
    "G" :  ["d" , "ʝ" , "G" , ""],
    "x" :  ["f" , "tɬ", "x" , ""],
    "ɣ" :  ["f" , "dɮ", "ɣ" , ""],
    "χ" :  ["s" , "tʃ", "χ" , ""],
    "ʁ" :  ["z" , "dʒ", "ʁ" , ""],
    "ɴ" :  ["m" , "ɲ" , "ɴ" , ""],
    "ʀ" :  ["ɬ" , "j" , "ʀ" , ""],
    }

sinfixes =
   {"noun" : [1, 2, 3, 4, 3, 1],
    "verb" : [2, 4, 3, 2, 3, 1]
    }


#given a surface form print the root form
#hmmm, dificult w/ deletion, is this even possible?
def surface_to_root(surface):
    root = []

    for char in surface:
        root += getroot(char)

    print root


#given a root form print all the known surface forms
def root_to_surface(root):
    surface_forms = {}

    for sinfix_name in sinfixes:
        surface_forms[sinfix] = inflect(root, sinfixes[sinfix_name])

    print surface_forms


#given a root and a sinfix return the inflected word
def inflect(root, sinfix):
    inflected = []

    for i in range(6):
        inflected += getsurface(root[i], sinfix[i])


#given a character get its root form
def getroot(char):
    for rootform in alterations.keyset():
        if alterations[rootform].contains(char):
            return rootform
    #if there is no root form don't change
    return char


#given a root character and a number get its surface form in that column
def getsurface(char, n):
    for rootform in alterations.keyset():
        if rootform == char:
            return alterations[rootform][n]
    return char


##############
#Main

#args are
word = argv[1]
root_to_surface(word)

