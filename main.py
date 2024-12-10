import streamlit as st
from numpy import random

# Function to reset the game
def restart_game():
    st.session_state.hiddenNumber = random.randint(1, 11)
    st.session_state.gameOver = False
    st.session_state.message = ""
    st.session_state.guess = ""

# Initialize game state
if "hiddenNumber" not in st.session_state:
    st.session_state.hiddenNumber = random.randint(1, 11)
if "gameOver" not in st.session_state:
    st.session_state.gameOver = False
if "message" not in st.session_state:
    st.session_state.message = ""
if "guess" not in st.session_state:
    st.session_state.guess = ""

# Display game title
st.title("Guess the Number Game!")

if not st.session_state.gameOver:
    # Prompt user to guess if the game is ongoing
    st.write("I'm thinking of a number between 1 and 10. Can you guess what it is?")
    guess = st.text_input("Enter your guess:")

    if guess:
        try:
            guess = int(guess)  # Convert input to an integer
            if guess < 1 or guess > 10:
                st.session_state.message = "Invalid guess! Please enter a number between 1 and 10."
            elif guess > st.session_state.hiddenNumber:
                st.session_state.message = "Your guess is too high!"
            elif guess < st.session_state.hiddenNumber:
                st.session_state.message = "Your guess is too low!"
            else:
                st.session_state.message = f"🎉 You guessed correctly! The number was {st.session_state.hiddenNumber}."
                st.session_state.gameOver = True  # End the game
        except ValueError:
            st.session_state.message = "Invalid input! Please enter a valid number."

# Display message
st.write(st.session_state.message)

# If the game is over, ask if the user wants to play again
if st.session_state.gameOver:
    st.write("Would you like to play again?")
    if st.button("Play Again"):
        restart_game()
