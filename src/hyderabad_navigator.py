import re
from collections import defaultdict

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer


HYDERABAD_PLACES = {
    "heritage": [
        {"name": "Charminar", "area": "Old City", "time": "Morning", "reason": "Historic monument and bustling bazaar"},
        {"name": "Golconda Fort", "area": "Golconda", "time": "Late Afternoon", "reason": "Fort architecture and sunset views"},
        {"name": "Chowmahalla Palace", "area": "Khilwat", "time": "Morning", "reason": "Royal Nizami architecture"},
        {"name": "Salar Jung Museum", "area": "Afzalgunj", "time": "Late Morning", "reason": "Art, antiques, and cultural collection"},
    ],
    "food": [
        {"name": "Paradise Biryani", "area": "Secunderabad", "time": "Lunch", "reason": "Famous biryani and Hyderabadi cuisine"},
        {"name": "Laad Bazaar", "area": "Charminar", "time": "Evening", "reason": "Traditional snacks and shopping"},
        {"name": "Banjara Hills Restaurants", "area": "Banjara Hills", "time": "Dinner", "reason": "Premium dining and multi-cuisine spots"},
        {"name": "Mughal Cuisine", "area": "Old City", "time": "Lunch", "reason": "Authentic Hyderabadi dishes"},
    ],
    "nature": [
        {"name": "Hussain Sagar Lake", "area": "Tank Bund", "time": "Evening", "reason": "Lake walk and city views"},
        {"name": "Nehru Zoological Park", "area": "Bahadurpura", "time": "Morning", "reason": "Wildlife and family-friendly outing"},
        {"name": "Ananthagiri Hills", "area": "Vikarabad", "time": "Morning", "reason": "Hill drive and scenic landscape"},
        {"name": "KBR National Park", "area": "Banjara Hills", "time": "Morning", "reason": "Nature trails and peaceful surroundings"},
    ],
    "shopping": [
        {"name": "Laad Bazaar", "area": "Charminar", "time": "Evening", "reason": "Traditional jewellery and bangles"},
        {"name": "GVK One", "area": "Madhapur", "time": "Evening", "reason": "Mall, brands, and food court"},
        {"name": "Madhapur Market", "area": "Madhapur", "time": "Afternoon", "reason": "Lifestyle shopping and cafés"},
        {"name": "Begum Bazaar", "area": "King Koti", "time": "Morning", "reason": "Wholesale shopping experience"},
    ],
    "family": [
        {"name": "Ramoji Film City", "area": "Anajpur", "time": "Full Day", "reason": "Theme park, film sets, and family fun"},
        {"name": "Nehru Zoological Park", "area": "Bahadurpura", "time": "Morning", "reason": "Kids and family-friendly outing"},
        {"name": "Hussain Sagar Lake", "area": "Tank Bund", "time": "Evening", "reason": "Boating and relaxed family time"},
        {"name": "Snow World", "area": "Madhapur", "time": "Evening", "reason": "Fun indoor activity"},
    ],
    "nightlife": [
        {"name": "Banjara Hills", "area": "Banjara Hills", "time": "Night", "reason": "Clubs, lounges, and rooftop dining"},
        {"name": "Gachibowli", "area": "Gachibowli", "time": "Night", "reason": "Modern nightlife with pubs and cafés"},
        {"name": "Tank Bund", "area": "Tank Bund", "time": "Night", "reason": "Night drive and lakefront ambience"},
        {"name": "Madhapur", "area": "Madhapur", "time": "Night", "reason": "Buzzing pub and dining district"},
    ],
    "adventure": [
        {"name": "Ananthagiri Hills", "area": "Vikarabad", "time": "Morning", "reason": "Trekking and scenic trails"},
        {"name": "Golconda Fort", "area": "Golconda", "time": "Late Afternoon", "reason": "Hiking and historical exploration"},
        {"name": "Hussain Sagar Lake", "area": "Tank Bund", "time": "Evening", "reason": "Boating and active evening"},
        {"name": "KBR National Park", "area": "Banjara Hills", "time": "Morning", "reason": "Nature walk and fitness-friendly spot"},
    ],
    "budget": [
        {"name": "Charminar", "area": "Old City", "time": "Morning", "reason": "Low-cost heritage visit"},
        {"name": "Laad Bazaar", "area": "Charminar", "time": "Evening", "reason": "Affordable shopping and local flavour"},
        {"name": "Hussain Sagar Lake", "area": "Tank Bund", "time": "Evening", "reason": "Budget-friendly leisure spot"},
        {"name": "Paradise Biryani", "area": "Secunderabad", "time": "Lunch", "reason": "Economical and iconic meal"},
    ],
}

INTENT_KEYWORDS = {
    "heritage": ["heritage", "history", "culture", "monument", "palace", "fort", "museum", "ancient"],
    "food": ["food", "biryani", "restaurant", "dining", "tasty", "eat", "cuisine", "lunch", "dinner"],
    "nature": ["nature", "lake", "park", "garden", "scenic", "hills", "green", "outdoor"],
    "shopping": ["shopping", "mall", "market", "buy", "souvenirs", "jewellery", "clothes"],
    "family": ["family", "kids", "children", "with family", "couple", "weekend family"],
    "nightlife": ["nightlife", "party", "pub", "club", "night", "evening", "rooftop"],
    "adventure": ["adventure", "trek", "hike", "trip", "activity", "thrill", "explore"],
    "budget": ["budget", "cheap", "affordable", "low cost", "economical", "limited budget"],
}

LABELS = ["heritage", "food", "nature", "shopping", "family", "nightlife", "adventure", "budget"]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def detect_duration(text):
    if re.search(r"\b(1|one)\s*day\b|\b1d\b", text):
        return 1
    if re.search(r"\b(2|two)\s*day\b|\b2d\b", text):
        return 2
    if re.search(r"\b(3|three)\s*day\b|\b3d\b", text):
        return 3
    if re.search(r"\bweekend\b|\b(2|two)\s*days\b", text):
        return 2
    return 2


def detect_budget(text):
    if any(word in text for word in ["budget", "cheap", "affordable", "low cost", "economical"]):
        return "budget"
    if any(word in text for word in ["luxury", "premium", "high budget", "expensive"]):
        return "premium"
    return "moderate"


def infer_primary_intent(text):
    cleaned = clean_text(text)
    scores = defaultdict(int)
    for label, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in cleaned:
                scores[label] += 2
    if not scores:
        return "heritage"
    return max(scores, key=scores.get)


def prepare_training_data():
    texts = [
        "heritage tour with charminar fort and museum in hyderabad", "heritage",
        "food trip with biryani and restaurants in hyderabad", "food",
        "nature outing with lake park and scenic places in hyderabad", "nature",
        "shopping plan for markets and malls in hyderabad", "shopping",
        "family vacation with kids and fun spots in hyderabad", "family",
        "nightlife in hyderabad with pubs clubs and late night dinner", "nightlife",
        "adventure hiking and trekking in hyderabad hills", "adventure",
        "cheap affordable trip with budget food and sightseeing", "budget",
        "historical and cultural hyderabad trip with monuments", "heritage",
        "best biryani places and food streets in hyderabad", "food",
        "lake view and nature walk in hyderabad", "nature",
        "markets for jewellry and local shopping in hyderabad", "shopping",
        "family-friendly itinerary for kids and elders in hyderabad", "family",
        "rooftop bars and nightlife in hyderabad evening", "nightlife",
        "trekking hill station experience near hyderabad", "adventure",
        "low-cost hyderabad trip with budget hotels and meals", "budget",
        "old city heritage sites and forts in hyderabad", "heritage",
        "taste authentic hyderabad cuisine and dum biryani", "food",
    ]

    dataset = []
    for i in range(0, len(texts), 2):
        dataset.append((texts[i], texts[i + 1]))
    return dataset


