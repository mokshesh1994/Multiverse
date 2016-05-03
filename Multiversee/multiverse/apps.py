from __future__ import unicode_literals

from django.apps import AppConfig

import os
from django.conf import settings

#from gensim import models, utils
#from gensim.models.doc2vec import Doc2Vec, TaggedDocument

#d2v_model = None
plk_path = None

class MultiConfig(AppConfig):
    name = 'multiverse'
    def ready(self):
        print "Startup Running"
        #global d2v_model
        #d2v_model = Doc2Vec.load(os.path.join(settings.PROJECT_ROOT, 'd2v_model.d2v'))
        global plk_path
        plk_path = settings.PROJECT_ROOT