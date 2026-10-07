import streamlit as st
import random

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Jahnavi Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fff7ed, #ffedd5, #fed7aa);
    }

    .title {
        text-align: center;
        color: #9a3412;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #c2410c;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .result {
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff;
        border: 2px solid #fb923c;
        margin-top: 20px;
    }

    .score {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #7c2d12;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        font-size: 18px;
        font-weight: bold;
        background-color: #f97316;
        color: white;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #ea580c;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Session State
# -------------------------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "ties" not in st.session_state:
    st.session_state.ties = 0

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""

if "result" not in st.session_state:
    st.session_state.result = ""

# -------------------------------
# Game Choices
# -------------------------------
choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# -------------------------------
# Game Logic
# -------------------------------
def play_game(user_choice):
    computer_choice = random.choice(list(choices.keys()))

    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice

    if user_choice == computer_choice:
        st.session_state.result = "It's a Tie! 🤝"
        st.session_state.ties += 1

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.session_state.result = "You Win! 🎉"
        st.session_state.user_score += 1

    else:
        st.session_state.result = "Computer Wins! 🤖"
        st.session_state.computer_score += 1


# -------------------------------
# Reset Game
# -------------------------------
def reset_game():
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.user_choice = ""
    st.session_state.computer_choice = ""
    st.session_state.result = ""


# -------------------------------
# Main Title
# -------------------------------
st.markdown(
    '<div class="title">🎮Jahnavi Rock Paper Scissors</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Play against the computer!</div>',
    unsafe_allow_html=True
)

# -------------------------------
# Scoreboard
# -------------------------------
st.markdown("### 🏆 Scoreboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f'<div class="score">👤 You<br>{st.session_state.user_score}</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f'<div class="score">🤝 Ties<br>{st.session_state.ties}</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f'<div class="score">🤖 Computer<br>{st.session_state.computer_score}</div>',
        unsafe_allow_html=True
    )

st.divider()

# -------------------------------
# Game Instructions
# -------------------------------
st.subheader("Choose your move:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Rock"):
        play_game("Rock")

with col2:
    if st.button("📄 Paper"):
        play_game("Paper")

with col3:
    if st.button("✂️ Scissors"):
        play_game("Scissors")

# -------------------------------
# Display Result
# -------------------------------
if st.session_state.result:

    st.markdown(
        '<div class="result">',
        unsafe_allow_html=True
    )

    st.subheader(st.session_state.result)

    st.write(
        f"👤 **You:** "
        f"{choices[st.session_state.user_choice]} "
        f"{st.session_state.user_choice}"
    )

    st.write(
        f"🤖 **Computer:** "
        f"{choices[st.session_state.computer_choice]} "
        f"{st.session_state.computer_choice}"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Reset Button
# -------------------------------
st.write("")

if st.button("🔄 Reset Game"):
    reset_game()
    st.rerun()

# -------------------------------
# Rules
# -------------------------------
with st.expander("📖 Game Rules"):
    st.write("""
    ** Jahnavi Rock Paper Scissors Rules:**

    🪨 Rock beats ✂️ Scissors

    📄 Paper beats 🪨 Rock

    ✂️ Scissors beats 📄 Paper

    Same choices result in a 🤝 Tie.
    """)

# -------------------------------
# Footer
# -------------------------------
st.divider()

st.caption("🎮 Rock Paper Scissors Game | Built with Python & Streamlit")