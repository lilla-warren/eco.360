import streamlit as st
from streamlit_drawable_canvas import st_canvas
import qrcode
from PIL import Image
import io

# ✅ This must be the FIRST Streamlit command
st.set_page_config(page_title="Eco360 Interactive Mockup", layout="wide")

# --- Inject Model Viewer dependencies ---
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.css">
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
    model-viewer {
        --progress-bar-color: #4CAF50;
        --progress-bar-height: 5px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 20px 0;
        background-color: #f8f9fa;
    }
    .model-container {
        width: 100%;
        height: 500px;
        position: relative;
    }
    .ar-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
    }
</style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("🛋️ Eco360: Sustainable Furniture Mockups")

# --- Furniture Section ---
st.sidebar.header("1. Furniture Selection")

furniture_items = {
    "Modern Sofa": {
        "image": "https://images.unsplash.com/photo-1585559605154-3f0f3f1e1f1e?auto=format&fit=crop&w=800&q=60",
        "3d_model": "https://cdn.jsdelivr.net/gh/KhronosGroup/glTF-Sample-Models/2.0/Sofa/glTF/Sofa.gltf",
        "price": 1200,
        "materials": "Recycled fabric, reclaimed wood"
    },
    "Ergonomic Chair": {
        "image": "https://images.unsplash.com/photo-1616627982374-5b5d5d5d5d5d?auto=format&fit=crop&w=800&q=60",
        "3d_model": "https://cdn.jsdelivr.net/gh/KhronosGroup/glTF-Sample-Models/2.0/Chair/glTF/Chair.gltf",
        "price": 450,
        "materials": "Bamboo, organic cotton"
    },
    "Dining Table": {
        "image": "https://images.unsplash.com/photo-1602526219042-3c3c3c3c3c3c?auto=format&fit=crop&w=800&q=60",
        "3d_model": "https://cdn.jsdelivr.net/gh/KhronosGroup/glTF-Sample-Models/2.0/Table/glTF/Table.gltf",
        "price": 800,
        "materials": "Reclaimed teak wood"
    },
    "Bookshelf": {
        "image": "https://images.unsplash.com/photo-1598300056589-4d4d4d4d4d4d?auto=format&fit=crop&w=800&q=60",
        "3d_model": "https://cdn.jsdelivr.net/gh/KhronosGroup/glTF-Sample-Models/2.0/Bookshelf/glTF/Bookshelf.gltf",
        "price": 350,
        "materials": "Recycled plastic, aluminum"
    }
}

furniture_choice = st.sidebar.selectbox("Choose a furniture item", list(furniture_items.keys()))
color = st.sidebar.color_picker("Pick furniture color", "#4CAF50")

# --- Show Furniture Image ---
try:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(furniture_items[furniture_choice]["image"], caption=f"Selected: {furniture_choice}", width=300)
        st.markdown(f"""
        **Price:** AED {furniture_items[furniture_choice]["price"]:,}  
        **Materials:** {furniture_items[furniture_choice]["materials"]}
        """)
except Exception as e:
    st.error("Failed to load furniture image")
    st.warning(f"Technical details: {str(e)}")

# --- Cost Estimator ---
st.sidebar.header("2. Cost Estimator")
layout_area = st.sidebar.slider("Layout Area (sqm)", 10, 200, 50)
duration = st.sidebar.selectbox("Usage Duration", ["1 week", "1 month", "6 months"])
quality = st.sidebar.radio("Material Quality", ["Standard", "Premium", "Eco-friendly"])

base_price = furniture_items[furniture_choice]["price"] / 10
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
    fill_color=color + "80",
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
<div class="model-container">
    <model-viewer 
        src="{furniture_items[furniture_choice]['3d_model']}" 
        alt="3D model of {furniture_choice}"
        style="width: 100%; height: 100%"
        camera-controls 
        auto-rotate 
        ar
        shadow-intensity="1"
        exposure="0.8"
        environment-image="neutral"
        background-color="#f0f0f0">
        <button slot="ar-button" class="ar-button">
            👆 View in AR
        </button>
    </model-viewer>
</div>
""", unsafe_allow_html=True)

# --- AR Experience ---
st.markdown("## 🕶️ AR Experience")
qr = qrcode.make(f"https://eco3600.streamlit.app/?item={furniture_choice.replace(' ', '_')}")
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)

col1, col2 = st.columns(2)
with col1:
    st.image(Image.open(buf), caption="Scan QR code for AR")
with col2:
    st.markdown(f"""
    ### Try our AR Experience
    1. Scan the QR code with your phone  
    2. View the **{furniture_choice}** in your space  
    3. See how it fits before buying  

    *Requires iOS 12+/Android 8+ with ARCore support*
    """)

# --- Feedback ---
st.markdown("## 💬 Feedback")
stars = st.slider("Rate your experience", 1, 5, 4)
comments = st.text_area("Your feedback")
if st.button("Submit Feedback"):
    st.success("✅ Thank you for your feedback!")

# --- Walkthrough Video ---
st.markdown("## 🎥 How It Works")
st.video("https://www.youtube.com/watch?v=9No-FiEInLA")  # Replace with your actual tutorial link

