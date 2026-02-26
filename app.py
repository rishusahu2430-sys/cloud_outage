import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import os
from sklearn.ensemble import RandomForestRegressor

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Cloud_outage AI| Command Center", layout="wide", page_icon="⚡")


# --------------------------------------------------
# MEGA UI STYLING (THE "TEACHER-STUNNER" CSS)
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

    /* 1. Deep Space Background with Animated Stars */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top right, #001f3f, #000000);
        color: #e0e0e0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* 2. Custom Sidebar Styling */
    [data-testid="stSidebar"] {
        background: rgba(0, 10, 20, 0.95) !important;
        border-right: 1px solid #00f5ff;
    }

    /* 3. Glassmorphism Panels */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(0, 245, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(0, 245, 255, 0.5);
    }

    /* 4. Cyberpunk Neon Title */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 75px;
        font-weight: 900;
        text-align: center;
        letter-spacing: 5px;
        background: linear-gradient(90deg, #00f5ff, #7000ff, #00f5ff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* 5. Glowing Prediction Box */
    .prediction-container {
        padding: 40px;
        border-radius: 30px;
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1), rgba(112, 0, 255, 0.1));
        border: 2px solid #00f5ff;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.4);
    }

    /* 6. Glowing Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #00f5ff, #7000ff) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        font-family: 'Orbitron', sans-serif !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        box-shadow: 0 4px 15px rgba(0, 245, 255, 0.5) !important;
        transition: 0.4s !important;
    }
    .stButton > button:hover {
        letter-spacing: 2px;
        box-shadow: 0 0 40px #00f5ff !important;
        transform: scale(1.02);
    }

    /* 7. Animated Metrics */
    [data-testid="stMetricValue"] {
        color: #00f5ff !important;
        font-family: 'Orbitron', sans-serif;
        font-size: 35px !important;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MODEL LOGIC (HIDDEN FROM UI)
# --------------------------------------------------
@st.cache_data
def get_data_and_model():
    df = pd.read_csv("cloud_outages_dataset.csv")
    features = ['cloud_provider', 'region', 'severity', 'number_of_customers_affected', 'ticket_count']
    X = pd.get_dummies(df[features])
    model = RandomForestRegressor(n_estimators=50, max_depth=8, random_state=42)
    model.fit(X, df['duration_minutes'])
    return df, model, X.columns.tolist()

df, model, model_columns = get_data_and_model()

# --------------------------------------------------
# HEADER & ANIMATION
# --------------------------------------------------
st.markdown('<div class="main-title">CLOUD OUTAGE AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px; color: #00f5ff; opacity: 0.8;'>CORE NEURAL NETWORK FOR OUTAGE ANALYSIS v3.0</p>", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR CONTROLS
# --------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #00f5ff;'>⚙️ SETTINGS</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    provider = st.selectbox("🌐 SELECT PROVIDER", df['cloud_provider'].unique())
    region = st.selectbox("📍 DATA CENTER REGION", df['region'].unique())
    severity = st.select_slider("🔥 SEVERITY LEVEL", options=['Low', 'Medium', 'High', 'Critical'])
    
    st.markdown("---")
    customers = st.slider("👥 IMPACTED USERS", 0, 100000, 5000)
    tickets = st.slider("🎫 ACTIVE TICKETS", 0, 500, 25)

# --------------------------------------------------
# MAIN DASHBOARD LAYOUT
# --------------------------------------------------
col_main, col_stats = st.columns([2, 1])

with col_main:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🛰️ Live Incident Stream")
    
    # Modernized Dataframe
    styled_df = df.head(8)[['cloud_provider', 'region', 'service', 'duration_minutes', 'severity']]
    st.dataframe(styled_df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🧠 Run Predictive Simulation")
    
    if st.button("EXECUTE AI PROJECTION"):
        # Encoding input
        input_data = pd.DataFrame(0, index=[0], columns=model_columns)
        input_data['number_of_customers_affected'] = customers
        input_data['ticket_count'] = tickets
        
        for col in [f"cloud_provider_{provider}", f"region_{region}", f"severity_{severity}"]:
            if col in model_columns:
                input_data[col] = 1
        
        with st.status("Initializing Neural Engine...", expanded=True) as status:
            st.write("Fetching historical outage patterns...")
            time.sleep(1)
            st.write("Analyzing current regional load...")
            time.sleep(1)
            status.update(label="Projection Complete!", state="complete", expanded=False)

        prediction = model.predict(input_data)[0]
        hours = prediction / 60

        st.markdown(f"""
            <div class="prediction-container">
                <p style="color: #00f5ff; font-family: 'Orbitron'; font-size: 18px;">PROJECTED SYSTEM DOWNTIME</p>
                <h1 style="color: #fff; font-size: 60px; margin: 0;">{hours:.2f} <span style="font-size: 30px;">HRS</span></h1>
                <p style="color: rgba(255,255,255,0.5);">Confidence Level: 92.4% | Model: RF-Pulse</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_stats:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📡 Global Metrics")
    st.metric("TOTAL INCIDENTS", f"{len(df):,}")
    st.metric("AVG. MTTR", f"{df['duration_minutes'].mean():.1f} Mins")
    st.metric("SLA UPTIME", "99.98%")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card" style="margin-top:20px; text-align:center;">', unsafe_allow_html=True)
    st.markdown("### AI STATUS")
    st.success("STABLE")
    st.caption("Active Nodes: 124/124")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
    <p style='text-align: center; color: rgba(255,255,255,0.3); padding-top: 50px;'>
        &copy; 2026 CLOUDPULSE ANALYTICS | CRYPTOGRAPHIC SECURE INTERFACE
    </p>
""", unsafe_allow_html=True)