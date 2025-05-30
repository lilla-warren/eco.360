import streamlit as st
from streamlit_drawable_canvas import st_canvas
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Eco360 Interactive Mockup", layout="wide")
st.title("🛋️ Eco360: Sustainable Furniture Mockups")

# --- Add ModelViewer CSS/JS ---
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.css">
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
    model-viewer {
        --progress-bar-color: #4CAF50;
        --progress-bar-height: 5px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- Furniture Section ---
st.sidebar.header("1. Furniture Selection")
furniture_items = {
    "Sofa": {
        "image": "https://images.unsplash.com/photo-1555041469-586c214f8342?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c29mYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "3d_model": "https://modelviewer.dev/shared-assets/models/sofa.glb"
    },
    "Chair": {
        "image": "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2hhaXJ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "3d_model": "https://modelviewer.dev/shared-assets/models/chair.glb"
    },
    "Table": {
        "image": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dGFibGV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "3d_model": "https://modelviewer.dev/shared-assets/models/table.glb"
    },
    "Shelf": {
        "image": "https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c2hlbGZ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "3d_model": "https://modelviewer.dev/shared-assets/models/bookshelf.glb"
    }
}

furniture_choice = st.sidebar.selectbox("Choose a furniture item", list(furniture_items.keys()))
color = st.sidebar.color_picker("Pick furniture color", "#f0a500")

# Display furniture image
try:
    st.image(
        furniture_items[furniture_choice]["image"],
        caption=f"Selected: {furniture_choice}", 
        width=300,
        use_column_width=False
    )
except Exception as e:
    st.error("Failed to load furniture image")
    st.warning(f"Technical details: {str(e)}")

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
st.markdown(f"""
<model-viewer 
    src="{furniture_items[furniture_choice]['3d_model']}" 
    alt="3D model of {furniture_choice}"
    style="width: 100%; height: 500px"
    camera-controls 
    auto-rotate 
    ar
    shadow-intensity="1"
    exposure="0.8"
    environment-image="neutral"
    background-color="#f0f0f0">
    <div class="progress-bar" slot="progress-bar"></div>
</model-viewer>
""", unsafe_allow_html=True)

st.caption("Rotate the model with your mouse. Click the AR icon to view in augmented reality on supported devices.")

# --- AR Feature ---
st.markdown("## 🕶️ AR Experience")
st.markdown(f"""
<model-viewer 
    src="{furniture_items[furniture_choice]['3d_model']}" 
    alt="AR view of {furniture_choice}"
    style="width: 100%; height: 400px"
    ar
    ar-modes="scene-viewer quick-look webxr"
    camera-controls
    environment-image="neutral"
    shadow-intensity="1"
    auto-rotate>
    <button slot="ar-button" style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
        View in AR
    </button>
</model-viewer>
""", unsafe_allow_html=True)

# --- Feedback Section ---
st.markdown("## 💬 Feedback")
stars = st.slider("Rate your experience", 1, 5, 4)
comments = st.text_area("Your feedback")
if st.button("Submit Feedback"):
    st.success("✅ Thank you for your feedback!")

# --- Walkthrough Video ---
st.markdown("## 🎥 Walkthrough")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with your actual video
