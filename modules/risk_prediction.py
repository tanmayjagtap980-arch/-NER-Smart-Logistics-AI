def calculate_risk(rainfall, flood, landslide):

    rainfall_score = min(rainfall / 3, 100)

    score = (
        rainfall_score * 0.30
        + flood * 0.35
        + landslide * 0.35
    )

    score = round(score, 2)

    if score < 30:
        level = "LOW"
        recommendation = "Route conditions appear relatively safe."

    elif score < 60:
        level = "MEDIUM"
        recommendation = "Monitor weather and road conditions."

    else:
        level = "HIGH"
        recommendation = (
            "Consider an alternative route and "
            "monitor disaster alerts."
        )

    return {
        "score": score,
        "level": level,
        "recommendation": recommendation
    }


def weather_risk(rainfall):

    if rainfall >= 20:
        return {
            "level": "HIGH",
            "color": "red",
            "message": "Heavy rainfall detected."
        }

    elif rainfall >= 5:
        return {
            "level": "MEDIUM",
            "color": "orange",
            "message": "Moderate rainfall detected."
        }

    else:
        return {
            "level": "LOW",
            "color": "green",
            "message": "Low rainfall conditions."
        }