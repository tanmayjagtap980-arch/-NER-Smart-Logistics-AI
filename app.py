import streamlit as st
import pandas as pd
from frontend.style import load_css
from frontend.components import hero, kpi, alert_card
from frontend.components import hero
from frontend.components import hero
from frontend.style import load_css
from modules.accessibility import calculate_accessibility
from modules.route_optimizer import optimize_route
from database.database import initialize_database
from modules.risk_prediction import calculate_risk
from modules.emergency import create_emergency
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

load_css()


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
# -----------------------------
# DASHBOARD (SIH COMMAND CENTER)
# -----------------------------

import plotly.express as px
import plotly.graph_objects as go

if page == "Dashboard":

    st.title("🛡️ NER Command & Logistics Control Center")
    st.caption("Real-Time Spatial Intelligence & Supply Chain Surveillance Platform | North Eastern Region")

    # 1. LIVE EMERGENCY TICKER
    st.error("🚨 **LIVE CRITICAL ALERT:** Active Landslide on **NH-37 (Silchar ➔ Imphal)**. Rerouting recommended via NH-54. | 🌧️ Heavy rainfall warning in **Meghalaya (Shillong sector)**.")

    st.markdown("---")

    # 2. HIGH-IMPACT KEY PERFORMANCE METRICS (KPIs)
    st.subheader("📊 Key Operational Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="🚚 Active Freight",
            value="142 Units",
            delta="+12 today"
        )

    with col2:
        st.metric(
            label="⏳ Delayed Transit",
            value="14 Units",
            delta="-3 vs yesterday",
            delta_color="inverse"
        )

    with col3:
        st.metric(
            label="🚨 High Risk Routes",
            value="3 Passes",
            delta="2 Blocked",
            delta_color="inverse"
        )

    with col4:
        st.metric(
            label="📍 Avg Accessibility",
            value="78 / 100",
            delta="+4% optimized"
        )

    with col5:
        st.metric(
            label="📦 Medical Cold-Chains",
            value="18 Active",
            delta="100% On-Time"
        )

    st.markdown("---")

    # 3. INTERACTIVE ANALYTICS CHARTS (PLOTLY)
    col_left, col_right = st.columns([1.5, 1])

    with col_left:
        st.subheader("🗺️ State-Wise Logistics Accessibility Index")
        
        # Sample data for NER States
        accessibility_data = {
            "State": ["Assam", "Arunachal", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Sikkim", "Tripura"],
            "Accessibility Score": [88, 62, 45, 58, 64, 52, 70, 82],
            "Status": ["Excellent", "Moderate", "Critical", "Moderate", "Moderate", "Critical", "Good", "Good"]
        }
        
        fig_bar = px.bar(
            accessibility_data,
            x="State",
            y="Accessibility Score",
            color="Accessibility Score",
            color_continuous_scale="RdYlGn",
            text="Accessibility Score",
            title="Current Route Accessibility Ratings per NER State"
        )
        fig_bar.update_layout(height=350, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_right:
        st.subheader("⚠️ Transit Delay Root Causes")
        
        delay_causes = {
            "Cause": ["Landslides", "Heavy Rainfall", "Checkpost Queue", "Road Maintenance", "Vehicle Breakdown"],
            "Incidents": [42, 28, 15, 10, 5]
        }
        
        fig_pie = px.pie(
            delay_causes,
            names="Cause",
            values="Incidents",
            color_discrete_sequence=px.colors.sequential.RdBu,
            hole=0.4,
            title="Primary Logistics Bottlenecks"
        )
        fig_pie.update_layout(height=350, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")

    # 4. EMERGENCY & DISASTER DISPATCH MONITOR
    st.subheader("🚨 Critical Corridor Status & Rapid Actions")
    
    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.markdown("##### **Recent High-Priority Disruption Events**")
        disruption_table = [
            {"Corridor": "NH-37: Silchar ➔ Imphal", "Hazard": "Landslide (Jiribam)", "Impact Level": "🔴 HIGH (Blocked)", "Reroute Plan": "Via Inland Waterway NW-2 + NH-54"},
            {"Corridor": "NH-08: Shillong ➔ Silchar", "Hazard": "Torrential Rainfall", "Impact Level": "🟡 MEDIUM (Slowing)", "Reroute Plan": "Speed Restricted to 30km/h"},
            {"Corridor": "NH-29: Dimapur ➔ Kohima", "Hazard": "Sinking Road Bed", "Impact Level": "🟡 MEDIUM (Single Lane)", "Reroute Plan": "Alternative Bypass Open"},
            {"Corridor": "NH-27: Guwahati ➔ Shillong", "Hazard": "Clear Passage", "Impact Level": "🟢 LOW (Normal)", "Reroute Plan": "Direct Route Active"},
        ]
        st.dataframe(disruption_table, use_container_width=True)

    with col_b:
        st.markdown("##### **Quick Emergency Actions**")
        st.button("⚡ Dispatch Medical Cold-Chain Emergency Drone", use_container_width=True)
        st.button("📡 Broadcast SMS Road Alert to Drivers", use_container_width=True)
        st.button("📑 Generate State Disaster Dept Logistics Report", use_container_width=True)
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
# -----------------------------
# ACCESSIBILITY INTELLIGENCE (AUTOMATED)
# -----------------------------

elif page == "Accessibility Intelligence":

    st.title("📍 Accessibility Intelligence")
    st.write("Select a highway/corridor to automatically evaluate accessibility based on infrastructure and live data.")

    # 1. Pre-configured Road Database (In production, load this from DB/GIS)
    ROAD_DATABASE = {
        "NH-27: Guwahati ➔ Shillong": {
            "road_quality": 85,
            "connectivity": 90,
            "base_weather": 80,
            "disaster_safety": 85,
            "description": "Four-lane national highway corridor with strong connectivity and infrastructure."
        },
        "NH-08: Shillong ➔ Silchar": {
            "road_quality": 60,
            "connectivity": 65,
            "base_weather": 50,
            "disaster_safety": 55,
            "description": "Hilly terrain route prone to landslides during heavy rainfall."
        },
        "NH-37: Silchar ➔ Imphal": {
            "road_quality": 40,
            "connectivity": 45,
            "base_weather": 40,
            "disaster_safety": 30,
            "description": "High-vulnerability mountain corridor subject to monsoon blockages."
        },
        "NH-29: Dimapur ➔ Kohima": {
            "road_quality": 65,
            "connectivity": 70,
            "base_weather": 60,
            "disaster_safety": 60,
            "description": "Active road expansion zone with frequent slow-moving traffic."
        },
        "NH-54: Silchar ➔ Aizawl": {
            "road_quality": 70,
            "connectivity": 75,
            "base_weather": 70,
            "disaster_safety": 65,
            "description": "Stable regional highway linking Mizoram with Assam."
        },
        "NH-415: Guwahati ➔ Itanagar": {
            "road_quality": 80,
            "connectivity": 80,
            "base_weather": 75,
            "disaster_safety": 75,
            "description": "Well-maintained corridor connecting Assam and Arunachal Pradesh."
        }
    }

    # 2. Automated Selection Input
    selected_road = st.selectbox(
        "🛣️ Select Highway Corridor",
        options=list(ROAD_DATABASE.keys()),
        index=0
    )

    # Fetch pre-configured data for selected route
    road_data = ROAD_DATABASE[selected_road]

    st.info(f"**Route Profile:** {road_data['description']}")

    # 3. Parameter Customization (Pre-filled Automatically)
    st.subheader("⚙️ Infrastructure & Condition Parameters (Auto-populated)")

    with st.expander("Adjust Parameters (Optional)", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            road_quality = st.slider(
                "Road Quality Index",
                min_value=0, max_value=100,
                value=road_data["road_quality"],
                help="Automatically loaded based on road surface quality and highway class."
            )

            connectivity = st.slider(
                "Network & Node Connectivity",
                min_value=0, max_value=100,
                value=road_data["connectivity"],
                help="Based on density of service hubs and secondary route options."
            )

        with col2:
            weather = st.slider(
                "Weather Condition Index",
                min_value=0, max_value=100,
                value=road_data["base_weather"],
                help="Automatically calculated based on recent rainfall and visibility metrics."
            )

            disaster = st.slider(
                "Disaster Safety Index",
                min_value=0, max_value=100,
                value=road_data["disaster_safety"],
                help="Dynamic score calculated using landslide and flood risk history."
            )

    # 4. Instant Real-time Calculation (No button click needed)
    result = calculate_accessibility(
        road_quality,
        connectivity,
        weather,
        disaster
    )

    st.divider()

    # 5. Accessibility Result Display
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

    # Status Feedback Boxes
    if result["level"] == "Excellent":
        st.success("🟢 **Excellent accessibility:** Logistics movement is highly reliable and clear for heavy transport.")
    elif result["level"] == "Good":
        st.success("🟢 **Good accessibility:** Normal logistics operations are proceeding smoothly.")
    elif result["level"] == "Moderate":
        st.warning("🟡 **Moderate accessibility:** Caution advised. Monitor live weather alerts and road notices.")
    else:
        st.error("🔴 **Poor accessibility:** High disruption risk. Consider dynamic rerouting or delay dispatch.")

# -----------------------------
# -----------------------------
# DISASTER & RISK ANALYSIS (AUTOMATED)
# -----------------------------

elif page == "Risk Analysis":

    st.title("🌧️ Disaster & Risk Analysis")
    st.write("Select a region or route corridor to automatically fetch real-time weather risk metrics and landslide vulnerability.")

    # 1. Real-time / Historic Risk Profile Database per Route
    ROUTE_RISK_DATABASE = {
        "Guwahati ➔ Shillong (NH-27)": {
            "rainfall": 25.0,
            "flood": 15,
            "landslide": 20,
            "terrain_type": "Low Hilly Corridor",
            "vulnerability_note": "Generally stable highway corridor with modern drainage."
        },
        "Shillong ➔ Silchar (NH-08)": {
            "rainfall": 120.0,
            "flood": 65,
            "landslide": 80,
            "terrain_type": "High Slope Monsoonal Pass",
            "vulnerability_note": "High susceptibility to soil saturation and mudslides during heavy downpours."
        },
        "Silchar ➔ Imphal (NH-37)": {
            "rainfall": 160.0,
            "flood": 80,
            "landslide": 95,
            "terrain_type": "Active Landslide Zone",
            "vulnerability_note": "Extreme landslide vulnerability near Jiribam sector during monsoons."
        },
        "Dimapur ➔ Kohima (NH-29)": {
            "rainfall": 75.0,
            "flood": 40,
            "landslide": 65,
            "terrain_type": "Geologically Unstable Ridge",
            "vulnerability_note": "Prone to rockfalls and sinking road patches."
        },
        "Silchar ➔ Aizawl (NH-54)": {
            "rainfall": 45.0,
            "flood": 30,
            "landslide": 35,
            "terrain_type": "Rolling Mountain Terrain",
            "vulnerability_note": "Moderate risk profile under standard seasonal conditions."
        },
        "Guwahati ➔ Itanagar (NH-415)": {
            "rainfall": 30.0,
            "flood": 20,
            "landslide": 25,
            "terrain_type": "Foothill Highway",
            "vulnerability_note": "Low disruption probability under present weather conditions."
        }
    }

    # 2. Automated Selection Dropdown
    selected_route = st.selectbox(
        "🛣️ Select Route Corridor for Risk Assessment",
        options=list(ROUTE_RISK_DATABASE.keys()),
        index=0
    )

    # Fetch pre-populated live/historical risk data
    risk_data = ROUTE_RISK_DATABASE[selected_route]

    st.info(f"**Terrain Profile:** {risk_data['terrain_type']} — *{risk_data['vulnerability_note']}*")

    # 3. Environmental Parameters (Auto-Populated & Fine-Tunable)
    st.subheader("🌐 Real-Time Environmental Inputs (Auto-populated)")

    with st.expander("Tweak/Override Live Inputs (Optional)", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            rainfall = st.number_input(
                "Live Rainfall Rate (mm)",
                min_value=0.0,
                max_value=300.0,
                value=float(risk_data["rainfall"]),
                step=5.0,
                help="Automatically loaded from regional weather stations."
            )

            flood = st.slider(
                "Flood Risk Level",
                min_value=0,
                max_value=100,
                value=int(risk_data["flood"]),
                help="Based on water table levels and recent river overflow reports."
            )

        with col2:
            landslide = st.slider(
                "Landslide Susceptibility Index",
                min_value=0,
                max_value=100,
                value=int(risk_data["landslide"]),
                help="Calculated using slope gradient, soil moisture, and historical blockage data."
            )

    # 4. Instant Risk Calculation (Runs automatically without button click)
    result = calculate_risk(
        rainfall,
        flood,
        landslide
    )

    st.divider()

    # 5. Display Risk Assessment Results
    st.subheader("Risk Assessment Verdict")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Composite Risk Score",
            f'{result["score"]}/100'
        )

    with col2:
        st.metric(
            "Risk Category Level",
            result["level"]
        )

    # Actionable Advisory Box
    if result["level"] == "LOW":
        st.success(f"{result['recommendation']}")
    elif result["level"] == "MEDIUM":
        st.warning(f"{result['recommendation']}")
    else:
        st.error(f"{result['recommendation']}")

#"Emergency Logistics
#.....
elif page == "Emergency Logistics":

    st.title("🚑 Emergency Logistics")

    hospitals = [
        "GMCH - Guwahati",
        "Civil Hospital - Shillong",
        "JN Hospital - Imphal",
        "Civil Hospital - Aizawl"
    ]

    hospital = st.selectbox(
        "Select Hospital",
        hospitals,
        key="emergency_hospital"
    )

    cargo = st.selectbox(
        "Emergency Cargo",
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
        "Quantity",
        min_value=1,
        value=10,
        key="emergency_quantity"
    )

    if st.button(
        "🚑 Create Emergency Request",
        key="create_emergency_request"
    ):

        emergency_id = create_emergency(
            hospital,
            cargo,
            quantity
        )

        st.success(
            f"Emergency request "
            f"EMG-{emergency_id} created."
        )

        st.warning(
            "Priority automatically set to CRITICAL."
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
#"Emergency Logistics
#.....
elif page == "Emergency Logistics":

    st.title("🚑 Emergency Logistics")

    hospitals = [
        "GMCH - Guwahati",
        "Civil Hospital - Shillong",
        "JN Hospital - Imphal",
        "Civil Hospital - Aizawl"
    ]

    hospital = st.selectbox(
        "Select Hospital",
        hospitals
    )

    cargo = st.selectbox(
        "Emergency Cargo",
        [
            "Blood",
            "Medical Supplies",
            "Medicines",
            "Food",
            "Water"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=10
    )

    if st.button(
        "🚑 Create Emergency Request"
    ):

        emergency_id = create_emergency(
            hospital,
            cargo,
            quantity
        )

        st.success(
            f"Emergency request "
            f"EMG-{emergency_id} created."
        )

        st.warning(
            "Priority automatically set to CRITICAL."
        )