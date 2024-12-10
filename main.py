import streamlit as st
from numpy import random

# Initialize game state
if "hiddenNumber" not in st.session_state:
    st.session_state.hiddenNumber = random.randint(1, 11)  # Generate random number once
if "gameOver" not in st.session_state:
    st.session_state.gameOver = False
if "message" not in st.session_state:
    st.session_state.message = ""

# Display game title and instructions
st.title("Guess the Number Game!")
st.write("I'm thinking of a number between 1 and 10. Can you guess what it is?")

# Take user input
if not st.session_state.gameOver:
    userGuess = st.text_input("Enter your guess:")

    if userGuess:
        try:
            userGuess = int(userGuess)  # Convert input to an integer
            if userGuess < 1 or userGuess > 10:  # Check if the guess is out of range
                st.session_state.message = "Invalid guess! Please enter a number between 1 and 10."
            elif userGuess > st.session_state.hiddenNumber:
                st.session_state.message = "Your guess is too high!"
            elif userGuess < st.session_state.hiddenNumber:
                st.session_state.message = "Your guess is too low!"
            elif userGuess == st.session_state.hiddenNumber:
                st.session_state.message = f"You guessed correctly! The number was {st.session_state.hiddenNumber}."
                st.session_state.gameOver = True
        except ValueError:
            st.session_state.message = "Invalid input! Please enter a valid number."

# Display message to the user
st.write(st.session_state.message)

# End the game
if st.session_state.gameOver:
    st.write("Game Over! Reload the page to play again.")

# Restart the game button
if st.button("Restart Game"):
    st.session_state.hiddenNumber = random.randint(1, 11)
    st.session_state.gameOver = False
    st.session_state.message = ""
