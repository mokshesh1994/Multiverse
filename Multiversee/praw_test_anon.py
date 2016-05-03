import praw
from pprint import pprint
import os
import re

r = praw.Reddit(user_agent='test_SSC script for class project by /u/zelyanii', client_id='XERBZJpRWiH4Ug',
                client_secret='lQ0_A6JG6-ORnOqtrAf-mPIOlDw',
                username='[reddit username]',
                password='[reddit password]')
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
if not os.path.exists(".\\Data\\"):
    os.mkdir(".\\Data\\")

for submission in submissions:
    request = r.subreddit(submission).hot(limit=1)
    print "ping"
    for i in range(request.limit):
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
##        if( flair_text in tag_groups ):
##            filename = str(sub.subreddit).lower()+"_"+str(sub.id.encode('ascii', 'ignore'))+".txt"
##            myfile = open(".\\Data\\"+filename, 'w')
##            myfile.write(str(sub.title.encode('ascii', 'ignore'))+'\n')
##            myfile.write(str(sub.author)+'\n')
##            #myfile.write(str(sub.link_flair_text.encode('ascii', 'ignore')))
##            myfile.write(str(sub.selftext.encode('ascii', 'ignore')))
##            myfile.close()
    
        if( flair_text in short_stories_tags ):
            print str(sub.title.encode('ascii', 'ignore'))+'\n'
        #print str(sub.selftext.encode('ascii', 'ignore'))+'\n'
            print str(sub.link_flair_text.encode('ascii', 'ignore'))
        myfile = open("sub_vars.txt", 'w')
        myfile.write(str(vars(sub)))
        myfile.close()
        
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


