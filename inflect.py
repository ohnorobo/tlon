#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pprint
import re


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
    "1noun.def.sg.nom" : [4,3,2,0,2,1,4],
    "1noun.def.sg.acc" : [4,3,1,0,2,1,4],
    "1noun.def.sg.dat" : [4,3,2,0,3,1,4],

    "2noun.indef.sg.nom" : [4,3,2,0,2,2,4],
    "2noun.demon.sg.nom" : [4,2,2,0,2,1,4],
    "2noun.def.dual.nom" : [4,3,3,0,3,3,4],
    "2noun.demon.dual.nom" : [4,2,3,0,3,3,4],
    "2noun.def.pl.nom" : [4,3,3,0,2,3,4],
    "2noun.indef.pl.nom" : [4,3,2,0,2,2,4],
    "2noun.demon.pl.nom" : [4,2,3,0,2,3,4],

    "2noun.indef.sg.acc" : [4,3,1,0,1,2,4],
    "2noun.demon.sg.acc" : [4,2,1,0,2,1,4],
    "2noun.def.dual.acc" : [4,3,2,0,3,3,4],
    "2noun.demon.dual.acc" : [4,2,2,0,3,3,4],
    "2noun.def.pl.acc" : [4,3,2,0,2,3,4],
    "2noun.indef.pl.acc" : [4,3,1,0,1,2,4],
    "2noun.demon.pl.acc" : [4,2,2,0,2,3,4],

    "2noun.indef.sg.dat" : [4,3,1,0,3,2,4],
    "2noun.demon.sg.dat" : [4,3,3,0,3,1,4],
    "2noun.def.dual.dat" : [4,3,1,0,2,3,3],
    "2noun.demon.dual.dat" : [4,2,1,0,3,3,4],
    "2noun.def.pl.dat" : [4,3,2,0,2,3,3],
    "2noun.indef.pl.dat" : [4,3,2,0,3,2,4],
    "2noun.demon.pl.dat" : [4,2,1,0,2,3,4],


    "1verb.perf.indic.1" : [1,4,4,0,1,2,2],
    "1verb.perf.indic.2" : [2,4,4,0,2,1,2],
    "1verb.perf.indic.3" : [1,4,4,0,2,2,1],

    "2verb.perf.cond.1" : [1,4,4,0,1,2,3],
    "2verb.perf.subj.1" : [1,4,4,0,1,3,2],
    "2verb.perf.imper.1" : [1,4,4,0,1,3,3],
    "2verb.imperf.indic.1" : [3,4,4,0,2,2,3],
    "2verb.imperf.cond.1" : [3,4,4,0,1,3,2],
    "2verb.imperf.subj.1" : [3,4,4,0,2,3,1],
    "2verb.imperf.imper.1" : [3,4,4,0,3,3,3],

    "2verb.perf.cond.2" : [2,4,4,0,2,1,3],
    "2verb.perf.subj.2" : [2,4,4,0,2,1,1],
    "2verb.perf.imper.2" : [2,4,4,0,2,3,1],
    "2verb.imperf.indic.2" : [2,4,4,0,1,2,3],
    "2verb.imperf.cond.2" : [2,4,4,0,1,2,2],
    "2verb.imperf.subj.2" : [2,4,4,0,3,1,2],
    "2verb.imperf.imper.2" : [2,4,4,0,3,3,2],

    "2verb.perf.cond.3" : [1,4,4,0,2,1,3],
    "2verb.perf.subj.3" : [1,4,4,0,2,1,1],
    "2verb.perf.imper.3" : [1,4,4,0,2,3,1],
    "2verb.imperf.indic.3" : [3,4,4,0,2,1,3],
    "2verb.imperf.cond.3" : [3,4,4,0,1,1,2],
    "2verb.imperf.subj.3" : [3,4,4,0,2,3,2],
    "2verb.imperf.imper.3" : [3,4,4,0,3,3,3],


    "1adj" : [3,4,1,0,4,2,3]
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

    for sinfix_name in reversed(sorted(sinfixes)):
        print sinfix_name
        print "    " + inflect(root, sinfixes[sinfix_name])
        #surface_forms[sinfix_name] = inflect(root, sinfixes[sinfix_name])

    #pprint.pprint(surface_forms)
    #print(surface_forms)


#given a root and a sinfix return the inflected word
def inflect(root, sinfix):
    inflected = ""

    #print root
    for i in range(7): #7 = CCCVCCC
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

    #split root word into list of consonants (some with ') and vowels
word = re.findall("k'|q'|k|g|q|G|x|ɣ|χ|ʁ|ɴ|ʀ|a|i|u" , sys.argv[1])
root_to_surface(word)



#usage

#./inflect.py qk\'qaqqʁ

#noun
#    tʃ'qaqz
#verb
#    çqaçqz
#root
#    qk'qaqqʁ

