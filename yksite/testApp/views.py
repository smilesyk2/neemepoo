from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
import urllib2
import urllib
import time
import datetime
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



# Create your views here.
def home(request):
    return render_to_response('index.html')

@csrf_exempt
def search(request):
    # Set the request authentication headers
    # timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
    # Send the GET request
    url = 'http://52.68.159.245:7800/search/search_json.jsp'
    
    data = {}
    if request.method == 'POST':
        for key in request.POST:
            data.update({key: request.POST[key]})

        print '@@@ data :::', json.dumps(data)
        
    print url
    req = urllib2.Request(url, urllib.urlencode(data)) if data!='' else urllib2.Request(url)
    # Read the response
    response = urllib2.urlopen(req).read()
    
    result = json.loads(response)
    #resultObj = result['SearchQueryResult']['Collection'][0]['DocumentSet']['Document']
    resultObj = result['SearchQueryResult']
    
    print '[search] resultObj', resultObj
    
    return render_to_response('main.html', {"resultObj": resultObj
                                            , "data" : data })
    
