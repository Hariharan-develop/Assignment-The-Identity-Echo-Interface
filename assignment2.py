import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

st.title("THE MULTIVERSE OF CHATBOTS")

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Categories
category = st.selectbox(
    "Choose a Category",
    [
        "Technology",
        "Tamil Cinema",
        "Sports",
        "Education",
        "Comedy",
        "Superheroes",
        "History",
        "Gaming",
        "Others"
    ]
)

# Characters based on category
if category == "Technology":
    people = [
        "Expert Hacker",
        "AI Professor",
        "Python Developer",
        "Cyber Security Expert",
        "Software Engineer"
    ]

elif category == "Tamil Cinema":
    people = [
        "Rajinikanth",
        "Vijay",
        "Ajith",
        "Kamal Haasan",
        "Vadivelu",
        "Goundamani",
        "Santhanam"
    ]

elif category == "Sports":
    people = [
        "Cristiano Ronaldo Fan",
        "Lionel Messi Fan",
        "Angry Ravi Shastri",
        "MS Dhoni",
        "Virat Kohli"
    ]

elif category == "Education":
    people = [
        "Strict Professor",
        "Friendly Teacher",
        "UPSC Mentor",
        "Exam Motivator"
    ]

elif category == "Comedy":
    people = [
        "Stand-up Comedian",
        "Sarcastic Friend",
        "Meme Lord",
        "Crazy Best Friend"
    ]

elif category == "Superheroes":
    people = [
        "Batman",
        "Spider-Man",
        "Iron Man",
        "Captain America",
        "Doctor Strange"
    ]

elif category == "History":
    people = [
        "Napoleon",
        "Julius Caesar",
        "Chanakya"
    ]

elif category == "Gaming":
    people = [
        "Pro Gamer",
        "Minecraft Expert",
        "PUBG Champion"
    ]

else:
    people = [
        "Relationship Coach",
        "Business Mentor",
        "Gym Trainer",
        "Yoga Master",
        "Master Chef",
        "Travel Guide",
        "Motivational Speaker",
        "Music Teacher",
        "Photographer",
        "Artist"
    ]

personality = st.selectbox(
    "Who do you want to talk to?",
    people
)

user_message = st.text_input("Say something:")

if st.button("SEND"):

    if user_message:

        prompt = f"""
You are acting as {personality}.

Stay completely in character.
Never tell the user you are an AI.
Reply exactly as {personality} would.

User: {user_message}
"""

        with st.spinner("Connecting to the multiverse..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Message received!")
        st.write(response.text)

    else:
        st.warning("Please type a message first.")