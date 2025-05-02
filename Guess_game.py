import random
import streamlit as st

class NumberGuessGame:
    def __init__(self, start=1, end=10):
        """
        Initialize the game with a range of numbers.
        """
        self.start = start
        self.end = end
        self.target_number = random.randint(self.start, self.end)

    def reset_game(self):
        """
        Reset the game by generating a new target number.
        """
        self.target_number = random.randint(self.start, self.end)

# Create a Streamlit app
st.title("Number Guess Game")
st.write("Guess the number between 1 and 10!")

# Initialize game instance
if "game" not in st.session_state:
    st.session_state.game = NumberGuessGame()

game = st.session_state.game

# Input form for the user's guess
guess = st.number_input("Enter your guess:", min_value=game.start, max_value=game.end, step=1, key="guess_input")

# Button to check the guess
if st.button("Check Guess"):
    if guess < game.target_number:
        st.warning("Too low! Try again.")
    elif guess > game.target_number:
        st.warning("Too high! Try again.")
    else:
        st.success("Congratulations! You guessed the right number!")
        st.balloons()

# Button to reset the game
if st.button("Reset Game"):
    game.reset_game()
    st.success("Game has been reset. A new number has been generated!")
