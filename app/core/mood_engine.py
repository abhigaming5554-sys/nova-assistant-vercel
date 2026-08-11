def detect_mood(text: str):
    text = text.lower()

    if any(word in text for word in ["thak gaya", "tired", "thak gya"]):
        return "tired"

    if any(word in text for word in ["bore", "boring", "bore ho raha"]):
        return "bored"

    if any(word in text for word in ["gussa", "frustrated", "problem", "error"]):
        return "frustrated"

    if any(word in text for word in ["coding", "project", "feature", "website"]):
        return "coding"

    return "normal"