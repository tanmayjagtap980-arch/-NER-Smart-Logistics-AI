import streamlit as st
import pandas as pd

# ============================================================
# FRONTEND
# ============================================================

from frontend.style import load_css
from frontend.components import hero, kpi, alert_card

# ============================================================
# MODULES
# ============================================================

from modules.accessibility import calculate_accessibility
from modules.route_optimizer import optimize_route
from modules.risk_prediction import calculate_risk
from modules.map_module import show_map

# ============================================================
# DATABASE
# ============================================================

from database.database import initialize_database
from database.crud import create_emergency

# ============================================================
# AUTHENTICATION
# ============================================================

from utils.auth import login_user, register_user

# ============================================================
# AI
# ============================================================

from utils.llm_assistant import ask_llm


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="NER Smart Logistics AI",
    page_icon="🚚",
    layout="wide"
)

load_css()


# ============================================================
# INITIALIZE DATABASE
# ============================================================

initialize_database()


# ============================================================
# SESSION STATE
# ============================================================

if "user" not in st.session_state:
    st.session_state.user = None

if "ai_question" not in st.session_state:
    st.session_state.ai_question = ""


# ============================================================
# LOGIN / REGISTER
# ============================================================

if st.session_state.user is None:

    st.title("🚚 NER Smart Logistics AI")

    st.subheader(
        "AI-Based Smart Logistics and Accessibility "
        "Intelligence Platform"
    )

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    # ========================================================
    # LOGIN
    # ========================================================

    with tab1:

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            key="login_button"
        ):

            if not email or not password:

                st.warning(
                    "Please enter email and password."
                )

            else:

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

    # ========================================================
    # REGISTER
    # ========================================================

    with tab2:

        name = st.text_input(
            "Name",
            key="register_name"
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

        if st.button(
            "Register",
            key="register_button"
        ):

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
                        "Registration successful. "
                        "Please login."
                    )

                else:

                    st.error(
                        "Registration failed. "
                        "Email may already exist."
                    )

    st.stop()


# ============================================================
# MAIN HEADER
# ============================================================

st.title(
    "🚚 NER Smart Logistics AI"
)

st.markdown(
    """
    ### AI-Based Smart Logistics and Accessibility Intelligence Platform

    **North Eastern Region of India**
    """
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "🚚 NER Smart Logistics"
)

st.sidebar.success(
    f"Logged in as: {st.session_state.user['name']}"
)

