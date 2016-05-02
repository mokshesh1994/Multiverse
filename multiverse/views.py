from django.shortcuts import render
from django.utils import timezone


from .models import Story
from .models import Sims

import os
import pickle
import dill
import datetime
#from SSRec.apps import d2v_model
from multiverse.apps import plk_path
#from gensim import models, similarities, utils
#from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# Create your views here.
def story_list(request):
    stories = Story.objects.filter(genre='science fiction')
    return render(request, 'multiverse/home.html', {'stories': stories[:25]})

#def similarity(request):
#    global d2v_model
#    sim = d2v_model.most_similar('good')
#    sim2 = []
#    for each in sim:
#        sim2.append(Sims.objects.create(text=each[0]))
#    Sims.objects.all().delete()
 #   return render(request, "SSRec/story_sim_test.html", {'sims': sim2})

#def update_db_from_file(request):
    #Story.objects.all().delete()
#    global plk_path
#    temp_story = nstory_document()
#    plk_file = open(os.path.join(plk_path, 'story_info.dplk'), 'rb')
#    stories=[]
#    while 1:
#        try:
#            temp_story = dill.load(plk_file)    #should get the info associated to a story
#            print temp_story.title
#            
#            stories.append(Story.objects.create(title=temp_story.title,
#                                 author=temp_story.author,
#                                 genre=temp_story.genre,
#                                 upvotes=temp_story.upvotes,
#                                 likes=0,
#                                 domain=temp_story.domain,
#                                 domainID=temp_story.sub_id,
#                                 nsfw=temp_story.over_18,
#                                 archived=temp_story.archived,
#                                 tags=temp_story.tags,
#                                 published_date= datetime.datetime.fromtimestamp(int(temp_story.creation_date)).strftime('%Y-%m-%d %H:%M:%S'),
#                                 text=temp_story.text ))
#        except (EOFError, pickle.UnpicklingError):     #dealing with end of file
#            break
#
#    return render(request, "SSRec/up_db_fm_fl.html", {'stories':stories})

class nstory_document:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.tags = ''
        self.genre = ''
        self.upvotes = ''
        self.sub_id = ''
        self.creation_date = ''
        self.domain = ''
        self.archived = ''
        self.over_18 = ''
        self.emotion_vector = []
        self.text = ''