# YouTube Browsing History Dashboard

This project is a simple dashboard built with Dash and Plotly that visualizes YouTube browsing history over the last month by categorizing the videos.

## Overview

- **get_youtube_history**: Simulates fetching YouTube watch history data. Replace with real API calls and authentication as needed.
- **classify_history**: Processes the fetched data to group videos by category.
- **Dashboard**: Uses Plotly Express to render a bar chart of the video counts per category.

## Requirements

This project requires the following Python packages:

- dash
- plotly
- pandas
- google-api-python-client (if integrating with the actual YouTube API)

## Setup & Installation

### 1. Create a Virtual Environment (Recommended)

On macOS or Linux, run the following commands in your project directory:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows, use:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install the Required Packages

Install the dependencies using the provided requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Run the dashboard by executing:

```bash
python app.py
```

Then, open your web browser and navigate to the URL provided in the terminal output (typically http://127.0.0.1:8050/).

## Notes

- Replace `YOUR_API_KEY` in `app.py` with your actual YouTube API key or set up proper OAuth2 credentials.
- The current implementation uses simulated data. Update the API integration as needed.
