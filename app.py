import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="For You 💖",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');
    
    /* ANIMATIONS */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0px); }
    }
    
    .stApp {
        background-color: #ffe6eb;
        background-image: radial-gradient(#ffccd5 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* Center all content */
    .main .block-container {
        max-width: 800px;
        margin: 0 auto;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    .main {
        display: flex;
        justify-content: center;
    }
    
    h1, h2, h3, p, div, span {
        font-family: 'Patrick Hand', cursive !important;
        color: #880d1e;
        text-align: center;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    h1 { font-size: 3rem !important; margin-bottom: 0px; }
    p { font-size: 1.5rem !important; }
    
    /* BUTTON STYLING */
    div[data-testid="stHorizontalBlock"] {
        gap: 1rem;
    }
    
    .stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    
    .stButton > button {
        background-color: #ff4b8b !important;
        color: white !important;
        border-radius: 25px !important;
        border: 2px solid white !important;
        padding: 15px 32px !important;
        font-size: 20px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        width: 100% !important;
        max-width: 400px !important;
        margin: 0 auto !important;
        display: block !important;
        transition: transform 0.3s ease, background-color 0.3s ease; 
        animation: fadeIn 2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #ff1f6d !important;
    }
    
    /* Center columns */
    [data-testid="column"] {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    [data-testid="stVerticalBlock"] > [data-testid="element-container"] {
        width: 100%;
    }
    
    img {
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        max-width: 100%;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Disable Streamlit's default fade transitions */
    .element-container {
        transition: none !important;
    }
    
    .stButton {
        transition: none !important;
    }
    
    /* Disable animations for elements that shouldn't re-animate */
    .no-animate h1, .no-animate h2, .no-animate h3, 
    .no-animate p, .no-animate div, .no-animate span {
        animation: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

def next_page():
    st.session_state.page += 1
    st.rerun()

def click_no():
    st.session_state.no_count += 1
    st.rerun()

# --- MASTER PLACEHOLDER ---
placeholder = st.empty()

with placeholder.container():

    # --- SLIDE 1: HOOK ---
    if st.session_state.page == 1:
        st.write("## 💌 You have a new message!")
        st.write("Someone sent you a very important delivery...")
        
        # st.image("nailong0.png") 
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Open Message 📂", key="btn_open"):
                next_page()

    # --- SLIDE 2: HEHE ---
    elif st.session_state.page == 2:
        st.write("## hehe ...")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("?", key="btn_hehe"):
                next_page()

    # --- SLIDE 3: OKAY SO ---
    elif st.session_state.page == 3:
        st.write("## okay so ...")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("what?", key="btn_what"):
                next_page()

    # --- SLIDE 4: THE NEW BUFFER SLIDE (NERVOUS) ---
    elif st.session_state.page == 4:
        st.write("## Actually wait...")
        st.write("I'm kinda nervous to say this. 🙈")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("It's okay, tell me...", key="btn_nervous"):
                next_page()

    # --- SLIDE 5: REALIZATION (Typing) ---
    elif st.session_state.page == 5:
        
        lines = [
            "I just realized na it's almost 6 months since we started talking.",
            "and I've been thinking..."
        ]
        
        # CLEAR PLACEHOLDER FIRST before animation
        if 'slide5_done' not in st.session_state:
            placeholder.empty()
            time.sleep(0.1)  # Small delay to ensure clean slate
            with placeholder.container():
                text_spot = st.empty()
                displayed_text = ""
                for line in lines:
                    for char in line:
                        displayed_text += char
                        text_spot.markdown(f"### {displayed_text}▌")
                        time.sleep(0.05)
                    displayed_text += "\n\n"
                
                st.session_state.slide5_done = True
                text_spot.markdown(f"### {displayed_text}")
                
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("Thinking what? 🤔", key="btn_thinking"):
                        next_page()
        else:
            full_text = "\n\n".join(lines)
            st.markdown(f"### {full_text}")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Thinking what? 🤔", key="btn_thinking"):
                    next_page()

    # --- SLIDE 6: THE PLAN (Typing) ---
    elif st.session_state.page == 6:
        
        lines = [
            "Valentine's Day is coming up and I want to take you out. 🌹",
            "Tas I know Saturday pag 14 and you might have class and your practice...",
            "So I was thinking sa Thursday?",
            "Kay...",
            "✨ Your class ends at 4 PM.",
            "✨ My class ends at 5 PM.",
            "And... I have something I want to give you in person. 👉👈"
        ]

        # CLEAR PLACEHOLDER FIRST before animation
        if 'slide6_done' not in st.session_state:
            placeholder.empty()
            time.sleep(0.1)  # Small delay to ensure clean slate
            with placeholder.container():
                text_spot = st.empty()
                displayed_text = ""
                for line in lines:
                    for char in line:
                        displayed_text += char
                        text_spot.markdown(f"### {displayed_text}▌")
                        time.sleep(0.04)
                    displayed_text += "\n\n"
                    time.sleep(0.3)
                
                st.session_state.slide6_done = True
                text_spot.markdown(f"### {displayed_text}")
                
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("Okay, I'm listening... 👀", key="btn_listening"):
                        next_page()
        else:
            full_text = "\n\n".join(lines)
            st.markdown(f"### {full_text}")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Okay, I'm listening... 👀", key="btn_listening"):
                    next_page()

    # --- SLIDE 7: THE ASK ---
    elif st.session_state.page == 7:
        # Always wrap in no-animate div to prevent re-animation on any rerun
        st.markdown('<div class="no-animate">', unsafe_allow_html=True)
        
        st.write("# So...")
        st.write("## Will you be my Valentine? 🌹")
        
        yes_text = "YES! 💖"
        no_text = "No"
        
        if st.session_state.no_count == 1:
            no_text = "Are you sure? 😢"
        elif st.session_state.no_count == 2:
            no_text = "Are you really sure?... 🥺"
        elif st.session_state.no_count == 3:
            no_text = "Are you really reallllyyy sure?"
        elif st.session_state.no_count == 4:
            no_text = "okay :<<<<< ..."
        
        # Add padding columns for better centering
        col_pad1, col1, col2, col_pad2 = st.columns([0.5, 1, 1, 0.5])
        
        if st.session_state.no_count < 5:
            with col1:
                if st.button(yes_text, key="yes_btn"):
                    next_page()
            with col2:
                if st.button(no_text, key="no_btn"):
                    click_no()
        else:
            st.write("okay tama na sa pagiging over")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("YES! (Okay fine 🙄) ", key="yes_forced"):
                    next_page()
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- SLIDE 8: SUCCESS ---
    elif st.session_state.page == 8:
        st.balloons()
        st.write("# YAY! See you Thursday! 🦖")
        
        st.write("I'll pick you up after your class. Don't be late! 😉")
        st.success("Date confirmed: Thursday, Feb 12")