import streamlit as st


def hero():

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                🛰️ NER Smart Logistics
            </div>

            <div class="hero-subtitle">
                AI-Based Logistics & Accessibility
                Intelligence Platform for North Eastern India
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def kpi(title, value, status):

    st.markdown(
        f"""
        <div class="kpi">

            <div class="kpi-title">
                {title}
            </div>

            <div class="kpi-value">
                {value}
            </div>

            <div class="kpi-status">
                ● {status}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def alert_card(title, message, level):

    css_class = "alert-green"

    if level == "HIGH":
        css_class = "alert-red"

    elif level == "MEDIUM":
        css_class = "alert-orange"

    st.markdown(
        f"""
        <div class="alert {css_class}">

            <strong>{title}</strong>

            <br>

            <span>
                {message}
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )