# Morse Code ↔ English Converter

This is a simple web application built with **Streamlit** that allows users to convert text between **English** and **Morse Code**. It provides two-way conversion:

1. **English to Morse Code**
2. **Morse Code to English**

## Features

- **Convert English to Morse Code**: Type English text, and the app will convert it to Morse code.
- **Convert Morse Code to English**: Type Morse code (with dots, dashes, and spaces), and the app will convert it back to English text.
- **Copy to Clipboard**: You can copy the converted result to your clipboard for easy use.

## How It Works

1. **Text Input**: The user enters English text or Morse code into the input box.
2. **Conversion Logic**: The app determines if the input is Morse code or English and converts it accordingly:
   - **English to Morse Code**: Each letter is converted to its Morse code equivalent using the predefined dictionary.
   - **Morse Code to English**: Each Morse code character is decoded back to its English letter using the reverse dictionary.
3. **Copy to Clipboard**: After conversion, the user can click on the **Copy to Clipboard** button to copy the converted result.

## Example

### English to Morse Code:
Input:
```
Hello
```
Output:
```
.... . .-.. .-.. ---
```

### Morse Code to English:
Input:
```
.... . .-.. .-.. ---
```
Output:
```
Hello
```

## Usage

1. Enter **English** text into the input box to get the **Morse Code**.
2. Enter **Morse Code** (with dots, dashes, and spaces) to get back the **English** text.
3. After conversion, click the **Copy to Clipboard** button to copy the result.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
