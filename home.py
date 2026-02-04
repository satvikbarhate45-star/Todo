import streamlit as st

st.set_page_config(
    page_title="Students Online & Learning Portal",
    page_icon="🎓",
    layout="wide"
)


# ---------------------------------------------------

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: #f5f7fb;
}

/* TOP NAVBAR */
.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    padding: 15px 30px;
    border-radius: 0 0 18px 18px;
    color: white;
    margin-bottom: 25px;
}

.nav-left {
    font-size: 22px;
    font-weight: 700;
}

.nav-right span {
    margin-left: 20px;
    font-size: 16px;
    cursor: pointer;
    transition: opacity 0.3s ease;
}

.nav-right span:hover {
    opacity: 0.8;
}

/* Cards */
.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TOP MENU ----------------
st.markdown("""
<div class="top-nav">
    <div class="nav-left">🎓 Students Online & Learning Portal</div>
    <div class="nav-right">
        <span>Dashboard</span>
        <span>Courses</span>
        <span>Practice</span>
        <span>Results</span>
        <span>Profile</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTENT ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📘 Courses</h3>
        <p>Learn Python, Web Dev, DSA, and more.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🧠 Practice</h3>
        <p>Improve skills with coding challenges.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Progress</h3>
        <p>Track your learning journey.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="card">
        <h3>👨‍🏫 Live Classes</h3>
        <p>Attend expert-led live sessions.</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h3>📄 Study Material</h3>
        <p>Access notes, PDFs, and recordings.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- LOGOUT ----------------
st.divider()
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("main.py")
