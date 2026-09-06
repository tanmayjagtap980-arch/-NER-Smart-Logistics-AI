import streamlit as st
import folium
from folium.plugins import MiniMap, MeasureControl, Fullscreen
from streamlit_folium import st_folium
from geopy.distance import geodesic

# Predefined key hubs in the North Eastern Region
NER_HUBS = {
    "Guwahati (Assam)": (26.1445, 91.7362),
    "Shillong (Meghalaya)": (25.5788, 91.8933),
    "Silchar (Assam)": (24.8333, 92.7789),
    "Imphal (Manipur)": (24.8170, 93.9368),
    "Kohima (Nagaland)": (25.6751, 94.1086),
    "Dimapur (Nagaland)": (25.9068, 93.7271),
    "Aizawl (Mizoram)": (23.7271, 92.7176),
    "Itanagar (Arunachal Pradesh)": (27.0844, 93.6053),
    "Agartala (Tripura)": (23.8315, 91.2868)
}

# Pre-defined status database for specific routes
ROUTE_STATUS_DB = {
    ("Silchar (Assam)", "Imphal (Manipur)"): {"status": "BLOCKED", "color": "#E53935", "reason": "🔴 Road Blocked due to Major Landslide at Jiribam"},
    ("Imphal (Manipur)", "Silchar (Assam)"): {"status": "BLOCKED", "color": "#E53935", "reason": "🔴 Road Blocked due to Major Landslide at Jiribam"},
    
    ("Shillong (Meghalaya)", "Silchar (Assam)"): {"status": "HAZARD", "color": "#FBC02D", "reason": "🟡 Heavy Rainfall & Flash Flood Risk (Proceed with Caution)"},
    ("Silchar (Assam)", "Shillong (Meghalaya)"): {"status": "HAZARD", "color": "#FBC02D", "reason": "🟡 Heavy Rainfall & Flash Flood Risk (Proceed with Caution)"},
    
    ("Dimapur (Nagaland)", "Kohima (Nagaland)"): {"status": "HAZARD", "color": "#FBC02D", "reason": "🟡 Sinking Roadbed & Active Rockfall Sector"},
    ("Kohima (Nagaland)", "Dimapur (Nagaland)"): {"status": "HAZARD", "color": "#FBC02D", "reason": "🟡 Sinking Roadbed & Active Rockfall Sector"}
}

# Natural Disasters with customized map icons
DISASTER_MARKERS = [
    {
        "location": (24.9500, 93.1000),
        "title": "Major Landslide Blockage",
        "icon": "exclamation-triangle",
        "color": "red",
        "detail": "NH-37 blocked completely. Emergency clearing in progress."
    },
    {
        "location": (25.2000, 91.8000),
        "title": "Heavy Rain & Waterlogging",
        "icon": "cloud",
        "color": "orange",
        "detail": "NH-08 experiencing low visibility and waterlogging."
    },
    {
        "location": (25.7500, 94.0000),
        "title": "Rockfall Zone",
        "icon": "warning",
        "color": "darkred",
        "detail": "NH-29 active rockfall risk near Kohima ridge."
    }
]

def calculate_route_metrics(origin_coords, dest_coords):
    """Calculates distance in KM and estimated driving time."""
    dist_km = geodesic(origin_coords, dest_coords).km
    estimated_hours = dist_km / 40.0
    hours = int(estimated_hours)
    minutes = int((estimated_hours - hours) * 60)
    return round(dist_km, 1), f"{hours}h {minutes}m"

def show_map():
    st.title("🗺️ North Eastern Region Navigation & Hazard Map")
    st.caption("100% Free OpenStreetMap Spatial Intelligence (No API Key Required)")

    # 1. ROUTE NAVIGATION CONTROLS
    col1, col2, col3 = st.columns([1.5, 1.5, 1])

    with col1:
        origin_name = st.selectbox("📍 Origin / Dispatch Hub", list(NER_HUBS.keys()), index=0)
    with col2:
        dest_name = st.selectbox("🏁 Destination Node", list(NER_HUBS.keys()), index=1)
    with col3:
        map_style = st.selectbox(
            "🎨 Map Layer Style", 
            ["Standard Street Map", "Topographic Terrain"]
        )

    origin_coords = NER_HUBS[origin_name]
    dest_coords = NER_HUBS[dest_name]

    # Calculate metrics
    dist_km, est_time = calculate_route_metrics(origin_coords, dest_coords)

    # Determine Route Safety Color (Blue = Safest, Yellow = Calamity/Hazard, Red = Blocked)
    route_key = (origin_name, dest_name)
    route_info = ROUTE_STATUS_DB.get(
        route_key, 
        {"status": "SAFE", "color": "#1E88E5", "reason": "🔵 Safest Route Available: Clear conditions reported."}
    )

    route_color = route_info["color"]
    route_reason = route_info["reason"]

    # Display Route Status Banner
    if route_info["status"] == "BLOCKED":
        st.error(f"**Route Status:** {route_reason} | **Distance:** {dist_km} km | **Est. Time:** {est_time}")
    elif route_info["status"] == "HAZARD":
        st.warning(f"**Route Status:** {route_reason} | **Distance:** {dist_km} km | **Est. Time:** {est_time}")
    else:
        st.success(f"**Route Status:** {route_reason} | **Distance:** {dist_km} km | **Est. Time:** {est_time}")

    # 2. SELECT FREE OPENSOURCE TILES (NO API KEY NEEDED)
    if map_style == "Topographic Terrain":
        tiles_url = "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png"
        attr = "OpenTopoMap"
    else:
        tiles_url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attr = "OpenStreetMap"

    # Midpoint for map centering
    mid_lat = (origin_coords[0] + dest_coords[0]) / 2
    mid_lon = (origin_coords[1] + dest_coords[1]) / 2

    # 3. CREATE FOLIUM MAP ENGINE
    m = folium.Map(
        location=[mid_lat, mid_lon],
        zoom_start=7,
        tiles=tiles_url,
        attr=attr,
        control_scale=True
    )

    # Add Map Widgets
    Fullscreen().add_to(m)
    MeasureControl(position='topright', active_color='red', completed_color='blue').add_to(m)
    MiniMap(toggle_display=True).add_to(m)

    # 4. DRAW ORIGIN & DESTINATION MARKERS
    folium.Marker(
        location=origin_coords,
        popup=f"Origin: {origin_name}",
        tooltip=f"Start: {origin_name}",
        icon=folium.Icon(color="green", icon="play")
    ).add_to(m)

    folium.Marker(
        location=dest_coords,
        popup=f"Destination: {dest_name}",
        tooltip=f"End: {dest_name}",
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

    # 5. DRAW ROUTE POLYLINE (Red = Blocked, Yellow = Hazard, Blue = Safest)
    folium.PolyLine(
        locations=[origin_coords, dest_coords],
        color=route_color,
        weight=6,
        opacity=0.85,
        tooltip=f"Route Status: {route_info['status']} ({dist_km} km)"
    ).add_to(m)

    # 6. DRAW NATURAL DISASTER MARKERS
    for disaster in DISASTER_MARKERS:
        folium.Marker(
            location=disaster["location"],
            popup=f"<b>⚠️ {disaster['title']}</b><br>{disaster['detail']}",
            tooltip=f"Disaster: {disaster['title']}",
            icon=folium.Icon(
                color=disaster["color"],
                icon=disaster["icon"]
            )
        ).add_to(m)

    # 7. RENDER MAP
    st_folium(m, width="100%", height=550)