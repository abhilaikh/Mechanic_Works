# main.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

# Load environment variables from .env file
load_dotenv()

# Create a FastAPI application instance
app = FastAPI()

# Point to our templates directory. Jinja2Templates helps us render HTML files.
templates = Jinja2Templates(directory="templates")

# Load the YouTube API key from environment variables
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Build a service object for interacting with the YouTube API.
# This object is what we use to make requests to YouTube.
youtube_service = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# This is the main route that serves our search page.
# The `get` method handles requests to the root URL ("/").
@app.get("/", response_class=HTMLResponse)
async def get_search_form(request: Request):
    """
    Renders the search form page.
    """
    return templates.TemplateResponse("search.html", {"request": request})

# This is the route that handles the search query submitted from the form.
# The `post` method handles the form submission.
@app.post("/search-youtube", response_class=HTMLResponse)
async def search_videos(request: Request, query: str = Form(...)):
    """
    Searches for YouTube videos based on the user's query and displays the results.
    """
    if not query:
        # If the search query is empty, render the page again with an error message.
        return templates.TemplateResponse(
            "search.html",
            {"request": request, "error": "Query cannot be empty."}
        )
    
    try:
        # Use the YouTube service to make a search request.
        # We specify the search query, what information we want ("snippet"),
        # the type of content ("video"), and the number of results ("maxResults").
        request_api = youtube_service.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=10
        )
        response = request_api.execute()

        videos = []
        for item in response.get('items', []):
            videos.append({
                "title": item['snippet']['title'],
                "video_id": item['id']['videoId'],
                "thumbnail_url": item['snippet']['thumbnails']['high']['url'],
                "channel_title": item['snippet']['channelTitle'],
                "description": item['snippet']['description']
            })

        # Render the template with the search results, passing them to the HTML file.
        return templates.TemplateResponse(
            "search.html",
            {"request": request, "results": videos, "query": query}
        )
    
    except Exception as e:
        # If an error occurs (e.g., invalid API key), display an error message.
        return templates.TemplateResponse(
            "search.html",
            {"request": request, "error": f"An error occurred: {e}"}
        )