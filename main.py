import streamlit as st
from supabase import create_client

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Portal Login",
    page_icon="🔐",
    layout="centered"
)

# ---------------- SUPABASE CONFIG ----------------
SUPABASE_URL = "https://pfccvjzrxktjtfdqodsj.supabase.co"
SUPABASE_KEY = "sb_publishable_OlKUyV7L6WF4gLMY6pO15A_7Jbdhbd2"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None
# ---------------------------------------------

# If already logged in → go home
if st.session_state.logged_in:
    st.switch_page("pages/home.py")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: #f5f7fb;
}

.login-box {
    max-width: 420px;
    margin: auto;
    margin-top: 80px;
    padding: 35px;
    background: white;
    border-radius: 18px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.1);
}

.login-title {
    text-align: center;
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 25px;
}

.stButton button {
    width: 100%;
    border-radius: 12px;
    padding: 10px;
    font-size: 16px;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("<div class='login-box'>", unsafe_allow_html=True)

st.markdown("<div class='login-title'>🎓 Student Portal Login</div>", unsafe_allow_html=True)

email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    if not email or not password:
        st.warning("Please fill all fields")
    else:
        result = supabase.table("users") \
            .select("*") \
            .eq("email", email) \
            .eq("password", password) \
            .execute()

        if result.data:
            st.session_state.logged_in = True
            st.session_state.user = result.data[0]
            st.success("Login successful 🎉")
            st.switch_page("pages/home.py")
        else:
            st.error("Invalid email or password ❌")

st.markdown("</div>", unsafe_allow_html=True)