if st.sidebar.button(
    "Logout",
    key="logout_button"
):

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
    ],
    key="navigation"
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    hero()

    st.markdown(
        '<div class="section-title">'
        '📊 Logistics Overview'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        kpi(
            "Active Routes",
            "128",
            "Network operational"
        )

    with col2:

        kpi(
            "Risk Alerts",
            "12",
            "Requires monitoring"
        )

    with col3:

        kpi(
            "Emergency Requests",
            "07",
            "Critical priority"
        )

    with col4:

        kpi(
            "Active Deliveries",
            "84",
            "Tracking live"
        )

    st.markdown(
        '<div class="section-title">'
        '⚠️ Live Intelligence'
        '</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([2, 1])

    # ========================================================
    # LEFT
    # ========================================================

    with left:

        st.markdown(
            """
            ### 🗺️ Regional Risk Status
            """,
            unsafe_allow_html=True
        )

        st.info(
            "Weather and route intelligence is being "
            "monitored across the North Eastern Region."
        )

        st.markdown(
            """
            **🟢 LOW RISK**

            Normal logistics conditions detected.
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            **🟠 MEDIUM RISK**

            Some routes require monitoring.
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            **🔴 HIGH RISK**

            Heavy rainfall or disaster conditions "
            "may affect logistics.
            """,
            unsafe_allow_html=True
        )

    # ========================================================
    # RIGHT
    # ========================================================

    with right:

        alert_card(
            "🔴 Heavy Rainfall",
            "Route monitoring required.",
            "HIGH"
        )

        alert_card(
            "🟠 Road Accessibility",
            "Moderate accessibility detected.",
            "MEDIUM"
        )

        alert_card(
            "🟢 Normal Route",
            "No immediate risk detected.",
            "LOW"
        )


# ============================================================
# NER MAP
# ============================================================

elif page == "NER Map":

    hero()

    st.markdown(
        '<div class="section-title">'
        '🗺️ North Eastern Region Intelligence Map'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Live weather and location intelligence "
        "is displayed on the regional map."
    )

    show_map()


# ============================================================
# ROUTE OPTIMIZATION
# ============================================================

elif page == "Route Optimization":

    hero()

    st.markdown(
        '<div class="section-title">'
        '🚚 AI Route Optimization'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Calculate the best road-network route "
        "between major North Eastern cities."
    )

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
            "📍 Source",
            cities,
            key="route_source"
        )

    with col2:

        destination = st.selectbox(
            "📍 Destination",
            cities,
            index=2,
            key="route_destination"
        )

    cargo = st.selectbox(
        "📦 Cargo",
        [
            "Medical Supplies",
            "Food Supplies",
            "Water",
            "Electronics",
            "General Cargo"
        ],
        key="route_cargo"
    )

    priority = st.selectbox(
        "⚡ Priority",
        [
            "Normal",
            "High",
            "Critical"
        ],
        key="route_priority"
    )

    if st.button(
        "🚀 Optimize Route",
        key="optimize_route_button"
    ):

        if source == destination:

            st.warning(
                "Source and destination must be different."
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

                st.write(
                    result.get(
                        "message",
                        "Unknown routing error."
                    )
                )


# ============================================================
# ACCESSIBILITY INTELLIGENCE
# ============================================================

elif page == "Accessibility Intelligence":

    hero()

    st.markdown(
        '<div class="section-title">'
        '📍 Accessibility Intelligence'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Select a highway/corridor to automatically "
        "evaluate logistics accessibility."
    )

    # ========================================================
    # ROAD DATABASE
    # ========================================================

    ROAD_DATABASE = {

        "NH-27: Guwahati ➔ Shillong": {

            "road_quality": 85,
            "connectivity": 90,
            "base_weather": 80,
            "disaster_safety": 85,

            "description":
                "Four-lane national highway corridor "
                "with strong connectivity and infrastructure."
        },

        "NH-08: Shillong ➔ Silchar": {

            "road_quality": 60,
            "connectivity": 65,
            "base_weather": 50,
            "disaster_safety": 55,

            "description":
                "Hilly terrain route prone to landslides "
                "during heavy rainfall."
        },

        "NH-37: Silchar ➔ Imphal": {

            "road_quality": 40,
            "connectivity": 45,
            "base_weather": 40,
            "disaster_safety": 30,

            "description":
                "High-vulnerability mountain corridor "
                "subject to monsoon blockages."
        },

        "NH-29: Dimapur ➔ Kohima": {

            "road_quality": 65,
            "connectivity": 70,
            "base_weather": 60,
            "disaster_safety": 60,

            "description":
                "Active road expansion zone with "
                "frequent slow-moving traffic."
        },

        "NH-54: Silchar ➔ Aizawl": {

            "road_quality": 70,
            "connectivity": 75,
            "base_weather": 70,
            "disaster_safety": 65,

            "description":
                "Stable regional highway linking "
                "Mizoram with Assam."
        },

        "NH-415: Guwahati ➔ Itanagar": {

            "road_quality": 80,
            "connectivity": 80,
            "base_weather": 75,
            "disaster_safety": 75,

            "description":
                "Well-maintained corridor connecting "
                "Assam and Arunachal Pradesh."
        }
    }

    selected_road = st.selectbox(
        "🛣️ Select Highway Corridor",
        options=list(ROAD_DATABASE.keys()),
        index=0,
        key="accessibility_road"
    )

    road_data = ROAD_DATABASE[selected_road]

    st.info(
        f"**Route Profile:** "
        f"{road_data['description']}"
    )

    st.subheader(
        "⚙️ Infrastructure & Condition Parameters"
    )

    with st.expander(
        "Adjust Parameters (Optional)",
        expanded=True
    ):

        col1, col2 = st.columns(2)

        with col1:

            road_quality = st.slider(
                "Road Quality Index",
                min_value=0,
                max_value=100,
                value=road_data["road_quality"],
                key="access_road_quality",
                help=(
                    "Based on road surface quality "
                    "and highway class."
                )
            )

            connectivity = st.slider(
                "Network & Node Connectivity",
                min_value=0,
                max_value=100,
                value=road_data["connectivity"],
                key="access_connectivity",
                help=(
                    "Based on service hubs and "
                    "secondary route options."
                )
            )

        with col2:

            weather = st.slider(
                "Weather Condition Index",
                min_value=0,
                max_value=100,
                value=road_data["base_weather"],
                key="access_weather",
                help=(
                    "Condition index based on weather."
                )
            )

            disaster = st.slider(
                "Disaster Safety Index",
                min_value=0,
                max_value=100,
                value=road_data["disaster_safety"],
                key="access_disaster",
                help=(
                    "Safety score based on flood "
                    "and landslide vulnerability."
                )
            )

    # ========================================================
    # CALCULATE
    # ========================================================

    result = calculate_accessibility(
        road_quality,
        connectivity,
        weather,
        disaster
    )

    st.divider()

    st.subheader(
        "Accessibility Result"
    )

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
            "🟢 Excellent accessibility: "
            "Logistics movement is highly reliable."
        )

    elif result["level"] == "Good":

        st.success(
            "🟢 Good accessibility: "
            "Normal logistics operations can proceed."
        )

    elif result["level"] == "Moderate":

        st.warning(
            "🟡 Moderate accessibility: "
            "Monitor live weather and road conditions."
        )

    else:

        st.error(
            "🔴 Poor accessibility: "
            "Consider dynamic rerouting or delay dispatch."
        )


# ============================================================
# RISK ANALYSIS
# ============================================================

elif page == "Risk Analysis":

    hero()

    st.markdown(
        '<div class="section-title">'
        '🌧️ Disaster & Risk Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Evaluate rainfall, flood and landslide "
        "risk for major logistics corridors."
    )

    ROUTE_RISK_DATABASE = {

        "Guwahati ➔ Shillong (NH-27)": {

            "rainfall": 25.0,
            "flood": 15,
            "landslide": 20,
            "terrain_type": "Low Hilly Corridor",

            "vulnerability_note":
                "Generally stable highway corridor "
                "with modern drainage."
        },

        "Shillong ➔ Silchar (NH-08)": {

            "rainfall": 120.0,
            "flood": 65,
            "landslide": 80,
            "terrain_type": "High Slope Monsoonal Pass",

            "vulnerability_note":
                "High susceptibility to soil saturation "
                "and mudslides during heavy downpours."
        },

        "Silchar ➔ Imphal (NH-37)": {

            "rainfall": 160.0,
            "flood": 80,
            "landslide": 95,
            "terrain_type": "Active Landslide Zone",

            "vulnerability_note":
                "Extreme landslide vulnerability "
                "during monsoons."
        },

        "Dimapur ➔ Kohima (NH-29)": {

            "rainfall": 75.0,
            "flood": 40,
            "landslide": 65,
            "terrain_type": "Geologically Unstable Ridge",

            "vulnerability_note":
                "Prone to rockfalls and sinking road patches."
        },

        "Silchar ➔ Aizawl (NH-54)": {

            "rainfall": 45.0,
            "flood": 30,
            "landslide": 35,
            "terrain_type": "Rolling Mountain Terrain",

            "vulnerability_note":
                "Moderate risk profile under standard "
                "seasonal conditions."
        },

        "Guwahati ➔ Itanagar (NH-415)": {

            "rainfall": 30.0,
            "flood": 20,
            "landslide": 25,
            "terrain_type": "Foothill Highway",

            "vulnerability_note":
                "Low disruption probability under "
                "present weather conditions."
        }
    }

    selected_route = st.selectbox(
        "🛣️ Select Route Corridor for Risk Assessment",
        options=list(ROUTE_RISK_DATABASE.keys()),
        index=0,
        key="risk_route"
    )

    risk_data = ROUTE_RISK_DATABASE[selected_route]

    st.info(
        f"**Terrain Profile:** "
        f"{risk_data['terrain_type']} — "
        f"*{risk_data['vulnerability_note']}*"
    )

    st.subheader(
        "🌐 Environmental Inputs"
    )

    with st.expander(
        "Tweak / Override Inputs",
        expanded=True
    ):

        col1, col2 = st.columns(2)

        with col1:

            rainfall = st.number_input(
                "Live Rainfall Rate (mm)",
                min_value=0.0,
                max_value=300.0,
                value=float(risk_data["rainfall"]),
                step=5.0,
                key="risk_rainfall"
            )

            flood = st.slider(
                "Flood Risk Level",
                min_value=0,
                max_value=100,
                value=int(risk_data["flood"]),
                key="risk_flood"
            )

        with col2:

            landslide = st.slider(
                "Landslide Susceptibility Index",
                min_value=0,
                max_value=100,
                value=int(risk_data["landslide"]),
                key="risk_landslide"
            )

    # ========================================================
    # CALCULATE RISK
    # ========================================================

    result = calculate_risk(
        rainfall,
        flood,
        landslide
    )

    st.divider()

    st.subheader(
        "Risk Assessment Verdict"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Composite Risk Score",
            f'{result["score"]}/100'
        )

    with col2:

        st.metric(
            "Risk Category",
            result["level"]
        )

    if result["level"] == "LOW":

        st.success(
            result["recommendation"]
        )

    elif result["level"] == "MEDIUM":

        st.warning(
            result["recommendation"]
        )

    else:

        st.error(
            result["recommendation"]
        )


# ============================================================
# EMERGENCY LOGISTICS
# ============================================================

elif page == "Emergency Logistics":

    hero()

    st.markdown(
        '<div class="section-title">'
        '🚑 Emergency Logistics Command'
        '</div>',
        unsafe_allow_html=True
    )

    st.error(
        "🚨 Emergency requests are automatically "
        "assigned CRITICAL priority."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        kpi(
            "Emergency Requests",
            "07",
            "Critical"
        )

    with col2:

        kpi(
            "Medical Cargo",
            "04",
            "Priority transport"
        )

    with col3:

        kpi(
            "Response Status",
            "ACTIVE",
            "Monitoring"
        )

    st.markdown(
        '<div class="section-title">'
        '🚑 Create Emergency Request'
        '</div>',
        unsafe_allow_html=True
    )

    hospitals = [
        "GMCH - Guwahati",
        "Civil Hospital - Shillong",
        "JN Hospital - Imphal",
        "Civil Hospital - Aizawl"
    ]

    hospital = st.selectbox(
        "🏥 Select Hospital",
        hospitals,
        key="emergency_hospital"
    )

    cargo = st.selectbox(
        "📦 Emergency Cargo",
        [
            "Blood",
            "Medical Supplies",
            "Medicines",
            "Food",
            "Water"
        ],
        key="emergency_cargo"
    )

    quantity = st.number_input(
        "📊 Quantity",
        min_value=1,
        value=10,
        step=1,
        key="emergency_quantity"
    )

    if st.button(
        "🚑 CREATE CRITICAL REQUEST",
        key="create_emergency_request"
    ):

        try:

            emergency_id = create_emergency(
                hospital,
                cargo,
                quantity
            )

            st.success(
                f"Emergency request "
                f"EMG-{emergency_id} created successfully."
            )

            st.warning(
                "⚠️ Priority: CRITICAL"
            )

            st.info(
                "🚚 Emergency shipment has been "
                "registered in the logistics system."
            )

        except Exception as error:

            st.error(
                "Unable to create emergency request."
            )

            st.exception(error)


# ============================================================
# DELIVERY TRACKING
# ============================================================

elif page == "Delivery Tracking":

    hero()

    st.markdown(
        '<div class="section-title">'
        '📦 Delivery Command Center'
        '</div>',
        unsafe_allow_html=True
    )

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
                "🟢 IN TRANSIT",
                "🔴 DELAYED",
                "🟢 IN TRANSIT",
                "✅ DELIVERED"
            ]
        }
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        kpi(
            "Total Deliveries",
            "04",
            "Tracked"
        )

    with col2:

        kpi(
            "In Transit",
            "02",
            "Live movement"
        )

    with col3:

        kpi(
            "Delayed",
            "01",
            "Needs attention"
        )

    with col4:

        kpi(
            "Delivered",
            "01",
            "Completed"
        )

    st.markdown(
        '<div class="section-title">'
        '🚚 Active Deliveries'
        '</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">'
        '🔎 Track Delivery'
        '</div>',
        unsafe_allow_html=True
    )

    selected_delivery = st.selectbox(
        "Select Delivery",
        [
            "DEL001",
            "DEL002",
            "DEL003",
            "DEL004"
        ],
        key="tracking_delivery"
    )

    if st.button(
        "🔍 Track Delivery",
        key="track_delivery_button"
    ):

        delivery_info = {

            "DEL001": (
                "Medicine",
                "Imphal",
                "IN TRANSIT"
            ),

            "DEL002": (
                "Food",
                "Shillong",
                "DELAYED"
            ),

            "DEL003": (
                "Medical Equipment",
                "Aizawl",
                "IN TRANSIT"
            ),

            "DEL004": (
                "Emergency Supplies",
                "Kohima",
                "DELIVERED"
            )
        }

        cargo_name, destination, status = (
            delivery_info[selected_delivery]
        )

        if status == "DELIVERED":

            st.success(
                f"Delivery {selected_delivery} "
                f"has been delivered."
            )

        elif status == "DELAYED":

            st.error(
                f"Delivery {selected_delivery} "
                f"is currently delayed."
            )

        else:

            st.info(
                f"Delivery {selected_delivery} "
                f"is currently in transit."
            )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Cargo",
                cargo_name
            )

        with col2:

            st.metric(
                "Destination",
                destination
            )

        with col3:

            st.metric(
                "Status",
                status
            )


