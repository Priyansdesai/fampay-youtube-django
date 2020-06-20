from django.shortcuts import render
from apiclient.discovery import build 
from django.http import HttpResponse
from .models import VideoData
from datetime import datetime
import os


file1 = open("date.txt","r+")  
new_date = file1.read()
if int(new_date) < 10:
    new_date = "0" + new_date
new_date_final = "2015-" + new_date + "-01T00:00:00Z"
file1.close()
file1 = open("date.txt", "w+")
file1.write(str(int(new_date) + 1))
file1.close()

# Arguments that need to passed to the build function 
DEVELOPER_KEY = "" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                      developerKey = DEVELOPER_KEY) 

def youtube_search_keyword(query, max_results): 
       
    # calling the search.list method to 
    # retrieve youtube search results 
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
                                               maxResults = max_results, relevanceLanguage='en', type = 'video', 
                                               order='date', publishedAfter=new_date_final).execute()
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

def index(request):
    received = youtube_search_keyword('Cricket', 2)
    for i in range(len(received)):
        result = received[i]
        new_obj = VideoData(i, result[0], result[2], result[3], result[1])
        if new_obj not in list(VideoData.objects.all()):
            new_obj.save()
    data = []
    for a in VideoData.objects.all():
        new_dict = {}
        new_dict['id'] = a.id
        new_dict['title'] = a.title
        new_dict['description'] = a.description
        new_dict['url'] = a.url
        new_dict['unique_id'] = a.unique_id
        print(a.unique_id)
        data.append(new_dict)
    return render(request, 'index.html', {"data":data})