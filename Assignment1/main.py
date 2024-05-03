# Define Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_code:
            morse += morse_code[char] + ' '
        else:
            morse += char  # If character not in dictionary, keep it as is
    return morse.strip()

# Main function
def main():
    print("Welcome to the Morse Code Converter!")
    while True:
        user_input = input("Enter text to convert (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Morse Code Converter. Goodbye!")
            break
        else:
            morse_text = text_to_morse(user_input)
            print("Morse Code:", morse_text)

if __name__ == "__main__":
    main()

