import streamlit as st;
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title='ChainTech Network Assignment',page_icon=":ℹ:",layout='wide');
with st.container():
    col_1,col_2,col_3,col_4,col_5 = st.columns(5)
    with col_1:
        st.link_button("Home 🏠",type='secondary',url="http://localhost:8501")
    with col_2:
        st.link_button(":grey[Exercise-2] 📑",type='secondary',url="http://127.0.0.1:8000/assignment/exercise_two/")
    with col_3:
        st.link_button(":grey[Exercise-3] 📑",type='secondary',url="http://127.0.0.1:8000/assignment/exercise_two_three/")
    with col_4:
        st.link_button(":grey[Exercise-4] 📑",type='secondary',url="http://127.0.0.1:8000/assignment/exercise_four/")
    with col_5:
        st.link_button(":grey[Exercise-5] 📑",type='secondary',url="http://127.0.0.1:8000/assignment/exercise_five/")    
st.subheader('', divider='rainbow')
lottie = "https://lottie.host/79c3b10b-0505-433a-9858-c63e5ae6ce01/lVyJiXEAT4.json"
lottie_dev = "https://lottie.host/e8ce4eb8-45c5-4c97-a24d-809072fc82ff/lwJrh9Ak21.json"
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# -----Header Section-----
st.subheader("Hello Vivek Here :wave:")
st.subheader("Information about Chain Network 🛈")
st.subheader('', divider='rainbow')
with st.container():
    left_column,right_column = st.columns(2)
    with left_column:
        st.title('What Does ChainTech Network Do???')
        st.write("Chaintech Network is one of the pioneer companies of India that is leading the blockchain revolution. What sets us apart is our unwavering commitment to harnessing the full potential of blockchain. As a team, we are a collective of relentless innovators, dreamers, and doers, united by the shared vision of a better tomorrow. Our ecosystem is a playground of innovation, where cutting-edge product development, visionary recruitment solutions, and empowering venture capital services converge to shape the future. We do not just talk about change; we make it happen. If you are a forward-thinker, a trailblazer, and a believer in the transformative power of blockchain, Chaintech Network is the place for you. Join us, and together, let us pioneer a new era of possibilities, where your internship becomes a launchpad for your career and where your passion fuels the blockchain revolution.")
        st.link_button("Konw More...",type='secondary',url="https://www.chaintech.network/")
    with right_column:
        st.lottie(lottie,height=300,width=800,key='coding')
st.subheader('', divider='rainbow')
with st.container():
    left_column,mid_column,right_column,final_col = st.columns(4)
    with left_column:
        st.subheader(' ╰┈➤ :grey[Contact Company] ',divider='rainbow')
        st.link_button("Get In Touch 🤝",type='secondary',url="https://www.chaintech.network/contact-us")
        st.link_button("Careers 💼",type='secondary',url="https://www.chaintech.network/careers")
    with mid_column:
        st.subheader(' ╰┈➤ :grey[Social Media Links] ',divider='rainbow')
        st.link_button("🌐",type='secondary',url="https://www.instagram.com/chaintech.network/")
        st.link_button("ℹn",type='secondary',url="https://in.linkedin.com/company/chaintech-network")
    with st.container():
        with right_column:
            st.subheader(' ╰┈➤ :grey[About Developer] ',divider='rainbow')
            st.subheader(' 🙋 :grey[Devloped by Vivek Patel]')
            st.subheader('📞 :grey[+91 9409143233]')
        with final_col:
            st.lottie(lottie_dev,height=150,width=300,key='developing')




