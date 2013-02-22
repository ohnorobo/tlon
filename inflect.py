#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pprint


alterations = {
    "k'" : ["", "p'", "ʃ'", "k'", ""],
    "q'" : ["", "t'", "ʃ'", "q'", ""],
    "k" :  ["", "p" , "ʃ" , "k" , ""],
    "g" :  ["", "b" , "ʒ" , "g" , ""],
    "q" :  ["", "t" , "ç" , "q" , ""],
    "G" :  ["", "d" , "ʝ" , "G" , ""],
    "x" :  ["", "f" , "tɬ", "x" , ""],
    "ɣ" :  ["", "f" , "dɮ", "ɣ" , ""],
    "χ" :  ["", "s" , "tʃ", "χ" , ""],
    "ʁ" :  ["", "z" , "dʒ", "ʁ" , ""],
    "ɴ" :  ["", "m" , "ɲ" , "ɴ" , ""],
    "ʀ" :  ["", "ɬ" , "j" , "ʀ" , ""],
    }

sinfixes = {
    "root" : [3, 3, 3, 0, 3, 3, 3],
    "noun" : [1, 2, 3, 0, 4, 3, 1],
    "verb" : [2, 4, 3, 0, 2, 3, 1]
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
        print sinfix_name
        print "    " + inflect(root, sinfixes[sinfix_name])
        #surface_forms[sinfix_name] = inflect(root, sinfixes[sinfix_name])

    #pprint.pprint(surface_forms)
    #print(surface_forms)


#given a root and a sinfix return the inflected word
def inflect(root, sinfix):
    inflected = ""

    for i in range(len(root)):
        inflected += getsurface(root[i], sinfix[i])

    #print inflected
    return inflected
    #return inflected.encode("utf-8")

#given a character get its root form
def getroot(char):
    for rootform in alterations.keys():
        if alterations[rootform].contains(char):
            return rootform
    #if there is no root form don't change
    return char


#given a root character and a number get its surface form in that column
def getsurface(char, n):
    #print "     root: " + char
    for rootform in alterations.keys():
        if rootform == char:

            #print str(n) + " surface: " + alterations[rootform][n]
            return alterations[rootform][n]
    return char


##############
#Main

#args are
#word = sys.argv[1].decode("utf-8")
word = sys.argv[1]
root_to_surface(word)

#usage
#./inflect.py qqqaqqq
#
#returns:
#
#noun
#    tçqaqt
#verb
#    çqaçqt
#root
#    qqqaqqq


