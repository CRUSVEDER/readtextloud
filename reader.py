import os
import string
import pygame
from gtts import gTTS
from pynput import keyboard
import time

# Sample text (replace this with your actual text)
text = """Google Dorking also known as Google hacking refers to the practice of using specially crafted search queries dorks to discover sensitive information or vulnerabilities in websites These dorks exploit advanced Google search operators e g filetype intext site to extract data that is often not visible through regular search methods While often employed by security experts and ethical hackers to identify and fix vulnerabilities malicious actors can also use these techniques to exploit weaknesses and gain unauthorized access to systems

Features and Functionalities of Google Dorks

Precise Targeting

Dorks allow users to narrow down searches to specific websites directories file types or content types For example using the site operator helps limit searches to a particular domain This precision enables users to search for specific types of information or hidden data Example siteexamplecom filetypepdf will show all PDF files hosted on the domain examplecom

Information Discovery

Dorks can uncover hidden files directories or information not indexed in standard search results For instance an improperly secured directory might be exposed using a dork Example Using intitleindexof can reveal open directories with potentially sensitive files like backups or configuration files

Vulnerability Identification

Google Dorks are widely used to find vulnerabilities or misconfigurations in websites and web applications Security professionals use them to locate potential entry points for attackers Example inurladmin can help locate unsecured admin login pages

Digital Forensics

Investigators can use dorks to search for evidence of criminal activity or locate specific digital traces related to their investigations For example forensic experts may use dorks to locate compromised data or logs that are publicly available Example filetypelog intextpassword might reveal log files containing sensitive information like login credentials

Competitive Analysis

Google Dorks can help gather intelligence on competitors by finding accidentally exposed files or sensitive data that can be used for market research or business strategy Example sitecompetitorcom filetypexls may uncover spreadsheets unintentionally exposed by a competitor

Common Google Dorking Queries

site

Limits search results to a specific website Example siteexamplecom limits results to the examplecom domain

filetype

Filters search results by file type Example filetypepdf returns only PDF files

intext and allintext

Searches for specific text within a webpages content Example intextpassword finds web pages containing the word password

intitle and allintitle

Searches for keywords in the title of a web page Example intitellogin will find pages with login in the title

inurl

Finds URLs that contain specific keywords Example inurladmin will return URLs with admin in them"""

# Remove punctuation
def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Get a list of words from the cleaned text
words = clean_text(text).split()
index = 0

# Function to speak the word
def speak_word(word):
    global index
    filename = f"word_{index}.mp3"  # Use index to create a unique filename
    tts = gTTS(text=word, lang='en')
    tts.save(filename)

    # Play the audio file using pygame
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Wait until the audio is done playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Cleanup after playing
    try:
        pygame.mixer.music.stop()  # Stop any playing music before deleting
        pygame.mixer.music.unload()  # Unload the music from the mixer
        os.remove(filename)  # Attempt to delete the file
        print(f"Deleted: {filename}")
    except Exception as e:
        print(f"Error removing file: {e}")

    index += 1  # Move to the next word

# Callback for key press events
def on_press(key):
    global index

    try:
        if key == keyboard.Key.esc:
            return False  # Stop the listener
        elif key == keyboard.Key.space:
            if index < len(words):
                speak_word(words[index])  # Speak the next word
            else:
                print("No more words to read.")  # Handle case with no more words
    except Exception as e:
        print(f"Error: {e}")

# Initialize pygame mixer
pygame.mixer.init()

# Print instructions
print("Press the spacebar to read the next word. Press 'Esc' to exit.")

# Start the listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop
try:
    while True:
        pass  # Just keep the script running
except KeyboardInterrupt:
    listener.stop()

listener.join()
