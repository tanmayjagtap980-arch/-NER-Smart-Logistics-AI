import requests
import pandas as pd


CITY_COORDINATES = {
    "Guwahati": [91.7362, 26.1445],
    "Shillong": [91.8933, 25.5788],
    "Imphal": [93.9368, 24.8170],
    "Aizawl": [92.7176, 23.7271],
    "Kohima": [94.1086, 25.6751],
    "Agartala": [91.2868, 23.8315],
    "Gangtok": [88.6065, 27.3389],
    "Itanagar": [93.6053, 27.0844]
}


def get_real_route(
    source,
    destination
):

    source_lon, source_lat = CITY_COORDINATES[source]

    destination_lon, destination_lat = CITY_COORDINATES[destination]

    url = (
        "https://router.project-osrm.org/route/v1/driving/"
        f"{source_lon},{source_lat};"
        f"{destination_lon},{destination_lat}"
        "?overview=false"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        route = data["routes"][0]

        distance_km = route["distance"] / 1000

        duration_hours = route["duration"] / 3600

        return {
            "found": True,
            "distance_km": round(
                distance_km,
                2
            ),
            "eta_hours": round(
                duration_hours,
                2
            ),
            "source": source,
            "destination": destination
        }

    except Exception as error:

        return {
            "found": False,
            "message": str(error)
        }


def optimize_route(
    source,
    destination,
    cargo,
    priority
):

    result = get_real_route(
        source,
        destination
    )

    if not result["found"]:

        return result

    if priority == "Critical":

        risk = "Medium"

    elif priority == "High":

        risk = "Medium"

    else:

        risk = "Low"

    result["cargo"] = cargo
    result["priority"] = priority
    result["risk"] = risk

    result["reason"] = (
        "Route calculated using OpenStreetMap/OSRM "
        "road-network routing. Risk classification "
        "is currently based on prototype risk rules."
    )

    return result