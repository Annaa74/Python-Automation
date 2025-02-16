import streamlit as st
import random

# Single responsibility functions (Valentine's Theme)

def generate_valentine_greeting(recipient_name):
    greetings = [
        f"Happy Valentine's Day, {recipient_name}! ❤️",
        f"Sending warm Valentine's Day wishes to you, {recipient_name}! 💕",
        f"May your Valentine's Day be filled with joy, {recipient_name}! 💖",
        f"Happy Valentine's Day, {recipient_name}! You're amazing! ✨",
        f"Wishing you a day filled with love and happiness, {recipient_name}! 💝"
    ]
    return random.choice(greetings)

def add_premium_message(greeting):
    premium_messages = [
        "You're extra special! 🌟",
        "A special Valentine's Day treat just for you! 🎁",
        "Enjoy this exclusive Valentine's Day message! 💎"
    ]
    return greeting + " " + random.choice(premium_messages)

def generate_discount_code():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    discount_code = ''.join(random.choice(characters) for i in range(8))
    return discount_code

def add_regular_message(greeting):
    regular_messages = [
        "Have a lovely day! 😊",
        "Wishing you all the best on Valentine's Day! 😄",
        "Enjoy the day! 🎉"
    ]
    return greeting + " " + random.choice(regular_messages)

def display_valentine_message(message, color, emoji):
    st.markdown(f"<h1 style='color: {color}; text-align: center;'>{emoji} {message} {emoji}</h1>", unsafe_allow_html=True)


def send_email(recipient_name, subject, message): # Simulated email
  print(f"Sending email to {recipient_name} with subject '{subject}':\n{message}")

def record_valentine_greeting(recipient_name): #Simulated Database Record
  print(f"Valentine's greeting recorded for {recipient_name} in the database (simulated).")



# Streamlit app
st.title("Happy Valentine's Day, My LinkedIn Connections! ❤️")

greeting_options = [
    "To all my amazing LinkedIn connections – Happy Valentine's Day!",
    "Sending warm Valentine's Day wishes to my incredible LinkedIn network!",
    "Happy Valentine's Day to the best connections a person could ask for!",
    "Cheers to celebrating Valentine's Day with my fantastic LinkedIn community!",
    "Happy Valentine's Day! So grateful for all of you on LinkedIn!"
]

chosen_greeting = random.choice(greeting_options)

st.markdown(f"<h2 style='color: #FF69B4; text-align: center;'>{chosen_greeting}</h2>", unsafe_allow_html=True)  # Pink color


general_messages = [
    "May your day be filled with love, laughter, and connections that truly matter.",
    "Wishing you a Valentine's Day as strong and valuable as our LinkedIn network!",
    "Let's celebrate the power of connection, both personally and professionally.",
    "Here's to building strong relationships and celebrating together!",
    "Happy Valentine's Day! Let's continue to support and inspire each other."
]
chosen_general_message = random.choice(general_messages)

colors = ["#FF69B4", "#FF1493", "#FF6347", "#FFA07A", "#FFD700"]  # Vibrant colors
emojis = ["❤️", "💕", "💖", "✨", "💝", "😊", "🎉", "🎁", "💎", "🌟", "🤝", "🚀"]
chosen_color = random.choice(colors)
chosen_emoji = random.choice(emojis)

display_valentine_message(chosen_general_message, chosen_color, chosen_emoji)  # Call the function


st.subheader("Share Your Valentine's Day Vibe!")
vibe = st.text_area("What's your favorite thing about Valentine's Day (or just about connecting with others)?")

if st.button("Share"):
    if vibe:
        st.write(f"\"{vibe}\" - That's a great vibe! Happy Valentine's Day!")
    else:
        st.write("Happy Valentine's Day!  Hope you have a wonderful day! ❤️")


# Surprising animations! (Choose one or a combination)

# 1. Confetti (Snow)
st.snow()  # Snow effect

# 2. Love Meter (Progress Bar)
love_meter = st.progress(0)
for i in range(101):
    love_meter.progress(i)

# 3. Success Alert (Virtual Hug)
if st.button("Send a Virtual Hug"):
    st.success("Virtual hug sent! 🤗")

# 4. Balloons!
st.balloons()
