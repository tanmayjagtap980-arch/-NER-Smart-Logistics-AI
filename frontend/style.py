import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =========================
           MAIN APPLICATION
        ========================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(30, 64, 175, 0.15),
                    transparent 35%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(14, 116, 144, 0.12),
                    transparent 35%
                ),
                #07111f;
            color: #f8fafc;
        }


        /* =========================
           SIDEBAR
        ========================= */

        section[data-testid="stSidebar"] {
            background: #081321;
            border-right: 1px solid rgba(148,163,184,0.15);
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: white;
        }


        /* =========================
           HEADER
        ========================= */

        .hero {

            padding: 28px;

            border-radius: 20px;

            background:
                linear-gradient(
                    135deg,
                    rgba(15,23,42,0.96),
                    rgba(15,42,67,0.94)
                );

            border: 1px solid rgba(96,165,250,0.20);

            box-shadow:
                0 15px 40px rgba(0,0,0,0.25);

            margin-bottom: 25px;
        }

        .hero-title {

            font-size: 34px;
            font-weight: 800;

            color: #f8fafc;

            margin-bottom: 6px;
        }

        .hero-subtitle {

            color: #94a3b8;

            font-size: 15px;
        }


        /* =========================
           KPI CARDS
        ========================= */

        .kpi {

            padding: 20px;

            border-radius: 18px;

            background:
                linear-gradient(
                    145deg,
                    #0f1d2d,
                    #0a1625
                );

            border: 1px solid
                rgba(148,163,184,0.15);

            box-shadow:
                0 10px 25px rgba(0,0,0,0.20);

            min-height: 125px;
        }

        .kpi-title {

            color: #94a3b8;

            font-size: 13px;

            text-transform: uppercase;

            letter-spacing: 1px;
        }

        .kpi-value {

            color: #f8fafc;

            font-size: 30px;

            font-weight: 800;

            margin-top: 8px;
        }

        .kpi-status {

            color: #22c55e;

            font-size: 12px;

            margin-top: 5px;
        }


        /* =========================
           SECTION TITLE
        ========================= */

        .section-title {

            font-size: 21px;

            font-weight: 700;

            color: #f8fafc;

            margin-top: 25px;

            margin-bottom: 12px;
        }


        /* =========================
           ALERT CARDS
        ========================= */

        .alert {

            padding: 15px;

            border-radius: 14px;

            margin-bottom: 10px;

            background: #0f1d2d;

            border: 1px solid
                rgba(148,163,184,0.12);
        }

        .alert-red {

            border-left: 4px solid #ef4444;
        }

        .alert-orange {

            border-left: 4px solid #f97316;
        }

        .alert-green {

            border-left: 4px solid #22c55e;
        }


        /* =========================
           BUTTONS
        ========================= */

        .stButton > button {

            border-radius: 10px;

            border: 1px solid
                rgba(96,165,250,0.30);

            background: #10243a;

            color: white;

            font-weight: 600;

            transition: 0.2s;
        }

        .stButton > button:hover {

            border-color: #60a5fa;

            background: #163454;
        }


        /* =========================
           DATAFRAME
        ========================= */

        div[data-testid="stDataFrame"] {

            border-radius: 15px;

            overflow: hidden;
        }


        /* =========================
           REMOVE EXTRA TOP SPACE
        ========================= */

        .block-container {

            padding-top: 2rem;

            padding-bottom: 3rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )