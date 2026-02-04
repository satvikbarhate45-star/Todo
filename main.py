import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Login", page_icon="🔐")

SUPABASE_URL = "https://pfccvjzrxktjtfdqodsj.supabase.co"
SUPABASE_KEY = "sb_publishable_OlKUyV7L6WF4gLMY6pO15A_7Jbdhbd2"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None
# ----------------------------------------------

# Already logged in → go home
if st.session_state.logged_in:
    st.switch_page("pages/home.py")

# ---------------- UI ----------------
st.markdown("""
<style>
body { background: #f5f7fb; }
</style>
""", unsafe_allow_html=True)

st.title("🔐 Secure Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if not email or not password:
        st.warning("Fill all fields")
    else:
        result = supabase.table("users") \
            .select("*") \
            .eq("email", email) \
            .eq("password", password) \
            .execute()

        if result.data:
            st.session_state.logged_in = True
            st.session_state.user = result.data[0]   # ✅ SAFE
            st.switch_page("pages/home.py")
        else:
            st.error("Invalid credentials ❌")
