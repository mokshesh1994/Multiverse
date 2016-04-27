
#need import doc_class_rw   the 'as story_doc' isn't needed, but shortens things
from doc_class_rw import story_document
from pprint import pprint
from collections import Counter
from decimal import Decimal
import os
import re
import math
import pickle


'''
naive bayes classes

science fiction
fantasy
horror
mystery & suspense
realistic fiction
historical fiction
action & adventure
humor
romance
speculative fiction
thriller
urban
misc fiction
non-fiction

'''

story_info_path = ".\\Data2-names\\pkl_story_info.pkl"
story_text_path = ".\\Data2\\"   #pretty sure story_document.file_path has the full path and we shouldn't need the .\\Data2\\ part

'''

classifications = {}
    classifications will contain the classes listed under naive bayes classes
        each class will contain a dictionary of documents #use sub_id as key?
            each document will contain a dictionary of terms
                each term will have a term count for that document

    
'''

story = story_document() #should be new instance of story_document class
#If you want to view all variables/fields in story, use pprint(vars(story)), it will tell you what
    #each variable is and its value

pickle_file = open(story_info_path, 'rb') #'rb' is needed, stands for read bytes vs. read since the file information is binary stored
story_list = []

while 1:
    try:
        story = pickle.load(pickle_file)    #should get the info associated to a story
        story_list.append(story)            #putting that info in a list so we can manipulate it
    except (EOFError, pickle.UnpicklingError):     #dealing with end of file
        break
pickle_file.close()

classification = {}

print len(story_list)

num_train_files = 100

for i in range(100):

# regex (?:\[\[\'\w+\'\]\])*\s(\w+(\s | .)?\s?\w*) grab capture group 1
    tags = story_list[i].tags
    genre = re.search(r"\s(\w+\-*\w*(\s | .)?\s?\w*)", tags).group()[1:] #look into fixing , case where there is no space in front of genre
    if classification.has_key(genre):
        classification[genre].append(story_list[i])
    else:
        classification[genre] = []
        classification[genre].append(story_list[i])

test_story_lists = []
for i in range(25):
    d = i+100
    test_story_lists.append(story_list[d])
    
cls_term_counts = {}
cls_term_totals = {}
cls_prob = {}

#story_text_file = open(story_list[4].file_path, 'r')
#story_text_list = story_text_file.read().replace('.','').replace('*','').replace('"','').replace('!','')\
#                          .replace(',','').replace('?','').replace(':','').replace(';','').lower().split()
#pprint(vars(story_list[4]))
#print story_text_list

#cls_term_counts['sci fi'] = Counter(story_text_list)
#print cls_term_counts['sci fi']['i']

for cls_elem in classification:
    if not cls_prob.has_key(cls_elem):
        cls_prob[cls_elem] = (len(classification[cls_elem])/float(num_train_files))
        #print cls_prob
    if not cls_term_counts.has_key(cls_elem):
        cls_term_counts[cls_elem] = {}
    if not cls_term_totals.has_key(cls_elem):
        cls_term_totals[cls_elem] = 0
    for stry_doc in classification[cls_elem]:
        story_text_file = open(stry_doc.file_path,'r')
        story_text_list = story_text_file.read().replace('.','').replace('*','').replace('"','').replace('!','')\
                          .replace(',','').replace('?','').replace(':','').replace(';','').lower().split()
        story_text_file.close()
        count_dict = Counter(story_text_list)
        cls_term_totals[cls_elem] += len(story_text_list)
        for term in count_dict:
            if cls_term_counts[cls_elem].has_key(term):
                cls_term_counts[cls_elem][term] += count_dict[term]
            else:
                cls_term_counts[cls_elem][term] = count_dict[term]

#print cls_term_totals
#print cls_prob
x = 0
for elm in cls_term_totals:
    x += cls_term_totals[elm]
print x
weird_x = x


##This is where we classify unknown documents, or known documents to evalutate our classifier.
##Should loop it over some data set we want to classify.
for elem in test_story_lists:
    
    #test_text_path = ".\\Data\\hfy_4ag99n.txt"
    test_file_list = []
    tags2 = elem.tags
    genre = re.search(r"\s(\w+\-*\w*(\s | .)?\s?\w*)", tags2).group()[1:]
    test_text_file = open(elem.file_path, 'r')
    test_text_list = test_text_file.read().replace('.','').replace('*','').replace('"','').replace('!','')\
                              .replace(',','').replace('?','').replace(':','').replace(';','').lower().split()
    test_text_file.close()
    count_dict = Counter(test_text_list)
    #print count_dict
    max_prob = -999999.0
    prob = Decimal(1.0)
    max_class = ''
    stuff = []

    for cls_elem in cls_term_counts:
        for term in test_text_list:
            if cls_term_counts[cls_elem].has_key(term):
                #prob_dbg = prob
                prob = (Decimal(prob)+ (Decimal(cls_term_counts[cls_elem][term]).ln()) - (Decimal(cls_term_totals[cls_elem]).ln()))
                if prob == 0.0:                     #don't worry about this stuff -v
                    print 'error dict:'
                    print cls_term_counts[cls_elem][term]
                    print cls_term_totals[cls_elem]
                    #print math.log10(prob_dbg)
                    print ''
                    break                           #-------------------------------
                
            else:
                #weird_x += count_dict[term]
                weird_x += 1
                #prob_dbg = prob
                #prob = (Decimal(prob) * (Decimal(count_dict[term]))/Decimal(weird_x))
                prob = (Decimal(prob) + (Decimal(1.0)) - Decimal(weird_x).ln())
                if prob == 0.0:                 #don't worry about this stuff -v
                    print 'error corpus:'
                    print count_dict[term]
                    print weird_x
                    #print math.log10(prob_dbg)
                    print ''
                    break                       #------------------------------
                #print prob
        prob = Decimal(prob) + Decimal(cls_prob[cls_elem]).ln()
        print Decimal(prob)
        if( prob > max_prob ):
            max_class = str(cls_elem)
            max_prob = prob
        weird_x = x
        stuff.append((prob, cls_elem))
        prob = 1.0
        
    print ''
    print max_prob
    print max_class
    print elem.title
    print genre
    print '\n--------------------------\n'
    #print stuff
'''
Now story_info should contain all the info for all retrieved stories

Next step would be to populate the dictionary with all the classifications, docs, terms, and term counts

Might have to some fancy stuff to properly get tags, maybe...
Either way we have stuff.... Now here is where I'm not certain how to proceed.
    P_hat( class | doc ) = P_hat( class )* |-|P_hat( term | class )<-for all terms in doc
        P_hat( term | class ) = count of term in class / count of all terms in class


Where/what do we store? We know the genres of subreddit shortstories, so this is mainly for other stories we encounter
                                ^Kinda of our training data/test data stuff

Binary associations? or Multimodal? ie: just one genre per story or maybe the two highest?

'''
