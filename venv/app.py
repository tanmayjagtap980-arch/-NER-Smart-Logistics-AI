import streamlit as st
import pandas as pd

from modules.accessibility import calculate_accessibility
from modules.route_optimizer import optimize_route
from database.database import initialize_database
from modules.risk_prediction import calculate_risk
from modules.emergency import emergency_delivery
from modules.map_module import show_map
from utils.auth import (
    login_user,
    register_user
)
from utils.llm_assistant import ask_llm

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="NER Smart Logistics AI",
    page_icon="🚚",
    layout="wide"
)


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------

initialize_database()


# -----------------------------
# SESSION STATE
# -----------------------------

if "user" not in st.session_state:
    st.session_state.user = None


# -----------------------------
# LOGIN / REGISTER
# -----------------------------

if st.session_state.user is None:

    st.title(
        "🚚 NER Smart Logistics AI"
    )

    st.subheader(
        "AI-Based Smart Logistics and Accessibility Intelligence Platform"
    )

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    # LOGIN
    with tab1:

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login_user(
                email,
                password
            )

            if user:

                st.session_state.user = user

                st.success(
                    "Login successful!"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid email or password."
                )

    # REGISTER
    with tab2:

        name = st.text_input(
            "Name"
        )

        new_email = st.text_input(
            "Email",
            key="register_email"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        if st.button("Register"):

            if (
                not name
                or not new_email
                or not new_password
            ):

                st.warning(
                    "Please fill in all fields."
                )

            else:

                success = register_user(
                    name,
                    new_email,
                    new_password
                )

                if success:

                    st.success(
                        "Registration successful. Please login."
                    )

                else:

                    st.error(
                        "Registration failed. Email may already exist."
                    )

    st.stop()


# -----------------------------
# HEADER
# -----------------------------

st.title(
    "🚚 NER Smart Logistics AI"
)

st.markdown(
    """
    ### AI-Based Smart Logistics and Accessibility Intelligence Platform
    **North Eastern Region of India**
    """
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title(
    "Navigation"
)

st.sidebar.success(
    f"Logged in as: {st.session_state.user['name']}"
)

if st.sidebar.button("Logout"):

    st.session_state.user = None

    st.rerun()

st.sidebar.divider()

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "NER Map",
        "Route Optimization",
        "Accessibility Intelligence",
        "Risk Analysis",
        "Emergency Logistics",
        "Delivery Tracking",
        "Demand Prediction",
        "AI Assistant"
    ]
)

# -----------------------------
# DASHBOARD
# -----------------------------

if page == "Dashboard":

    st.header("📊 Logistics Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Active Deliveries",
            "128"
        )

    with col2:
        st.metric(
            "Delayed Deliveries",
            "17"
        )

    with col3:
        st.metric(
            "High Risk Routes",
            "11"
        )

    with col4:
        st.metric(
            "Accessibility",
            "74/100"
        )

    st.divider()

    st.subheader("System Overview")

    st.info(
        """
        The platform uses AI, GIS, route optimization,
        accessibility intelligence and predictive analytics
        to improve logistics across the North Eastern Region.
        """
    )


# -----------------------------
# MAP
# -----------------------------

elif page == "NER Map":

    st.header("🗺️ North Eastern Region Map")

    show_map()


# -----------------------------
# ROUTE OPTIMIZATION
# -----------------------------

elif page == "Route Optimization":

    st.title("🚚 AI Route Optimization")

    cities = [
        "Guwahati",
        "Shillong",
        "Imphal",
        "Aizawl",
        "Kohima",
        "Agartala",
        "Gangtok",
        "Itanagar"
    ]

    col1, col2 = st.columns(2)

    with col1:

        source = st.selectbox(
            "Source",
            cities
        )

    with col2:

        destination = st.selectbox(
            "Destination",
            cities,
            index=2
        )

    cargo = st.selectbox(
        "Cargo",
        [
            "Medical Supplies",
            "Food Supplies",
            "Water",
            "Electronics",
            "General Cargo"
        ]
    )

    priority = st.selectbox(
        "Priority",
        [
            "Normal",
            "High",
            "Critical"
        ]
    )

    if st.button(
        "🚀 Optimize Route"
    ):

        if source == destination:

            st.warning(
                "Source and destination "
                "must be different."
            )

        else:

            with st.spinner(
                "Calculating route..."
            ):

                result = optimize_route(
                    source,
                    destination,
                    cargo,
                    priority
                )

            if result["found"]:

                st.success(
                    "Recommended route calculated!"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Distance",
                        f'{result["distance_km"]} km'
                    )

                with col2:

                    st.metric(
                        "ETA",
                        f'{result["eta_hours"]} hours'
                    )

                with col3:

                    st.metric(
                        "Risk",
                        result["risk"]
                    )

                st.info(
                    result["reason"]
                )

            else:

                st.error(
                    "Unable to calculate route."
                )


# -----------------------------
# ACCESSIBILITY
# -----------------------------

