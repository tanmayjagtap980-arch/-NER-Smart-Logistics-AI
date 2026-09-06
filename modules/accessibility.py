def calculate_accessibility(road_quality, connectivity, weather, disaster):
    """
    Calculates weighted accessibility score (0 to 100).
    Road Quality: 30%, Connectivity: 20%, Weather: 25%, Disaster Safety: 25%
    """
    score = (road_quality * 0.30) + (connectivity * 0.20) + (weather * 0.25) + (disaster * 0.25)
    score = round(score, 1)

    if score >= 80:
        level = "Excellent"
    elif score >= 65:
        level = "Good"
    elif score >= 50:
        level = "Moderate"
    else:
        level = "Poor"

    return {
        "score": score,
        "level": level
    }