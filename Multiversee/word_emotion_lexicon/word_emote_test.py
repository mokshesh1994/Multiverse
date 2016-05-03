
import sys
import os
import time
import re
import math



#Parses a file with the regex pattern \w+\t\w+\t\d
def parse_emote_file_readin(some_file_path):
    myfile = open(some_file_path)
    liststr = myfile.read().lower()
    myfile.close()
    return re.findall(r"\w+\t\w+\t\d", liststr)

#Parses a file with the regex pattern [a-zA-Z]{3,}
def parse_file_readin(some_file_path):
    myfile = open(some_file_path)
    liststr = myfile.read().lower()
    myfile.close()
    return re.findall(r"[a-zA-Z]{3,}", liststr)

def print_ranked( emote_path, doc_path ):
    emotereg = []
    emotelist = []
    docreg = []
    emoteDict = {}
    docDict = {}

##    anger = 0
##    anticipation = 0
##    disgust = 0
##    fear = 0
##    joy	= 0
##    negative = 0
##    positive = 0
##    sadness = 0
##    surprise = 0
##    trust = 0
    emote_vec = [0,0,0,0,0,0,0,0,0,0]
    emote_word =['anger', 'anticipation', 'disgust', 'fear',
                 'joy','negative','positive', 'sadness', 'surprise', 'trust']
    emotereg = parse_emote_file_readin(emote_path)

    for elem in emotereg:
        emotelist = elem.split('\t')
        if not emoteDict.has_key(emotelist[0]) :
            emoteDict[emotelist[0]] = []
            emoteDict[emotelist[0]].append(int(emotelist[2]))
        else:
            emoteDict[emotelist[0]].append(int(emotelist[2]))

    docreg = parse_file_readin(doc_path)
    not_in_emote = 0
    for elem in docreg:
        if emoteDict.has_key(elem) :
            emote_vec[0]    += emoteDict[elem][0]
            emote_vec[1]    += emoteDict[elem][1]
            emote_vec[2]    += emoteDict[elem][2]
            emote_vec[3]    += emoteDict[elem][3]
            emote_vec[4]    += emoteDict[elem][4]
            emote_vec[5]    += emoteDict[elem][5]
            emote_vec[6]    += emoteDict[elem][6]
            emote_vec[7]    += emoteDict[elem][7]
            emote_vec[8]    += emoteDict[elem][8]
            emote_vec[9]    += emoteDict[elem][9]
        else:
            not_in_emote += 1
            
    return emote_vec


def main():

#https://en.wikipedia.org/wiki/Contrasting_and_categorization_of_emotions

    e_path = "NRC_wordlevel_alphabetized_v0.92.txt"
    d_path = "hfy_4c3y0v.txt"

    cos_vec = []
      
    cos_vec.append(print_ranked(e_path, d_path))

if __name__ == '__main__':
  main()


