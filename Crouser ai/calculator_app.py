import streamlit as st

# Set page config
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

# Sidebar
with st.sidebar:
    st.header("About 🧮")
    st.write("""
    This is a simple, interactive calculator app built with Streamlit.
    
    **Features:**
    - Addition, Subtraction, Multiplication, Division
    - Friendly UI with emojis
    - Built for quick calculations!
    """)
    st.markdown("---")
    st.write("Created by Your Neelachala Nayak")

# Main header
st.markdown("<h1 style='color:#4F8BF9;text-align:center;'>🧮 Fun Calculator</h1>", unsafe_allow_html=True)
st.subheader("Do quick math with style! ✨")

# Layout with columns
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0, key="num1")
with col2:
    num2 = st.number_input("Enter second number", value=0.0, key="num2")

operation = st.selectbox("Select operation", ("➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"))

result = None
if st.button("Calculate 🚀"):
    if operation == "➕ Add":
        result = num1 + num2
        emoji = "😊"
    elif operation == "➖ Subtract":
        result = num1 - num2
        emoji = "🤔"
    elif operation == "✖️ Multiply":
        result = num1 * num2
        emoji = "💪"
    elif operation == "➗ Divide":
        if num2 != 0:
            result = num1 / num2
            emoji = "🧠"
        else:
            st.error("❌ Cannot divide by zero!")
            emoji = None
    if result is not None and emoji:
        st.success(f"Result: {result} {emoji}")