import streamlit as st
import re
import streamlit.components.v1 as components

# Morse code dictionary
morsecode_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/",
}
# Create a reverse dictionary for Morse code to English
reverse_morsecode_dict = {}
for letter, code in morsecode_dict.items():
    reverse_morsecode_dict[code] = letter

# check if the input is Morse code
def is_morse_code(text):
    cleaned_text = text.strip()

    for char in cleaned_text:
        if char not in [".", "-", "/", " "]:
            return False

    return True

# convert English text to Morse code
def english_to_morse(text):
    morse_message = []
    for char in text:
        upper_char = char.upper()
        morse_char = morsecode_dict.get(upper_char, "")
        morse_message.append(morse_char)
    return " ".join(morse_message)

# convert Morse code to English text
def morse_to_english(code):
    cleaned_code = code.strip()

    morse_chars = cleaned_code.split()

    english_chars = []
    for morse_char in morse_chars:
        if morse_char in reverse_morsecode_dict:
            english_chars.append(reverse_morsecode_dict[morse_char])

    return "".join(english_chars)


st.set_page_config(page_title="Morse Code Converter", layout="centered")

# CSS styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f9f9f9;
        color: #222;
    }

    textarea {
        border-radius: 10px !important;
        padding: 15px !important;
        font-size: 16px !important;
        font-family: 'Inter', sans-serif !important;
    }

    .stButton button {
        background-color: #0066ff;
        color: white;
        padding: 0.6em 1.5em;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        transition: background 0.3s ease;
    }

    .stButton button:hover {
        background-color: #004dcc;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("📡 Morse Code ↔ English Converter")
st.markdown("Type in English or Morse code below, then press **Convert**.")

user_input = st.text_area(
    "", height=150, placeholder="Example: Hello OR .... . .-.. .-.. ---"
)

convert_clicked = st.button("🔁 Convert")

# Conversion logic
if convert_clicked and user_input.strip():
    if is_morse_code(user_input):
        output = morse_to_english(user_input)
        st.success("✅ Morse Code ➜ English")
    else:
        output = english_to_morse(user_input)
        st.success("✅ English ➜ Morse Code")

    st.code(output, language="text")

    # Copy button with styled success message
    components.html(
        f"""
    <div style="margin-top: 10px;">
        <button onclick="navigator.clipboard.writeText(`{output}`);
                         const msg = document.getElementById('copiedMsg');
                         msg.style.display = 'block';
                         setTimeout(() => msg.style.display = 'none', 2000);"
            style="background-color: #28a745; color: white; padding: 10px 20px;
                   font-size: 16px; border: none; border-radius: 5px; cursor: pointer;">
            📋 Copy to Clipboard
        </button>
        <p id="copiedMsg" style="display:none; margin-top: 8px; color: green; font-weight: 600;">
            ✅ Copied to clipboard!
        </p>
    </div>
    """,
        height=100,
    )
elif convert_clicked:
    st.warning("⚠️ Please enter something to convert.")

st.markdown("---")
