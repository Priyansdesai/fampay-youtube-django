from django.shortcuts import render
from apiclient.discovery import build 
from .models import VideoData
from datetime import datetime
from django.conf import settings

# Loads the API version from the settings file 
YOUTUBE_API_VERSION = settings.YOUTUBE_API_VERSION

# Loads the API Service name from the settings file
YOUTUBE_API_SERVICE_NAME = settings.YOUTUBE_API_SERVICE_NAME

# Loads the Developer Key for loading the YouTube API
DEVELOPER_KEY = settings.DEVELOPER_KEY

# Opens the file date.txt to get the state of date. 
file1 = open("date.txt","r+")  
new_date = file1.read()

# For string manipulation purposes, all dates less than 10 are appended with 0 
if int(new_date) < 10:
    new_date = "0" + new_date

# Date is written in the format taken by the YouTube Object
new_date_final = "2018-01-" + new_date + "T00:00:00Z"
file1.close()

# After getting the current date, it is updated to the next day for next reload of the page to use it. 
file1 = open("date.txt", "w+")
file1.write(str(int(new_date) + 1))
file1.close()

# Builds the YouTube object using the YouTube API and Developer Key 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                    developerKey = DEVELOPER_KEY) 

def youtube_search_keyword(query, max_results): 
	"""
		Input: Query (Keyword for the YouTube videos), Max_Results (Max amount of videos to be retrieved in every request)
		Output: Videos satisfying query 
	"""
       
    # Retrieves the Videos filtered by other parameters such date and relevance language, ordered by the publishedDate column
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
                                               maxResults = max_results, relevanceLanguage='en', type = 'video', 
                                               order='date', publishedAfter=new_date_final).execute()
    
    # Receives all the videos through the items of retrieved results. 
    results = search_keyword.get("items", [])  

    # Videos return list initialized
    videos = []

    # Iterating through every result and obtaining required information. 
    for result in results: 

        # Checks if the result object is indeed a YouTube video 
        if result['id']['kind'] == "youtube#video": 

        	# Adds a list of all the required details of every video to the return list of videos
            videos.append([result["snippet"]["title"], 
                            result["id"]["videoId"], result['snippet']['description'], 
                            result['snippet']['thumbnails']['default']['url'], result['snippet']['publishedAt']]) 
  	
  	# Returns the list of videos 
    return videos

def index(request):
	data = []
	file1 = open("total.txt","r+")  
	new_total = file1.read()
	new_total_final = int(new_total)
	file1.close()
	file1 = open("total.txt", "w+")
	file1.write(str(int(new_total) + 1))
	file1.close()
	received = youtube_search_keyword('Cricket', new_total_final)
	for i in range(len(received)):
		result = received[i]
		new_obj = VideoData(i, result[0], result[2], result[3], result[1], result[4])
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
		new_dict['published_at'] = a.published_at
		data.append(new_dict)
	return render(request, 'index.html', {"data":data})