from django.shortcuts import render
from apiclient.discovery import build 
from django.http import HttpResponse

# Arguments that need to passed to the build function 
DEVELOPER_KEY = "AIzaSyDjoVQ-cpwwmAAjmF2Uc7ECxzcgrPPG9pQ" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 
   
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
            videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
                            result["id"]["videoId"], result['snippet']['description'], 
                            result['snippet']['thumbnails']['default']['url'])) 
  
        # playlist result object
    return videos

# Create your views here.

def index(request):
	return render(request, 'index.html', {"videos":youtube_search_keyword('Cricket', 10)})
   