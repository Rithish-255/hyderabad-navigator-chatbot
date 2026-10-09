# Hyderabad Navigator Chatbot

A major project that combines NLP and Machine Learning to build an intelligent travel planner for Hyderabad.

## Project Overview
Hyderabad Navigator Chatbot helps users plan trips by understanding their travel intent and generating city-specific recommendations. It uses:
- NLP-based keyword processing to analyze user queries
- Random Forest classification to predict trip intent
- Hyderabad-focused place recommendations
- Dynamic itinerary generation for city travel

## Objective
To create an AI-powered trip advisor that can:
- detect user interests such as heritage, food, nightlife, shopping, family outings, adventure, and budget travel
- recommend popular Hyderabad attractions
- provide a 1-day, 2-day, or 3-day itinerary
- support both CLI and web-based interactions

## Features
- Real-time travel query understanding
- Random Forest-based route classification
- Hyderabad-specific recommendations
- Budget and duration detection
- Beautiful chatbot UI using Flask
- Output generation for project demos and academic use

## Tech Stack
- Python 3.10+
- Flask
- scikit-learn
- pandas
- NumPy
- HTML/CSS

## Project Structure
```text
hyderabad-navigator-chatbot/
├── app.py
├── README.md
├── requirements.txt
├── demo_output.txt
├── project_report.md
├── src/
│   └── hyderabad_navigator.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the Web App
```bash
python app.py
```
Then open:
```text
http://127.0.0.1:5000/
```

## Run the CLI Mode
```bash
python src/hyderabad_navigator.py
```

## Example Queries
- I want a 2-day heritage and food trip in Hyderabad
- Suggest a family trip with kids and nature spots
- Plan a budget trip with shopping and local food
- I need a weekend trip with nightlife and good restaurants
- Recommend a 1-day historical tour in Hyderabad

## Sample Result
```text
Hyderabad Navigator Bot
Recommended trip style: Heritage | Duration: 2 day(s) | Budget: Moderate

Top suggestions:
- Charminar (Old City) - Historic monument and bustling bazaar
- Golconda Fort (Golconda) - Fort architecture and sunset views
- Chowmahalla Palace (Khilwat) - Royal Nizami architecture
- Paradise Biryani (Secunderabad) - Famous biryani and Hyderabadi cuisine
```

## Academic Relevance
This project demonstrates the use of:
- NLP preprocessing for text classification
- Machine Learning for intent recognition
- Real-life conversational systems
- Smart recommendation systems for tourism

## Author
Rithish-255
