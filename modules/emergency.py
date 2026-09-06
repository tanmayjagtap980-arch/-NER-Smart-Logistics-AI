import streamlit as st


def create_emergency(hospital, cargo, quantity):
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
            "Oxygen",
            "Food",
            "Other"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    priority = st.selectbox(
        "Priority",
        [
            "🔴 Critical",
            "🟠 High",
            "🟡 Medium"
        ]
    )

    if st.button("🚑 Create Emergency Request"):
        st.success("Emergency request created successfully!")

        st.write("### Emergency Details")
        st.write(f"**Hospital:** {hospital}")
        st.write(f"**Cargo:** {cargo}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Priority:** {priority}")