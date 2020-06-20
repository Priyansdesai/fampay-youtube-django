from django.shortcuts import render
from apiclient.discovery import build 
from django.http import HttpResponse
from .models import VideoData

# Arguments that need to passed to the build function 
#DEVELOPER_KEY = "" 
#YOUTUBE_API_SERVICE_NAME = "youtube"
#YOUTUBE_API_VERSION = "v3"
   
# creating Youtube Resource Object 
#youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        #developerKey = DEVELOPER_KEY) 
   
def youtube_search_keyword(query, max_results): 
       
    # calling the search.list method to 
    # retrieve youtube search results 
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
                                               maxResults = max_results, relevanceLanguage='en').execute()
    # extracting the results from search response 
    results = search_keyword.get("items", [])  
    # empty list to store video,  
    # channel, playlist metadata 
    videos = [] 
    playlists = [] 
    channels = [] 
       
    # extracting required info from each result object 
    for result in results: 
        # video result object 
        if result['id']['kind'] == "youtube#video": 
            videos.append([result["snippet"]["title"], 
                            result["id"]["videoId"], result['snippet']['description'], 
                            result['snippet']['thumbnails']['default']['url']]) 
  
        # playlist result object
    return videos

# Create your views here.

def index(request):
    #received = youtube_search_keyword('Cricket', 10)
    """for result in received:
        new_obj = VideoData(1, result[0], result[2], result[3], result[1])
        if new_obj not in list(VideoData.objects.all()):
            new_obj.save()"""
    for a in VideoData.objects.all():
        print(a.name())
    return render(request, 'index.html', {"videos":"HELLO"})