elif page == "Accessibility Intelligence":

    st.title("📍 Accessibility Intelligence")

    st.write(
        "Evaluate logistics accessibility based on "
        "road quality, connectivity, weather and disaster conditions."
    )

    st.subheader("Enter Infrastructure Conditions")

    col1, col2 = st.columns(2)

    with col1:

        road_quality = st.slider(
            "Road Quality",
            min_value=0,
            max_value=100,
            value=70
        )

        connectivity = st.slider(
            "Connectivity",
            min_value=0,
            max_value=100,
            value=70
        )

    with col2:

        weather = st.slider(
            "Weather Condition",
            min_value=0,
            max_value=100,
            value=80
        )

        disaster = st.slider(
            "Disaster Safety",
            min_value=0,
            max_value=100,
            value=70
        )

    if st.button("📊 Calculate Accessibility"):

        result = calculate_accessibility(
            road_quality,
            connectivity,
            weather,
            disaster
        )

        st.subheader("Accessibility Result")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Accessibility Score",
                f'{result["score"]}/100'
            )

        with col2:

            st.metric(
                "Accessibility Level",
                result["level"]
            )

        if result["level"] == "Excellent":

            st.success(
                "Excellent accessibility. "
                "Logistics movement should be relatively easy."
            )

        elif result["level"] == "Good":

            st.success(
                "Good accessibility. "
                "Normal logistics operations are possible."
            )

        elif result["level"] == "Moderate":

            st.warning(
                "Moderate accessibility. "
                "Monitor road and environmental conditions."
            )

        else:

            st.error(
                "Poor accessibility. "
                "Consider alternative routes or logistics plans."
            )

# -----------------------------
# RISK
# -----------------------------

elif page == "Risk Analysis":

    st.title("🌧️ Disaster & Risk Analysis")

    st.write(
        "Analyze logistics risk using rainfall, "
        "flood risk and landslide risk."
    )

    st.subheader("Environmental Conditions")

    col1, col2 = st.columns(2)

    with col1:

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=300.0,
            value=30.0,
            step=1.0
        )

        flood = st.slider(
            "Flood Risk",
            min_value=0,
            max_value=100,
            value=20
        )

    with col2:

        landslide = st.slider(
            "Landslide Risk",
            min_value=0,
            max_value=100,
            value=20
        )

    if st.button("🌧️ Calculate Risk"):

        result = calculate_risk(
            rainfall,
            flood,
            landslide
        )

        st.subheader("Risk Assessment")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Risk Score",
                f'{result["score"]}/100'
            )

        with col2:

            st.metric(
                "Risk Level",
                result["level"]
            )

        st.info(
            result["recommendation"]
        )

        if result["level"] == "LOW":

            st.success(
                "LOW RISK — Route conditions "
                "appear relatively safe."
            )

        elif result["level"] == "MEDIUM":

            st.warning(
                "MEDIUM RISK — Monitor weather "
                "and road conditions."
            )

        else:

            st.error(
                "HIGH RISK — Consider an alternative "
                "route and monitor disaster alerts."
            )

# -----------------------------
# DELIVERY TRACKING
# -----------------------------

elif page == "Delivery Tracking":

    st.header("📦 Delivery Tracking")

    data = pd.DataFrame(
        {
            "Delivery ID": [
                "DEL001",
                "DEL002",
                "DEL003",
                "DEL004"
            ],
            "Destination": [
                "Imphal",
                "Shillong",
                "Aizawl",
                "Kohima"
            ],
            "Cargo": [
                "Medicine",
                "Food",
                "Medical Equipment",
                "Emergency Supplies"
            ],
            "Status": [
                "IN TRANSIT",
                "DELAYED",
                "IN TRANSIT",
                "DELIVERED"
            ]
        }
    )

    st.dataframe(
        data,
        use_container_width=True
    )


# -----------------------------
# DEMAND
# -----------------------------

elif page == "Demand Prediction":

    st.header("📈 Logistics Demand Prediction")

    region = st.selectbox(
        "Select Region",
        [
            "Assam",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Tripura",
            "Sikkim",
            "Arunachal Pradesh"
        ]
    )

    if st.button("Predict Demand"):

        st.success(
            f"Predicted logistics demand for {region}: HIGH"
        )

        st.metric(
            "Expected Demand",
            "78%"
        )


# -----------------------------
# -----------------------------
# AI ASSISTANT
# -----------------------------

elif page == "AI Assistant":

    st.title(
        "🤖 AI Logistics Assistant"
    )

    st.write(
        "Ask the AI about routes, delays, "
        "risk, emergency logistics, "
        "warehouses and accessibility."
    )

    question = st.text_area(
        "Ask your question",
        placeholder=(
            "Example: What should I do if "
            "heavy rainfall is expected on "
            "the Guwahati to Imphal route?"
        ),
        height=120
    )

    if st.button("🤖 Ask AI"):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "AI is thinking..."
            ):

                answer = ask_llm(
                    question
                )

            st.subheader(
                "AI Response"
            )

            st.write(
                answer
            )