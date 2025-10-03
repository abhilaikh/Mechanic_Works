# YouTube Video Search Application

## Description

This is a simple web application built with FastAPI that allows users to search for videos on YouTube. It uses the YouTube Data API to fetch video results based on a user's query and displays them in a user-friendly format.

## Features

-   Search for YouTube videos using keywords.
-   Display video titles, thumbnails, channel names, and descriptions.
-   Link directly to YouTube videos.

## Technologies Used

-   FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
-   Jinja2: A template engine for Python.
-   YouTube Data API: Used to fetch video information from YouTube.

## Project Structure

-   `main.py`: The core FastAPI application logic.
-   `templates/search.html`: The Jinja2 template for the UI.
-   `.env`: File to store environment variables (like the API key). Ignored by Git.
-   `requirements.txt`: A list of Python dependencies for the project.

## Code Explanation

### `main.py` (Python - FastAPI Application)

This file contains the core logic of the application:

-   It sets up a FastAPI application instance.
-   It defines two routes:
    -   `/`: Renders the `search.html` template, displaying the search form.
    -   `/search-youtube`: Handles the form submission, calls the YouTube Data API, and renders the `search.html` template with the search results.
-   It uses the `googleapiclient.discovery` library to interact with the YouTube Data API.  You'll need to set the `YOUTUBE_API_KEY` environment variable with your API key.

### `templates/search.html` (HTML - Jinja2 Template)

This file defines the structure and appearance of the search form and the search results display:

-   It uses HTML to create the basic layout, including the search form, result display, and error message area.
-   It uses Jinja2 templating to dynamically insert data into the HTML:
    -   `{{ query or '' }}`:  Displays the search query in the input field (if it exists).
    -   `{% if error %}`...`{% endif %}`:  Displays an error message if one is passed from the Python code.
    -   `{% for video in results %}`...`{% endfor %}`:  Loops through the `results` list (passed from the Python code) and generates HTML for each video, including the title, thumbnail, channel, and description.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abhilaikh/Mechanic_Works.git
    cd Mechanic_Works/youtube-automation
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:** Install the required packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:** Create a file named `.env` in the project root and add your YouTube API key to it:
    ```bash
    YOUTUBE_API_KEY="YOUR_API_KEY_HERE"
    ```

5.  **Run the Application:** To start the development server, use the following command:
    ```bash
    uvicorn main:app --reload
    ```

6.  **Access the Application:** Open your web browser and navigate to `http://127.0.0.1:8000`.
