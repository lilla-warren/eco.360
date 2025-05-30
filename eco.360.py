
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
    "Sofa": "https://images.unsplash.com/photo-1555041469-586c214f8342?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c29mYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    "Chair": "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2hhaXJ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    "Table": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dGFibGV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    "Shelf": "https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c2hlbGZ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60"
}

furniture_choice = st.sidebar.selectbox("Choose a furniture item", list(furniture_items.keys()))
color = st.sidebar.color_picker("Pick furniture color", "#f0a500")

# Display furniture image with error handling
try:
    st.image(
        furniture_items[furniture_choice],
        caption=f"Selected: {furniture_choice}", 
        width=300,
        use_column_width=False
    )
except Exception as e:
    st.error("Failed to load furniture image")
    st.warning(f"Technical details: {str(e)}")
    st.info("Please try again later or contact support")

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
# Using a YouTube video as example - replace with your own
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
 
