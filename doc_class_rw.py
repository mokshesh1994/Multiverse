

#from pprint import pprint
#import os
#import re
#import pickle

class story_document:

    def __init__(self):
        self.title = ''
        self.author = ''
        self.tags = ''
        self.upvotes = ''
        self.sub_id = ''
        self.domain = ''
        self.sub_reddit = ''
        self.archived = ''
        self.over_18 = ''
        self.emotion_vector = []
        self.file_path = ''

##    def __init__(self, other):
##        self.title = other.title
##        self.author = other.author
##        self.tags = other.tags
##        self.upvotes = other.upvotes
##        self.sub_id = other.sub_id
##        self.r_domain = other.r_domain
##        self.sub_reddit = other.sub_reddit
##        self.r_archived = other.r_archived
##        self.r_over_18 = other.r_over_18
##        self.emotion_vector = other.emotion_vector

##
##if not os.path.exists(".\\Data2-names\\"):
##    exit()
##
##temp = story_document()
##temp_list = []
##
##myfile = open(".\\Data2-names\\story_info.txt", 'r')
##mypickled_file = open(".\\Data2-names\\pkl_story_info.pkl", "wb")
##
##
##for line in myfile:
##    if line == '\n' and len(temp_list) < 9:
##        print "temp_list not full, hit new line"+str(temp_list)+'\n'
##        exit()
##    elif len(temp_list) == 9:
##        temp.title = temp_list[0][:-1]
##        temp.author = temp_list[1][:-1]
##        temp.tags = temp_list[2][:-1]
##        temp.upvotes = temp_list[3][:-1]
##        temp.sub_id = temp_list[4][:-1]
##        temp.domain = temp_list[5][:-1]
##        temp.sub_reddit = temp_list[6][:-1]
##        temp.archived = temp_list[7][:-1]
##        temp.over_18 = temp_list[8][:-1]
##        temp.file_path = ".\\Data2\\"+temp.sub_reddit+'_'+temp.sub_id+'.txt'
##        #pprint(vars(temp))
##        #c =raw_input("Enter to continue")
##        pickle.dump(temp, mypickled_file, -1)
##        del temp_list[:]
##    else:
##        temp_list.append(line)
##        
##    
###with open(".\\Data2-names\\story_info.txt", 'r') as myfile
##myfile.close()
##mypickled_file.close()
##
##c =raw_input("Enter to continue")
##
##t2 = story_document()
####pklread = open(".\\Data2-names\\pkl_story_info.pkl", "rb")
####for i in range(5):
####    t2 = pickle.load(pklread)
####    pprint(vars(t2))
####    print '\n'
####pklread.close()
####c =raw_input("Enter to continue")
##pklread = open(".\\Data2-names\\pkl_story_info.pkl", "rb")
##for i in range(5):
##    t2 = pickle.load(pklread)
##    pprint(vars(t2))
##    print '\n'
##pklread.close()
##
##
