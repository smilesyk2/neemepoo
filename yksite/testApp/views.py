from django.shortcuts import render, render_to_response
import urllib2
import time
import datetime
import json

# Create your views here.
def home(request):
    return render_to_response('index.html')

def search(request):
    # Set the request authentication headers
    # timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
    
    # Send the GET request
    url = 'http://52.68.159.245:7800/search/search_json.jsp'      
    req = urllib2.Request(url)
    
    # Read the response
    resp = urllib2.urlopen(req).read()
    
    print resp['SearchQueryResult']['Collection']['DocumentSet']
    
    return render_to_response('main.html', {"resultObj": json.loads(resp)})