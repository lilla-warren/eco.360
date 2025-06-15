import streamlit as st
import time

st.set_page_config(page_title="Project: SANE", layout="centered")

# Terminal effect
def typewriter(text):
    for char in text:
        st.markdown(f"<span style='color:#cccccc'>{char}</span>", unsafe_allow_html=True)
        time.sleep(0.03)

st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>PROJECT: SANE</h1>", unsafe_allow_html=True)
st.markdown("---")

typewriter("[ ██ ] Memory restoration initialized...")
time.sleep(0.3)
typewriter("[ ██ ] Loop detected...")
time.sleep(0.3)
typewriter("[ ██ ] Authentication bypassed.")
time.sleep(0.4)

st.markdown(" ")
if st.button("ENTER THE LOOP"):
    st.session_state.entered = True

if st.session_state.get("entered", False):
    codename = st.text_input("Enter your codename:", placeholder="e.g. KAIROS")
    if codename:
        st.markdown(f"**Welcome, {codename.upper()}**")
        st.info("“We remember you. Even if you don’t.”")

st.set_page_config(page_title="PROJECT: SANE - Memory Loop", layout="centered")

# Initialize session state
if "codename" not in st.session_state:
    st.session_state.codename = None
if "fragments" not in st.session_state:
    st.session_state.fragments = []

# Typing animation function
def typewriter(text, delay=0.03):
    typed = ""
    for char in text:
        typed += char
        st.markdown(f"<span style='color:#cccccc;font-family:monospace;'>{typed}</span>", unsafe_allow_html=True)
        time.sleep(delay)

# Entry screen
st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>PROJECT: SANE</h1>", unsafe_allow_html=True)
st.markdown("---")

if not st.session_state.codename:
    typewriter("[ ██ ] MEMORY ACCESS ENGAGED...")
    time.sleep(0.3)
    typewriter("[ ██ ] SCANNING LOOP...")
    time.sleep(0.3)
    typewriter("[ ██ ] FRAGMENT INTERFACE READY.")
    time.sleep(0.3)

    codename = st.text_input("Enter your codename:", placeholder="e.g. VANTA, KAIROS, NULL")
    if codename:
        st.session_state.codename = codename.upper()
        st.success(f"Welcome, {st.session_state.codename}")
        st.info("“Fragments do not lie. They just forget the order.”")
        st.experimental_rerun()

# Main archive interface
if st.session_state.codename:
    st.markdown(f"### Logged in as: `{st.session_state.codename}`")
    st.markdown("#### Submit a memory fragment (anonymously):")
    fragment = st.text_area("Memory Fragment", placeholder="e.g. I saw him again in the corridor. But this time, he didn't remember me.")

    if st.button("Submit Fragment"):
        if fragment.strip():
            st.session_state.fragments.append((st.session_state.codename, fragment.strip()))
            st.success("Fragment uploaded.")
        else:
            st.warning("Empty fragments vanish in the void.")

    st.markdown("---")
    st.markdown("## 🧠 The Loop Archives")
    if st.session_state.fragments:
        for i, (code, frag) in enumerate(reversed(st.session_state.fragments), 1):
            st.markdown(f"**[{code}]**")
            st.markdown(f"> {frag}")
            st.markdown("---")
    else:
        st.markdown("_No fragments yet..._ The silence is suspicious.")
