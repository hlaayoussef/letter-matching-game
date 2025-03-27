import streamlit as st
import random

# Game data with words and their starting letters
GAME_DATA = [
    {"word": "Apple", "image": "🍎", "letter": "A"},
    {"word": "Banana", "image": "🍌", "letter": "B"},
    {"word": "Cat", "image": "🐱", "letter": "C"},
    {"word": "Dog", "image": "🐶", "letter": "D"},
    {"word": "Elephant", "image": "🐘", "letter": "E"},
    {"word": "Fish", "image": "🐠", "letter": "F"},
    {"word": "Giraffe", "image": "🦒", "letter": "G"}
]

def reset_game():
    st.session_state.current_level = 0
    st.session_state.score = 0
    st.session_state.game_over = False

def letter_matching_game():
    # Initialize session state if not exists
    if 'current_level' not in st.session_state:
        reset_game()

    st.title("🧩 Letter Matching Game")
    
    # If game is not over
    if not st.session_state.get('game_over', False):
        # Get current game item
        current_item = GAME_DATA[st.session_state.current_level]
        
        # Display image and word
        st.write(f"### What letter does this word start with?")
        st.write(f"## {current_item['image']} {current_item['word']}")
        
        # Create columns for letter selection
        cols = st.columns(5)
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        random.shuffle(letters)
        
        # Letter selection buttons
        for i, letter in enumerate(letters[:5]):
            with cols[i]:
                if st.button(letter, key=f"letter_{letter}"):
                    # Check if selected letter is correct
                    if letter == current_item['letter']:
                        st.session_state.score += 10
                        
                        # Move to next level or end game
                        if st.session_state.current_level < len(GAME_DATA) - 1:
                            st.session_state.current_level += 1
                        else:
                            st.session_state.game_over = True
        
        # Display current score
        st.write(f"### Score: {st.session_state.score}")
    
    # Game over screen
    else:
        st.balloons()
        st.title("🎉 Great Job!")
        st.write(f"## Your Final Score: {st.session_state.score}")
        
        # Restart game
        if st.button("Play Again"):
            reset_game()

# Run the game
def main():
    letter_matching_game()

if __name__ == "__main__":
    main()
