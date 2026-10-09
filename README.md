# Hyderabad Navigator Chatbot

An intelligent trip-planning chatbot for Hyderabad built with Python, natural language processing (NLP), and a Random Forest classifier. It interprets user travel preferences, identifies the main trip intent, and generates a day-wise Hyderabad itinerary.

## Features
- NLP-based query understanding
- Random Forest trip intent classification
- Hyderabad-specific place recommendations
- Day-wise travel itinerary generation
- Budget, duration, and interest-aware planning
- Simple CLI chatbot interface

## Project Structure
- `src/hyderabad_navigator.py` - core chatbot logic
- `requirements.txt` - project dependencies
- `README.md` - project overview
- `demo_output.txt` - sample execution result

## Tech Stack
- Python 3.10+
- scikit-learn
- pandas
- NumPy
- Regex-based NLP preprocessing

## Installation
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# or
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Run the Chatbot
```bash
python src/hyderabad_navigator.py
```

## Example Queries
- I want a 2-day heritage and food trip in Hyderabad
- Suggest a family-friendly itinerary with kids
- Plan a budget trip with shopping and evening spots
- I need a 1-day nature and lake tour
- Recommend a weekend trip with nightlife and good restaurants

## Sample Output
See `demo_output.txt` for an example of the chatbot response.

## Project Goal
This project demonstrates how NLP can understand travel intent and how a Random Forest model can assist in recommending personalized city itineraries.
