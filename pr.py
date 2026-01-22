import streamlit as st
from PIL import Image
import base64

# Page setup
st.set_page_config(page_title="Forest Landing Page", layout="wide")

# --- Custom CSS ---
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('https://cdn.pixabay.com/photo/2018/10/23/20/24/forest-3769959_1280.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.navbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 80px;
    background-color: rgba(0, 0, 0, 0.6);
    border-radius: 12px;
}}

.navbar .logo {{
    color: white;
    font-size: 26px;
    font-weight: bold;
}}

.navbar ul {{
    list-style: none;
    display: flex;
    gap: 30px;
    margin: 0;
}}

.navbar ul li {{
    color: white;
    cursor: pointer;
    font-weight: 500;
    transition: color 0.3s;
}}

.navbar ul li:hover {{
    color: #00bcd4;
}}

.login-btn {{
    padding: 8px 18px;
    border: 2px solid white;
    color: white;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s;
}}

.login-btn:hover {{
    background-color: #00bcd4;
    color: black;
}}

.content {{
    text-align: center;
    color: white;
    margin-top: 180px;
}}

.content h1 {{
    font-size: 50px;
    font-weight: bold;
}}

.content p {{
    font-size: 22px;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# --- Navbar ---
st.markdown("""
<div class="navbar">
    <div class="logo">Logo</div>
    <ul>
        <li>Home</li>
        <li>About</li>
        <li>Services</li>
        <li>Contact</li>
    </ul>
    <div class="login-btn">Login</div>
</div>
""", unsafe_allow_html=True)

# --- Center Content ---
st.markdown("""
<div class="content">
    <h1>Welcome to the Wild Forest</h1>
    <p>Discover the beauty of nature and wildlife.</p>
</div>
""", unsafe_allow_html=True)