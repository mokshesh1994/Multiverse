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

def about_page(request):
    return render(request, 'multiverse/about.html',{})

def contact_page(request):
    return render(request, 'multiverse/contact.html',{})

#def similarity(request):
#    global d2v_model
#    sim = d2v_model.most_similar('good')
#    sim2 = []
#    for each in sim:
#        sim2.append(Sims.objects.create(text=each[0]))
#    Sims.objects.all().delete()
 #   return render(request, "SSRec/story_sim_test.html", {'sims': sim2})

def science_fiction(request):
    stories = Story.objects.filter(genre="science fiction")
    return render(request, 'multiverse/science_fiction.html', {'stories': stories[:30]})

def Horror(request):
    stories = Story.objects.filter(genre="horror")
    return render(request, 'multiverse/horror.html', {'stories': stories[:30]})

def Humor(request):
    stories = Story.objects.filter(genre="misc fiction")
    return render(request, 'multiverse/humor.html', {'stories': stories[:30]})

def mystery_suspence(request):
    stories = Story.objects.filter(genre="thriller")
    return render(request, 'multiverse/mystery_suspence.html', {'stories': stories[:30]})

def action_adventure(request):
    stories = Story.objects.filter(genre="fantasy")
    return render(request, 'multiverse/action_adventure.html', {'stories': stories[:30]})

def historical_fiction(request):
    stories = Story.objects.filter(genre="historical fiction")
    return render(request, 'multiverse/historical_fiction.html', {'stories': stories[:30]})

def non_fiction(request):
    stories = Story.objects.filter(genre="non fiction")
    return render(request, 'multiverse/non_fiction.html', {'stories': stories[:30]})

def realistic_fiction(request):
    stories = Story.objects.filter(genre="realistic fiction")
    return render(request, 'multiverse/realistic_fiction.html', {'stories': stories[:30]})

def Romance(request):
    stories = Story.objects.filter(genre="romance")
    return render(request, 'multiverse/romance.html', {'stories': stories[:30]})

def speculative_fiction(request):
    stories = Story.objects.filter(genre="speculative fiction")
    return render(request, 'multiverse/speculative_fiction.html', {'stories': stories[:30]})

def Thriller(request):
    stories = Story.objects.filter(genre="thriller")
    return render(request, 'multiverse/thriller.html', {'stories': stories[:30]})

def Urban(request):
    stories = Story.objects.filter(genre="fantasy")
    return render(request, 'multiverse/urban.html', {'stories': stories[:30]})

def update_db_from_file(request):
    #Story.objects.all().delete()
    global plk_path
    temp_story = nstory_document()
    plk_file = open(os.path.join(plk_path, 'story_info.dplk'), 'rb')
    stories=[]
    while 1:
        try:
            temp_story = dill.load(plk_file)    #should get the info associated to a story
            print temp_story.title
            
            stories.append(Story.objects.create(title=temp_story.title,
                                 author=temp_story.author,
                                 genre=temp_story.genre,
                                 upvotes=temp_story.upvotes,
                                 likes=0,
                                 domain=temp_story.domain,
                                 domainID=temp_story.sub_id,
                                 nsfw=temp_story.over_18,
                                 archived=temp_story.archived,
                                 tags=temp_story.tags,
                                 published_date= datetime.datetime.fromtimestamp(int(temp_story.creation_date)).strftime('%Y-%m-%d %H:%M:%S'),
                                 text=temp_story.text ))
        except (EOFError, pickle.UnpicklingError):     #dealing with end of file
            break

    return render(request, "multiverse/up_db_fm_fl.html", {'stories':stories})

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