def train_model():
    dataset = prepare_training_data()
    X = [text for text, _ in dataset]
    y = [label for _, label in dataset]

    vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words="english")
    X_vec = vectorizer.fit_transform(X)

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_vec, y)
    return model, vectorizer


MODEL, VECTORIZER = train_model()


def find_relevant_places(label, query):
    cleaned = clean_text(query)
    preferred_places = []
    for place in HYDERABAD_PLACES.get(label, []):
        place_text = clean_text(" ".join([place["name"], place["area"], place["reason"]]))
        if any(keyword in cleaned for keyword in ["family", "kids"]) and label == "family":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["nature", "park", "lake"]) and label == "nature":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["food", "biryani", "restaurant", "eat"]) and label == "food":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["heritage", "history", "fort"]) and label == "heritage":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["shopping", "market", "buy"]) and label == "shopping":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["night", "pub", "club"]) and label == "nightlife":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["adventure", "trek", "hike", "activity"]) and label == "adventure":
            preferred_places.append(place)
        elif any(keyword in cleaned for keyword in ["budget", "cheap", "affordable"]) and label == "budget":
            preferred_places.append(place)
        elif label in ["heritage", "food", "nature", "shopping", "family", "nightlife", "adventure", "budget"]:
            preferred_places.append(place)

    if not preferred_places:
        return HYDERABAD_PLACES.get(label, [])[:4]
    return preferred_places[:4]


def build_trip_plan(query):
    text = clean_text(query)
    duration = detect_duration(text)
    budget_level = detect_budget(text)
    predicted_label = MODEL.predict(VECTORIZER.transform([text]))[0]

    intent = infer_primary_intent(text)
    final_intent = predicted_label if predicted_label in LABELS else intent

    places = find_relevant_places(final_intent, text)
    itinerary = []

    if duration == 1:
        itinerary.append(f"Day 1: Explore {places[0]['name']} in {places[0]['area']} in the {places[0]['time']} and then visit {places[1]['name']}.")
        itinerary.append(f"Evening: Spend time at {places[2]['name']} for local dining and relaxation.")
    elif duration == 2:
        itinerary.append(f"Day 1: Start with {places[0]['name']} ({places[0]['time']}), continue to {places[1]['name']}, and finish with {places[2]['name']} in the evening.")
        itinerary.append(f"Day 2: Begin with {places[3]['name']}, then explore a food or shopping stop based on your interest and complete the trip with a relaxed evening route.")
    else:
        itinerary.append(f"Day 1: Historic sightseeing at {places[0]['name']} and {places[1]['name']}.")
        itinerary.append(f"Day 2: Nature and food trail with {places[2]['name']} and {places[3]['name']}.")
        itinerary.append(f"Day 3: Final shopping or family leisure at a local market or entertainment hub.")

    return {
        "predicted_intent": final_intent,
        "duration_days": duration,
        "budget_level": budget_level,
        "places": places,
        "itinerary": itinerary,
    }


def chatbot_response(user_query):
    plan = build_trip_plan(user_query)
    summary = (
        f"Recommended trip style: {plan['predicted_intent'].title()} | Duration: {plan['duration_days']} day(s) | "
        f"Budget: {plan['budget_level'].title()}"
    )

    lines = [
        "Hyderabad Navigator Bot",
        summary,
        "",
        "Top suggestions:",
    ]

    for place in plan["places"]:
        lines.append(f"- {place['name']} ({place['area']}) - {place['reason']}")

    lines.extend(["", "Itinerary:"])
    lines.extend(f"{i+1}. {entry}" for i, entry in enumerate(plan["itinerary"]))

    return "\n".join(lines)


if __name__ == "__main__":
    print("Hyderabad Navigator Chatbot")
    print("Type 'exit' to stop the chatbot.\n")

    while True:
        user_query = input("You: ")
        if user_query.strip().lower() in {"exit", "quit", "bye"}:
            print("Bot: Thank you for using Hyderabad Navigator. Have a great trip!")
            break

        response = chatbot_response(user_query)
        print("\nBot:\n" + response)
        print("\n" + "-" * 60)