# ============================================================
# DEMAND PREDICTION
# ============================================================

elif page == "Demand Prediction":

    hero()

    st.markdown(
        '<div class="section-title">'
        '📈 AI Demand Forecasting'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Predict logistics demand across "
        "the North Eastern Region."
    )

    region = st.selectbox(
        "📍 Select Region",
        [
            "Assam",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Tripura",
            "Sikkim",
            "Arunachal Pradesh"
        ],
        key="demand_region"
    )

    col1, col2 = st.columns(2)

    with col1:

        current_demand = st.number_input(
            "Current Demand (%)",
            min_value=0,
            max_value=100,
            value=60,
            key="current_demand"
        )

    with col2:

        growth = st.number_input(
            "Expected Growth (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            key="demand_growth"
        )

    if st.button(
        "🤖 Predict Demand",
        key="predict_demand_button"
    ):

        predicted = (
            current_demand
            * (1 + growth / 100)
        )

        predicted = min(
            round(predicted, 2),
            100
        )

        if predicted >= 80:

            level = "HIGH"
            icon = "🔴"

        elif predicted >= 50:

            level = "MEDIUM"
            icon = "🟠"

        else:

            level = "LOW"
            icon = "🟢"

        st.success(
            f"AI prediction generated for {region}."
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Current Demand",
                f"{current_demand}%"
            )

        with col2:

            st.metric(
                "Predicted Demand",
                f"{predicted}%"
            )

        with col3:

            st.metric(
                "Demand Level",
                f"{icon} {level}"
            )

        st.progress(
            predicted / 100
        )


