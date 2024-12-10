import streamlit as st
from numpy import random

# Function to reset the game
def restart_game():
    st.session_state.hiddenNumber = random.randint(1, 11)
    st.session_state.gameOver = False
    st.session_state.message = ""
    st.session_state.userGuess = ""

# Initialize game state
if "hiddenNumber" not in st.session_state:
    st.session_state.hiddenNumber = random.randint(1, 11)
if "gameOver" not in st.session_state:
    st.session_state.gameOver = False
if "message" not in st.session_state:
    st.session_state.message = ""
if "userGuess" not in st.session_state:
    st.session_state.userGuess = ""

# Display game title and instructions
st.title("Guess the Number Game!")
st.write("I'm thinking of a number between 1 and 10. Can you guess what it is?")

# Game logic
if not st.session_state.gameOver:
    # Show the input box if the game is not over
    userGuess = st.text_input("Enter your guess:", value=st.session_state.userGuess)

    if userGuess:  # Process only if user has entered a guess
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
                st.session_state.gameOver = True  # Mark the game as over
        except ValueError:
            st.session_state.message = "Invalid input! Please enter a valid number."
    # Update the session state to persist the user's guess
    st.session_state.userGuess = userGuess

# Display message to the user
st.write(st.session_state.message)

# Show "Restart Game" button when the game is over
if st.session_state.gameOver:
    # Hide the input box when the game is over
    st.write("Press the button below to restart the game.")
    if st.button("Restart Game"):
        restart_game()
