# Hyderabad Navigator Chatbot

## Abstract
The Hyderabad Navigator Chatbot is an intelligent trip-planning system designed to recommend customized travel experiences in Hyderabad based on user interests. The system combines natural language processing (NLP) and a Random Forest classifier to detect user intent and generate a personalized itinerary. The design is suitable for major project work in AI, ML, and intelligent systems.

## Problem Statement
Tourists often struggle to decide what places to visit in a city depending on their interests, trip duration, and budget. A static travel guide is too generic. There is a need for an intelligent assistant that can understand natural language input and recommend a trip plan automatically.

## Objectives
1. To design a chatbot capable of understanding trip-related natural language queries.
2. To classify trip intent using Random Forest.
3. To recommend Hyderabad attractions based on user preferences.
4. To generate a day-wise itinerary based on duration and budget.
5. To provide an interactive system for practical demonstration.

## Methodology
### NLP Layer
The system cleans the input query by converting it to lowercase and removing punctuation. Keywords such as heritage, food, shopping, family, nightlife, adventure, and budget are used to detect user intention.

### Machine Learning Layer
A Random Forest classifier is trained on labeled text samples to classify travel intent. This classifier predicts the primary trip style and helps determine recommendation categories.

### Recommendation Engine
Based on the predicted intent, the chatbot selects relevant places around Hyderabad such as Charminar, Golconda Fort, Hussain Sagar Lake, Laad Bazaar, Ramoji Film City, and Paradise Biryani.

### Itinerary Generation
The system computes trip duration and budget, then produces a simple day-wise itinerary. This ensures recommendations are aligned with the travel plan.

## Tools and Technologies
- Python
- scikit-learn
- NumPy
- pandas
- Flask
- HTML/CSS

## Expected Results
The chatbot should respond with:
- recommended trip style
- day-wise itinerary
- budget-aware suggestions
- Hyderabad-specific travel recommendations

## Example Input and Output
Input:
```text
I want a 2-day heritage and food trip in Hyderabad with family
```

Output:
```text
Hyderabad Navigator Bot
Recommended trip style: Heritage | Duration: 2 day(s) | Budget: Moderate

Top suggestions:
- Charminar (Old City) - Historic monument and bustling bazaar
- Golconda Fort (Golconda) - Fort architecture and sunset views
- Chowmahalla Palace (Khilwat) - Royal Nizami architecture
- Paradise Biryani (Secunderabad) - Famous biryani and Hyderabadi cuisine
```

## Conclusion
The Hyderabad Navigator Chatbot demonstrates how artificial intelligence can power a smart, personalized city trip planner. The combination of NLP and Random Forest classification makes the system effective, interactive, and suitable for real-world recommendation tasks.
