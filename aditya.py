import streamlit as st
import yagmail
st.header("Hybrid Communication System")
# Vigenere Cipher functions
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def decryptvigenere(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


# Polybius Cipher function

def polybiusCipher(s):
    cipher_text = ""
    for char in s:
        row = int((ord(char) - ord('a')) / 5) + 1
        col = ((ord(char) - ord('a')) % 5) + 1
        if char == 'k':
            row = row - 1
            col = 5 - col + 1
        elif ord(char) >= ord('j'):
            if col == 1:
                col = 6
                row = row - 1
            col = col - 1
        cipher_text += str(row) + str(col)
    return cipher_text

#Polybius cipher decrypt
def polybiusDecrypt(s):
    orig_text = ""
    i = 0
    while i < len(s):
        row = int(s[i])
        col = int(s[i+1])
        if row == 0 or col == 0:
            i += 2
            continue
        char = chr((row - 1) * 5 + col + ord('a') - 1)
        if char > 'i':
            char = chr(ord(char) + 1)
        orig_text += char
        i += 2
    return orig_text

# Driver code
Operation = st.radio("Select Operation: ", ("Encrypt", "Decrypt"))
if Operation == "Encrypt":
    string = st.text_input("Enter the string to be Encrypted: ")
    to = st.text_input("Enter the Email Address: ")
    if(st.button("Encrypt")):
        keyword = "QWERTY"
        key_vigenere = generateKey(string, keyword)
        cipher_text_vigenere = cipherText(string, key_vigenere)

        # Using Vigenere Cipher output as input for Polybius Cipher
        polybius_input = cipher_text_vigenere.lower()  # Convert to lowercase for Polybius Cipher
        polybius_output = polybiusCipher(polybius_input)
        email_sender = "avadityaverma5@gmail.com"
        password = "nyoa dbtt csjk clku"
        yag = yagmail.SMTP(email_sender, password)
        subject = 'The Encrypted String'
        contents = ['The Polybius Encrypted String is', polybius_output]
        yag.send(to, subject, contents)
        yag.close()
        st.write("Email sent successfully")


elif Operation == "Decrypt":
    polybius_output = st.text_input("Enter the string to be Decrypted: ")
    if(st.button("Decrypt")):
        decrypted_polybius = polybiusDecrypt(polybius_output)
        key = "QWERTY"
        key_vigenere = generateKey(decrypted_polybius.upper(), key)
        decrypted_vigenere = decryptvigenere(decrypted_polybius.upper(), key_vigenere)
        st.write("Decrypted Vigenere Ciphertext:", decrypted_vigenere)