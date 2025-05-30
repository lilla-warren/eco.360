import streamlit as st
from PIL import Image
import qrcode
import io

# App config
st.set_page_config(page_title="Eco360", layout="wide")
st.title("🌍 Eco360 – The Circular Future of Furniture")

# Sidebar navigation
sections = [
    "Home", "Furniture Lifecycle Tracker", "Green Points", "DIY Hub",
    "AI Matchmaker", "Impact Dashboard", "Subscription Boxes", "Education", "Join Us"
]
choice = st.sidebar.radio("🔎 Explore Eco360", sections)

# Reusable QR generator
def generate_qr(url):
    qr = qrcode.make(url)
    buf = io.BytesIO()
    qr.save(buf)
    buf.seek(0)
    return Image.open(buf)

# Pages
if choice == "Home":
    st.header("🏠 Welcome to Eco360")
    st.markdown("""
    Eco360 is your smart sustainability platform for the circular furniture economy. 
    Experience AR previews, track impact, earn green points, and build a better future – one chair at a time.
    """)
    st.image("https://images.unsplash.com/photo-1598300053614-6fb35d7c4e04?auto=format&fit=crop&w=1400&q=80", use_column_width=True)

elif choice == "Furniture Lifecycle Tracker":
    st.header("🔐 Furniture Lifecycle Tracker (Blockchain-backed)")
    st.markdown("""
    Each item gets a virtual passport:
    - **Ownership history**
    - **Repair records**
    - **Recycling or upcycling journey**
    - **Environmental stats (CO₂ saved, water saved)**
    
    **📦 Visual Timeline (Like Package Tracking)**
    """)
    st.image("https://miro.medium.com/v2/resize:fit:800/format:webp/1*Z3NqS34VRl7b2D7tdGG0GQ.png", caption="Furniture Lifecycle Example")

elif choice == "Green Points":
    st.header("🎯 Gamified Green Points")
    st.markdown("""
    Earn points when you:
    - Lease instead of buy
    - Recycle or donate
    - Scan furniture QR IDs
    - Attend webinars or share awareness
    
    🔁 Redeem for:
    - Discounts and deals
    - Eco-products
    - Ranks and badges
    """)
    st.progress(50)
    st.success("You've earned 150 Green Points so far!")

elif choice == "DIY Hub":
    st.header("🧰 DIY Repair & Upcycle Hub")
    st.markdown("""
    - 🎥 Watch video tutorials
    - 🪚 Follow guides (e.g., turn chairs into shelves)
    - 🔄 Share your own hacks
    - 💬 Join our upcycle forum!
    """)
    st.video("https://www.youtube.com/watch?v=8bl8K-3rM3U")

elif choice == "AI Matchmaker":
    st.header("🤖 ECO360 Matchmaker (AI-Powered)")
    st.markdown("""
    Smart suggestions for:
    - Space, taste, and budget matching
    - Sustainable swap-outs
    - 📱 AR preview in your space
    """)
    ar_link = "https://eco360-ar-demo.streamlit.app/"
    st.image(generate_qr(ar_link), caption="Scan to launch AR Experience")
    st.markdown(f"[Try AR Demo]({ar_link})")

elif choice == "Impact Dashboard":
    st.header("📊 Your Eco Impact")
    col1, col2 = st.columns(2)
    col1.metric("Wood Saved", "25kg")
    col1.metric("Plastic Diverted", "8kg")
    col2.metric("CO₂ Avoided", "42kg")
    col2.metric("Water Saved", "520L")
    st.markdown("### 🌍 Collective Impact")
    st.success("Over 14,200kg of waste diverted globally!")

elif choice == "Subscription Boxes":
    st.header("📦 Furniture Subscription Plans")
    st.markdown("""
    - 🏠 **First Apartment Starter Set**
    - 🧑‍💻 **Eco Office Pack**
    - 🧸 **Kids' Growth Furniture**

    🔄 Modular, swappable every 6–12 months.
    🟢 Always sustainable.
    """)
    st.image("https://cdn.shopify.com/s/files/1/0024/9803/5810/articles/sustainable-furniture_1600x.jpg?v=1677207791")

elif choice == "Education":
    st.header("🎓 Eco Education Program")
    st.markdown("""
    Partner with schools & universities:
    - Student upcycle design challenges
    - Earn credit for sustainability actions
    - Internship & showcase opportunities
    """)
    st.balloons()

elif choice == "Join Us":
    st.header("🤝 Join the Eco360 Revolution")
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    why = st.text_area("Tell us why you're passionate about this mission")
    if st.button("Submit"):
        st.success("Thanks! We'll get back to you soon. 🌱")

