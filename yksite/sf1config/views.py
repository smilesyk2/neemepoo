# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from sf1config.forms import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
class SourceConfigWizard( SessionWizardView ):
    def get_template_names ( self ): 
        return [ SOURCE_TEMPLATES [ self . steps . current ]]
    
    def done(self):
        return render_to_response('sf1config/source/complete.html')