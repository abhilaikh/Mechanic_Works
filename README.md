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

-   `main.py`: Contains the FastAPI application code and API endpoints.
-   `templates/`: Contains the Jinja2 HTML templates for the user interface.
    -   `search.html`: HTML template for the search form and displaying search results.
-   `venv/`: (Virtual Environment) Contains the project's isolated dependencies.

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

1.  **Install Dependencies:** Make sure you have Python installed. Then, install the required packages using pip:
    ```bash
    pip install fastapi uvicorn Jinja2 google-api-python-client
    ```

2.  **Set up environment variables:** Store your YouTube API key in an environment variable named `YOUTUBE_API_KEY`.  You can do this in your terminal before running the app:

    ```bash
    export YOUTUBE_API_KEY="YOUR_API_KEY"  # Linux/macOS
    # or
    set YOUTUBE_API_KEY="YOUR_API_KEY"  # Windows
    ```
    Replace `"YOUR_API_KEY"` with your actual YouTube API key.

3.  **Run the Application:** To start the server, use the following command:
    ```bash
    uvicorn main:app --reload
    ```
    This command starts the FastAPI application using Uvicorn, a production-ready ASGI server. The `--reload` flag enables automatic reloading upon code changes, which is useful during development.

4.  **Access the Application:** Open your web browser and go to `http://127.0.0.1:8000/` to see the search form.

## Folder Architecture

-   **Project Root:** This is the main directory containing all project files.
-   `main.py`: This file contains the FastAPI application code.
-   `templates/`: This directory contains the Jinja2 HTML templates used to render the user interface.
-   `venv/`: This directory (which might be hidden in your file explorer) typically contains the virtual environment for the project.
