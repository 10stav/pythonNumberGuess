import streamlit as st
from numpy import random

# Generate a random number between 1 and 10
hiddenNumber = random.randint(1, 11)

# Initialize game state
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
            if userGuess > hiddenNumber:
                st.session_state.message = "Your guess is too high!"
            elif userGuess < hiddenNumber:
                st.session_state.message = "Your guess is too low!"
            elif userGuess == hiddenNumber:
                st.session_state.message = f"You guessed correctly! The number was {hiddenNumber}."
                st.session_state.gameOver = True
        except ValueError:
            st.session_state.message = "Please enter a valid number!"

# Display message to the user
st.write(st.session_state.message)

# End the game
if st.session_state.gameOver:
    st.write("Game Over! Reload the page to play again.")
