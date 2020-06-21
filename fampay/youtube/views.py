# Loads all the necessary imports for the views to work
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
    # Retrieves the Videos filtered by other parameters such date and relevance language
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", maxResults = max_results,
    											  relevanceLanguage='en', type = 'video', order='date',
      											  publishedAfter=new_date_final).execute()

    # Receives all the videos through the items of retrieved results. 
    results = search_keyword.get("items", [])  
    # Videos return list initializes
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
	# Initializes the list that will be returned with the data from the database. 
	data = []

	# Opens the file total.txt and loads the next max_results
	file1 = open("total.txt","r+")  
	new_total = file1.read()
	new_total_final = int(new_total)
	file1.close()

	# Writes the next max_results to the total.txt, incremented by one
	file1 = open("total.txt", "w+")
	file1.write(str(int(new_total) + 1))
	file1.close()

	# Receives a list of videos matching to the keyword "Cricket"
	received = youtube_search_keyword('Cricket', new_total_final)

	# Iterates through the results to add the result to the database
	for i in range(len(received)):

		# Video on the ith position in the list of videos 
		result = received[i]

		# Initializes the VideoData object, which is how the videos will be saved in the database 
		new_obj = VideoData(i, result[0], result[2], result[3], result[1], result[4])

		# Due to duplicate videos being retrieved from YouTube search and preventing from creating duplicate objects, it is checked that particular video does not already exist
		if new_obj not in list(VideoData.objects.all()):
			new_obj.save()

	# Prepares the JSON containing all fields to be displayed on the table
	for video in VideoData.objects.all():
		new_dict = {}

		# Identifies every video with a unique number
		new_dict['id'] = video.id

		# Gives the title of the video 
		new_dict['title'] = video.title

		# Gives the description of the video
		new_dict['description'] = video.description

		# Gives the Thumbnail url of the video
		new_dict['url'] = video.url

		# Gives the unique ID given by YouTube
		new_dict['unique_id'] = video.unique_id

		# Gives the published date of the video
		new_dict['published_at'] = video.published_at

		# Appends the JSON to the list containing all data
		data.append(new_dict)

	# Calls the render function to render the data
	return render(request, 'index.html', {"data":data})