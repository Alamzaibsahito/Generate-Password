import streamlit as st
import random
import string
import pyperclip  


# Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    if length < 8:
        return "🔴Weak"
    elif 8 <= length < 12:
        return "🟡Moderate"
    else:
        return "🟢Strong"

# Function to generate a random password
def generate_password(length, use_numbers, use_symbols):
    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Streamlit App Layout
st.markdown("<h1 style='text-align: center; color: white;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

# CSS to customize the UI and make it responsive
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        div[data-testid="stSidebar"] {
            background-color: yellow
        }
        h1 {
            background-color: red;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-size: 2.5rem;
        }
        .stButton button {
            background-color: pink;
            color: white;
            border-radius: 10px;
            padding: 8px 16px;
            font-size: 1rem;
        }
        .stSlider {
            color: green;
        }
        footer {
            bottom: 0;
            width: 100%;
            background-color: #2;
            color: black;
            text-align: center;
            padding: 20px;
            font-size: 1rem;
            font-weight: bold;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 15px;
            margin-top: 20px;
        }
        @media only screen and (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
            .stButton button {
                font-size: 0.9rem;
                padding: 6px 12px;
            }
            footer {
                font-size: 0.9rem;
                padding: 15px;
            }
        }
        @media only screen and (max-width: 480px) {
            h1 {
                font-size: 1.5rem;
            }
            .stButton button {
                font-size: 0.8rem;
                padding: 5px 10px;
            }
            footer {
                font-size: 0.8rem;
                padding: 10px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Choose method for generating password
password_method = st.radio(
    "Choose your password method:", 
    ('🎲 Generate Password', '✍️ Enter Password')
)

if password_method == '🎲 Generate Password':
    length = st.slider('Password Length', 8, 32, 16)
    use_numbers = st.checkbox('🔢 Include Numbers', value=True)
    use_symbols = st.checkbox('💎 Include Symbols', value=True)
    
    if st.button('🎲 Generate Password'):
        generated_password = generate_password(length, use_numbers, use_symbols)
        st.success(f'🔐 Generated Password: {generated_password}')
        strength = calculate_strength(generated_password)
        st.info(f'💡 Password Strength: {strength}')
        

# Copy to clipboard button
if st.button("Generate and Copy Password"):
    generate_password = generate_password(length, use_numbers, use_symbols)
    st.success(f"🔐 Generated Password: {generate_password}")
        # Save Password as Text File
    if st.button("💾 Save Password"):
        with open("password.txt", "w") as f:
            f.write(generated_password)
        st.success("✅ Password Saved as password.txt!")


    # Copy to clipboard
    if st.button("Copy to Clipboard"):
        pyperclip.copy(generate_password)
        st.success("📋 Password copied to clipboard")


elif password_method == '✍️ Enter Password':
    show_password = st.checkbox("👁 Show Password", value=False)
    entered_password = st.text_input('Enter your password', type='password')
    if entered_password:
        strength = calculate_strength(entered_password)
        st.info(f'💡 Password Strength: {strength}')

# Responsive centered footer
st.markdown("""
    <footer>
        Made with ❤️ Alam Zaib | <a href="https://github.com/Alamzaibsahito" target="_blank">GitHub</a>
    </footer>
""", unsafe_allow_html=True)
