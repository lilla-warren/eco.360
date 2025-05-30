
# app.py
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Eco360 Interactive Mockup", layout="wide")
st.title("🛋️ Eco360: Sustainable Furniture Mockups")

# --- Furniture Section ---
st.sidebar.header("1. Furniture Selection")
furniture_items = {
    "Sofa": "assets/furniture_images/sofa.jpg",
    "Chair": "assets/furniture_images/chair.jpg",
    "Table": "assets/furniture_images/table.jpg",
    "Shelf": "assets/furniture_images/shelf.jpg"
}
furniture_choice = st.sidebar.selectbox("Choose a furniture item", list(furniture_items.keys()))
color = st.sidebar.color_picker("Pick furniture color", "#f0a500")
st.image(furniture_items[furniture_choice], caption=f"Selected: {furniture_choice}", width=300)

# --- Cost Estimator ---
st.sidebar.header("2. Cost Estimator")
layout_area = st.sidebar.slider("Layout Area (sqm)", 10, 200, 50)
duration = st.sidebar.selectbox("Usage Duration", ["1 week", "1 month", "6 months"])
quality = st.sidebar.radio("Material Quality", ["Standard", "Premium", "Eco-friendly"])

base_price = 50  # AED per sqm
multiplier = {"Standard": 1, "Premium": 1.5, "Eco-friendly": 1.2}[quality]
cost = layout_area * base_price * multiplier
if duration == "1 month":
    cost *= 1.2
elif duration == "6 months":
    cost *= 1.5
st.sidebar.success(f"💰 Estimated Cost: AED {int(cost):,}")

# --- Layout Drawing ---
st.markdown("## 🏗️ Layout Designer")
st.write("Draw your space and place your selected furniture item below:")
canvas_result = st_canvas(
    fill_color=color + "80",  # transparent fill
    stroke_width=2,
    stroke_color=color,
    background_color="#fff",
    width=600,
    height=400,
    drawing_mode="rect",
    key="canvas1"
)

# --- 3D Preview ---
st.markdown("## 🧊 3D Preview")
st.markdown("""
<iframe title="3D Furniture Preview" width="100%" height="480"
src="https://sketchfab.com/models/2bdfc662e9c94ef9b10fda2bb208f5ee/embed" 
frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# --- AR Feature ---
st.markdown("## 🕶️ AR Experience")
ar_link = "https://example.com/ar-model-view"
qr = qrcode.make(ar_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)
st.image(Image.open(buf), caption="Scan to view in AR")
st.markdown(f"[Open AR View]({ar_link})")

# --- Feedback Section ---
st.markdown("## 💬 Feedback")
stars = st.slider("Rate your experience", 1, 5, 4)
comments = st.text_area("Your feedback")
if st.button("Submit Feedback"):
    st.success("✅ Thank you for your feedback!")

# --- Walkthrough Video ---
st.markdown("## 🎥 Walkthrough")
st.video("assets/videos/walkthrough.mp4")
import os
from pathlib import Path

# Get the directory where the script is located
script_dir = Path(images).parent

furniture_items = {
    "Chair": script_dir / "images" / "chair.jpeg",
    "Table": script_dir / "images" / "table.jpeg",
    # Add other items
}

# Verify files exist
for name, path in furniture_items.items():
    if not path.exists():
        st.error(f"Image not found: {path}")
