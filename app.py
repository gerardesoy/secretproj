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
    
    /* Phone-like container */
    .main .block-container {
        max-width: 500px !important;
        margin: 0 auto !important;
        padding: 2rem 1.5rem !important;
        min-height: 100vh !important;
        box-shadow: 0 0 40px rgba(255, 75, 139, 0.3) !important;
        border-left: 5px solid #ff4b8b !important;
        border-right: 5px solid #ff4b8b !important;
        position: relative !important;
        background-color: #fff5f8;
    }
    
    @media (max-width: 600px) {
        .main .block-container {
            max-width: 100% !important;
            border-left: none !important;
            border-right: none !important;
            box-shadow: none !important;
        }
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
    .stButton {
        width: 100% !important;
    }
    
    .stButton>button {
        background-color: #ff4b8b !important;
        color: white !important;
        border-radius: 25px !important;
        border: 2px solid white !important;
        padding: 15px 32px !important;
        font-size: 20px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        display: block !important;
        margin: 0 auto !important;
        width: 320px !important;
        max-width: 100% !important;
        transition: transform 0.3s ease, background-color 0.3s ease;
        animation: fadeIn 2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #ff1f6d !important;
    }
    
    img {
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        max-width: 100%;
        animation: fadeIn 1.5s ease-in-out;
    }
    
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
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
            
    /* BOUNCING ARROW ANIMATION */
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-10px);}
            60% {transform: translateY(-5px);}
        }

        .scroll-down {
            text-align: center;
            font-size: 30px;
            color: #ff4b8b;
            animation: bounce 2s infinite;
            margin-top: 20px;
            opacity: 0.7;
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

    # --- SLIDE 1
    if st.session_state.page == 1:
        st.write("## 💌 You have a new message!")
        st.write("Someone sent you a very important delivery...")
        
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        with col3:
            st.image("nailong-clap.gif", use_container_width=True)
          
        if st.button("Open Message 📂", use_container_width=True):
            next_page()

    # --- SLIDE 2
    elif st.session_state.page == 2:
       
        st.write("## hehe ...")
        
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        with col3:
            st.image("nailong1.png", use_container_width=True)
            pass
            
        if st.button("...", use_container_width=True):
            next_page()

    # --- SLIDE 3
    elif st.session_state.page == 3:
        st.write("## okay so ...")
        
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        with col3:
            st.image("nailong2.png", use_container_width=True)
            pass

        if st.button("...", use_container_width=True):
            next_page()

    # --- SLIDE 4
    elif st.session_state.page == 4:
        
        lines = [
            "I realized we have been talking for a while now and I really enjoy our conversations 😊",
            "and I have been thinking...",
            "...",
            "..."
        ]
        
        if 'slide5_done' not in st.session_state:
            placeholder.empty()
            time.sleep(0.1)
            with placeholder.container():
                text_spot = st.empty()
                displayed_text = ""
                
                # Simplified typing loop for stability
                displayed_lines = [] 
                for line in lines:
                    displayed_lines.append("") 
                    for char in line:
                        displayed_lines[-1] += char
                        formatted_text = "\n\n".join([f"### {l}" for l in displayed_lines])
                        text_spot.markdown(f"{formatted_text}▌")
                        time.sleep(0.05)
                    time.sleep(0.2)
                
                st.session_state.slide5_done = True

                formatted_text = "\n\n".join([f"### {l}" for l in lines])
                text_spot.markdown(formatted_text)
                
                # --- ARROW ADDED HERE ---
                st.markdown('<div class="scroll-down">⬇️</div>', unsafe_allow_html=True)
                
                col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
                with col3:
                    st.image("nailong-writing.gif", use_container_width=True)
                    pass

                st.write("") 
                if st.button("...", use_container_width=True):
                    next_page()

        else:
            formatted_text = "\n\n".join([f"### {l}" for l in lines])
            st.markdown(formatted_text)
            
            # --- ARROW ADDED HERE ---
            st.markdown('<div class="scroll-down">⬇️</div>', unsafe_allow_html=True)

            st.write("") 
            if st.button("...", use_container_width=True):
                    next_page()

    # --- SLIDE 5
    elif st.session_state.page == 5:
        
        lines = [
            "Valentine's Day is coming up and I want to take you out. 🌹",
            "Tas I know Saturday pag 14 and you might have class and your practice...",
            "So I was thinking sa Thursday nalang",
            "Kay",
            "Your class ends at 4 PM.",
            "My class ends at 5 PM.",
            "And...",
            "I have something I want to give you in person.",
        ]

        if 'slide6_done' not in st.session_state:
            placeholder.empty()
            time.sleep(0.1) 
            with placeholder.container():
                text_spot = st.empty()
                displayed_text = ""
                
                displayed_lines = []
                for line in lines:
                    displayed_lines.append("")
                    for char in line:
                        displayed_lines[-1] += char
                        formatted_text = "\n\n".join([f"### {l}" for l in displayed_lines])
                        text_spot.markdown(f"{formatted_text}▌")
                        time.sleep(0.04)
                    time.sleep(0.3)
                
                st.session_state.slide6_done = True
                text_spot.markdown(f"### {displayed_text}")
                
                # --- ARROW ADDED HERE ---
                st.markdown('<div class="scroll-down">⬇️</div>', unsafe_allow_html=True)

                st.write("") 
                if st.button(":0", use_container_width=True):
                    next_page()

        else:
            full_text = "\n\n".join(lines)
            st.markdown(f"### {full_text}")
            
            # --- ARROW ADDED HERE ---
            st.markdown('<div class="scroll-down">⬇️</div>', unsafe_allow_html=True)

            col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
            with col3:
                st.image("nailong-heart.gif", use_container_width=True)
                pass
            st.write("") 
            if st.button("wooow", use_container_width=True):
                next_page()
            if st.button("okayyy", use_container_width=True):
                next_page()

    # --- SLIDE 6
    elif st.session_state.page == 6:

        st.markdown('<div class="no-animate">', unsafe_allow_html=True)
        st.write("# So...")
        st.write("## May I be your Valentine? 🌹")
        
        yes_text = "YES! 💖"
        no_text = "No"
        
        if st.session_state.no_count == 1:
            no_text = "Are you sure?"
        elif st.session_state.no_count == 2:
            no_text = "Are you really sure?"
        elif st.session_state.no_count == 3:
            no_text = "Are you really reallllyyy sure?"
        elif st.session_state.no_count == 4:
            no_text = "sure na talaga?"
        elif st.session_state.no_count == 5:
            no_text = "sure na sure na ba talaga?"
        elif st.session_state.no_count == 6:
            no_text = "grabe pipindut lagihap an no"
        elif st.session_state.no_count == 7:
            no_text = "wow pipindut gud lagihap DAWHDH"
        elif st.session_state.no_count == 8:
            no_text = "kayano ka pa aadi"
        elif st.session_state.no_count == 9:
            no_text = "hala kay gin spam nala inin na button"
        elif st.session_state.no_count == 10:
            no_text = "mawawara na adin na option"
        elif st.session_state.no_count == 11:
            no_text = "3"
        elif st.session_state.no_count == 12:
            no_text = "2"
        elif st.session_state.no_count == 13:
            no_text = "1"
        elif st.session_state.no_count == 14:
            no_text = "0"

        col1, col2 = st.columns([1, 1])
        
        if st.session_state.no_count < 14:
            with col1:
                if st.button(yes_text, key="yes_btn", use_container_width=True):
                    next_page()
            with col2:
                if st.button(no_text, key="no_btn", use_container_width=True):
                    click_no()
        else:
            st.write("okay, tama na sa pagiging over")
            if st.button("YES!", use_container_width=True):
                next_page()
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- SLIDE 7
    elif st.session_state.page == 7:
        st.write("# YAY!")

        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        with col3:
            st.image("nailong-dancing.gif", use_container_width=True)
            pass
        
        st.balloons()
        st.write("")
        st.info("ℹ️ **System Notice:**\n\nMore details will be talked about :>")