# ============================================================
# AI ASSISTANT
# ============================================================

elif page == "AI Assistant":

    hero()

    st.markdown(
        '<div class="section-title">'
        '🤖 AI Logistics Copilot'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Ask questions about routes, weather, delays, "
        "accessibility, emergency logistics, "
        "warehouses and demand."
    )

    st.markdown(
        "### 💡 Quick Questions"
    )

    q1, q2, q3 = st.columns(3)

    with q1:

        if st.button(
            "🌧️ Heavy Rainfall",
            key="ai_rain"
        ):

            st.session_state.ai_question = (
                "What should I do if heavy rainfall "
                "is expected on the Guwahati to Imphal route?"
            )

    with q2:

        if st.button(
            "🚚 Route Delay",
            key="ai_delay"
        ):

            st.session_state.ai_question = (
                "How should I handle a delayed "
                "medical delivery?"
            )

    with q3:

        if st.button(
            "🚑 Emergency",
            key="ai_emergency"
        ):

            st.session_state.ai_question = (
                "How should emergency medical cargo "
                "be prioritized?"
            )

    question = st.text_area(
        "Ask your question",
        value=st.session_state.ai_question,
        placeholder=(
            "Example: Which route should I use "
            "during heavy rainfall?"
        ),
        height=130,
        key="ai_input"
    )

    if st.button(
        "🤖 Ask AI",
        key="ask_ai_button"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "🧠 AI is analyzing..."
            ):

                answer = ask_llm(
                    question
                )

            st.markdown(
                "### 🧠 AI Recommendation"
            )

            st.info(
                answer
            )