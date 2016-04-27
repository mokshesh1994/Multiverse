import praw
from doc_class_rw import story_document
from pprint import pprint
import pickle
import os
import re

r = praw.Reddit(user_agent='test_SSC script for class project by /u/zelyanii', client_id='XERBZJpRWiH4Ug',
                client_secret='lQ0_A6JG6-ORnOqtrAf-mPIOlDw',
                username='',
                password='')
#submissions = ['hfy', 'shortscifistories']
submissions = ['shortstories']
#tag_groups = set(['oc','mini','nano','micro','[mini]','[micro]','[nano]'])
tag_groups = set(['[SF]','[FN]','[HR]','[MS]','[RF]','[HF]','[AA]','[HM]','[RO]','[SP]','[TH]','[UR]','[MF]','[NF]'])
##r/shortstories  doesn't use css for link flair, but does have link flair text
short_stories_tags = set(['science fiction','fantasy','horror','mystery & suspense',
                          'realistic fiction','historical fiction','action & adventure',
                          'humor','romance','speculative fiction','thriller','urban',
                          'misc fiction','non-fiction'])
##domain: u'self.shortstories'
if not os.path.exists(".\\Data2\\"):
    os.mkdir(".\\Data2\\")
if not os.path.exists(".\\Data2-names\\"):
    os.mkdir(".\\Data2-names\\")

title_file = "story_info"

temp_story = story_document()
pickle_myfile = open(".\\Data2-names\\"+title_file+".pkl", 'wb')

for submission in submissions:
    request = r.subreddit(submission).new(limit=1000)

    for i in range(request.limit):
        print "ping"
        #i=0
        #while i < 1000:
        sub = next(request)
        flair_text = ''
        if( str(sub.domain.encode('ascii','ignore')) != ('self.'+str(sub.subreddit).lower()) ): #is the story held on the reddit domain? if not skip it.
            continue;
        if( sub.link_flair_text ):
            flair_text = str(sub.link_flair_text.encode('ascii', 'ignore')).lower()
        else:
            sub_title = str(sub.title.encode('ascii', 'ignore'))
            doc = re.match(r"\[[a-zA-Z]+\]?", sub_title)
            if(doc):
                flair_text = str(doc.group()).replace('[','').replace(']','').lower()
            else:
                flair_text = ''
        if( flair_text in short_stories_tags ):
            filename = str(sub.subreddit).lower()+"_"+str(sub.id.encode('ascii', 'ignore'))+".txt"
            
            myfile = open(".\\Data2\\"+filename, 'w')
            #myfile.write(str(sub.title.encode('ascii', 'ignore'))+'\n')
            #myfile.write(str(sub.author)+'\n')
            #myfile.write(str(sub.link_flair_text.encode('ascii', 'ignore')))
            myfile.write(str(sub.selftext.encode('ascii', 'ignore').replace('*',"")))
            myfile.close()

            sub_title = str(sub.title.encode('ascii', 'ignore'))
            doc = re.findall(r"\[[a-zA-Z]+\]?", sub_title)

    #add time story posted
            temp_story.title = str(sub.title.encode('ascii', 'ignore'))
            temp_story.author = str(sub.author)
            temp_story.tags = str(doc)+" "+str(sub.link_flair_text.encode('ascii', 'ignore')).lower()
            temp_story.upvotes = sub.ups
            temp_story.sub_id = str(sub.id.encode('ascii', 'ignore'))
            temp_story.domain = str(sub.domain.encode('ascii', 'ignore'))
            temp_story.sub_reddit = str(sub.subreddit).lower()
            temp_story.archived = sub.archived
            temp_story.over_18 = sub.over_18
            temp_story.file_path = ".\\Data2\\"+temp_story.sub_reddit+'_'+temp_story.sub_id+'.txt'

            pickle.dump(temp_story, pickle_myfile, -1)
pickle_myfile.close()

##            sub_title = str(sub.title.encode('ascii', 'ignore'))
##            doc = re.findall(r"\[[a-zA-Z]+\]?", sub_title)
##            myfile.write(sub_title+'\n')
##            myfile.write(str(sub.author)+'\n')
##            myfile.write(str(doc)+" "+str(sub.link_flair_text.encode('ascii', 'ignore')).lower()+'\n')
##            myfile.write(str(sub.ups)+'\n')
##            myfile.write(str(sub.id.encode('ascii', 'ignore'))+'\n')
##            myfile.write(str(sub.domain.encode('ascii','ignore'))+'\n')
##            myfile.write(str(sub.subreddit).lower()+'\n')
##            myfile.write(str(sub.archived)+'\n')
##            myfile.write(str(sub.over_18)+'\n\n')
##            myfile.close()

    ##    if( flair_text in short_stories_tags ):
##        i += 1
##        print str(sub.title.encode('ascii', 'ignore'))+'\n'
##    #print str(sub.selftext.encode('ascii', 'ignore'))+'\n'
##        print str(sub.link_flair_text.encode('ascii', 'ignore'))
##    #print str(vars(sub))
    
    #    print str(sub.title.encode('ascii', 'ignore'))+'\n'
    #    print str(sub.selftext.encode('ascii', 'ignore'))+'\n'


##    print str(sub.title.encode('ascii', 'ignore'))
##    if( sub.link_flair_text ):
##        print str(sub.link_flair_text.encode('ascii', 'ignore'))
##    else:
##        sub_title = str(sub.title.encode('ascii', 'ignore'))
##        doc = re.match(r"\[[a-zA-Z]+\]", sub_title)
##        if(doc):
##            print str(doc.group()).replace('[','').replace(']','')+" Extracted"
##        else:
##            print "None"
##    print str(sub.author)+'\n'
##    filename = "d"+str(i)+".txt"
##    myfile = open(".\\Data\\"+filename, 'w')
##    myfile.write(str(sub.title.encode('ascii', 'ignore'))+'\n')
##    myfile.write(str(sub.author)+'\n')
##    #myfile.write(str(sub.link_flair_text.encode('ascii', 'ignore')))
##    myfile.write(str(sub.selftext.encode('ascii', 'ignore')))
##    myfile.close()
    
    
#pprint(vars(sub))
#pprint(dir(sub))


