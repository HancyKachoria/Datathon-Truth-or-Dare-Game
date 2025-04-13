import streamlit as st
import random

# Set page config to ensure sidebar is visible
st.set_page_config(
    page_title="Truth or Dare Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded"
)


def game_settings():
    """Game settings function for intensity level and game type selection"""
    # Initialize session state for settings
    if 'intensity_level' not in st.session_state:
        st.session_state.intensity_level = 'mild'
    if 'game_type' not in st.session_state:
        st.session_state.game_type = 'truth'

    # Intensity Level Selection
    st.header("Select Intensity Level")
    intensity_options = {
        'mild': 'Mild',
        'funny': 'Funny',
        'spicy': 'Spicy',
        'drunk': 'Drunk'
    }

    # Create radio buttons for intensity
    intensity_level = st.radio(
        label="",
        options=list(intensity_options.keys()),
        format_func=lambda x: intensity_options[x],
        key="intensity_radio",
        horizontal=False,
        label_visibility="collapsed"
    )

    # Game Type Selection
    st.header("Choose Game Type")
    game_type = st.radio(
        label="",
        options=['truth', 'dare'],
        format_func=lambda x: x.capitalize(),
        key="game_type_radio",
        horizontal=False,
        label_visibility="collapsed"
    )

    # Update session state
    st.session_state.intensity_level = intensity_level
    st.session_state.game_type = game_type

    # Add some spacing
    st.write("")

    # Display current settings
    st.write(f"Current Settings:")
    st.write(f"- Intensity: {intensity_options[intensity_level]}")
    st.write(f"- Game Type: {game_type.capitalize()}")

    return {
        'intensity': intensity_level,
        'game_type': game_type
    }


# Custom CSS to style the radio buttons like checkboxes
st.markdown("""
<style>
    div[data-testid="stRadio"] > div {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    div[data-testid="stRadio"] > div > label {
        padding: 0.5rem;
        background-color: #F0F2F6;
        border-radius: 4px;
        cursor: pointer;
        color: #31333F;
    }
    div[data-testid="stRadio"] > div > label:hover {
        background-color: #E0E2E6;
    }
    div[data-testid="stRadio"] > div > label > div {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .stRadio > label {
        background-color: #F0F2F6;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }

    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    /* Apply custom fonts */
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stTextInput, .stSelectbox, .stButton {
        font-family: 'sans serif' !important;
    }
    
    /* Style the main title */
    h1 {
        color: #FF4B4B;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    /* Style the sidebar */
    .css-1d391kg {
        background-color: #F0F2F6;
        padding: 1.5rem;
        border-radius: 1rem;
    }
    
    /* Style buttons */
    .stButton>button {
        background-color: #FF4B4B;
        color: #FFFFFF;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: none;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #FF6B6B;
        transform: translateY(-2px);
    }
    
    /* Style the expander */
    .stExpander {
        background-color: #F0F2F6;
        border-radius: 1rem;
        padding: 1.5rem;
    }
    
    /* Style the toggle button */
    div[data-testid="stButton"] button[kind="secondary"] {
        background-color: #FF4B4B;
        color: #FFFFFF;
        font-weight: 600;
    }
    
    div[data-testid="stButton"] button[kind="secondary"]:hover {
        background-color: #FF6B6B;
    }
    
    /* Style the challenge text */
    .challenge-text {
        font-size: 1.2rem;
        line-height: 1.6;
        padding: 1.5rem;
        background-color: #F0F2F6;
        color: #31333F;
        border-radius: 1rem;
        margin: 1rem 0;
        border: 1px solid #E0E2E6;
    }
</style>
""", unsafe_allow_html=True)

# Truth questions categorized by intensity and gender
TRUTHS = {
    'mild': {
        'all': [
            "What's the most embarrassing song on your playlist?",
            "Have you ever pretended to like a gift you hated?",
            "What's the weirdest food combination you secretly enjoy?",
            "Have you ever laughed so hard you peed a little?",
            "What's your most ridiculous childhood fear?"
        ],
        'male': [
            "What's the most embarrassing thing you've done to impress a girl?",
            "Have you ever cried during a movie?",
            "What's your guilty pleasure TV show?"
        ],
        'female': [
            "What's the most embarrassing thing you've done to impress a guy?",
            "Have you ever faked being sick to get out of something?",
            "What's your guilty pleasure TV show?"
        ]
    },
    'funny': {
        'all': [
            "If you had to marry a kitchen appliance, which one would you choose and why?",
            "What's the most ridiculous lie you've ever told?",
            "Have you ever tried to impress someone and failed spectacularly?",
            "What's the weirdest thing you've ever eaten on a dare?",
            "If you could swap lives with any fictional character for a day, who would it be?"
        ],
        'male': [
            "What's the most ridiculous pickup line you've ever used?",
            "Have you ever been caught checking yourself out in a mirror?",
            "What's the most embarrassing thing you've done at the gym?"
        ],
        'female': [
            "What's the most ridiculous pickup line you've ever received?",
            "Have you ever been caught checking yourself out in a mirror?",
            "What's the most embarrassing thing you've done at the gym?"
        ]
    },
    'spicy': {
        'all': [
            "What's the most scandalous thing you've done that no one knows about?",
            "Have you ever had a crush on a friend's sibling?",
            "What's the most outrageous thing you've done to get someone's attention?",
            "Have you ever pretended to be someone else online?",
            "What's the most embarrassing thing you've done while drunk?"
        ],
        'male': [
            "What's the most embarrassing thing that's happened to you on a date?",
            "Have you ever been friend-zoned? Tell us about it.",
            "What's the most ridiculous thing you've done to get a girl's attention?"
        ],
        'female': [
            "What's the most embarrassing thing that's happened to you on a date?",
            "Have you ever friend-zoned someone? Tell us about it.",
            "What's the most ridiculous thing you've done to get a guy's attention?"
        ]
    },
    'drunk': {
        'all': [
            "What's the most embarrassing thing you've done while drunk?",
            "Have you ever woken up in a strange place after drinking?",
            "What's the weirdest thing you've eaten while drunk?",
            "Have you ever sent drunk texts you regretted?",
            "What's the most ridiculous thing you've done to get more alcohol?"
        ],
        'male': [
            "What's the most embarrassing thing you've done to impress a girl while drunk?",
            "Have you ever tried to fight someone while drunk?",
            "What's the most ridiculous thing you've done to prove you're not drunk?"
        ],
        'female': [
            "What's the most embarrassing thing you've done to impress a guy while drunk?",
            "Have you ever tried to fight someone while drunk?",
            "What's the most ridiculous thing you've done to prove you're not drunk?"
        ]
    }
}

# Dare challenges categorized by intensity and gender
DARES = {
    'mild': {
        'all': [
            "Do your best impression of a celebrity",
            "Sing the chorus of your favorite song in a funny voice",
            "Dance like nobody's watching for 30 seconds",
            "Tell a joke that makes everyone groan",
            "Do 10 jumping jacks while singing the alphabet"
        ],
        'male': [
            "Do your best impression of a female celebrity",
            "Let a girl give you a makeover",
            "Do a catwalk in high heels"
        ],
        'female': [
            "Do your best impression of a male celebrity",
            "Let a guy give you a makeover",
            "Do a bodybuilder pose"
        ]
    },
    'funny': {
        'all': [
            "Put on a blindfold and let someone feed you mystery food",
            "Do your best robot dance for a full minute",
            "Speak in a British accent for the next 3 rounds",
            "Wear your clothes inside out for the next 10 minutes",
            "Do an impression of each person in the group"
        ],
        'male': [
            "Let a girl style your hair however she wants",
            "Do a sexy dance for the group",
            "Wear lipstick for the next 3 rounds"
        ],
        'female': [
            "Let a guy style your hair however he wants",
            "Do a sexy dance for the group",
            "Wear a fake mustache for the next 3 rounds"
        ]
    },
    'spicy': {
        'all': [
            "Let someone give you a makeover with their eyes closed",
            "Do a seductive dance to a children's song",
            "Let someone draw on your face with eyeliner",
            "Do a runway walk in your most ridiculous outfit",
            "Give a lap dance to a chair"
        ],
        'male': [
            "Let a girl put makeup on you",
            "Do a strip tease (keep clothes on) to a slow song",
            "Let a girl dress you up in her clothes"
        ],
        'female': [
            "Let a guy put makeup on you",
            "Do a strip tease (keep clothes on) to a slow song",
            "Let a guy dress you up in his clothes"
        ]
    },
    'drunk': {
        'all': [
            "Do your best drunk impression",
            "Try to walk in a straight line with your eyes closed",
            "Do a beer pong shot blindfolded",
            "Try to say the alphabet backwards",
            "Do a shot of water pretending it's alcohol"
        ],
        'male': [
            "Let a girl give you a 'drunk makeover'",
            "Do your best drunk girl impression",
            "Try to put on lipstick while 'drunk'"
        ],
        'female': [
            "Let a guy give you a 'drunk makeover'",
            "Do your best drunk guy impression",
            "Try to shave your face while 'drunk'"
        ]
    }
}


def get_truth(intensity, gender):
    # Combine gender-specific and all-gender truths
    truths = TRUTHS[intensity]['all'] + TRUTHS[intensity][gender]
    return random.choice(truths)


def get_dare(intensity, gender):
    # Combine gender-specific and all-gender dares
    dares = DARES[intensity]['all'] + DARES[intensity][gender]
    return random.choice(dares)


# Initialize session state variables
if 'participants' not in st.session_state:
    st.session_state.participants = []
if 'show_participants' not in st.session_state:
    st.session_state.show_participants = True
if 'played_players' not in st.session_state:
    st.session_state.played_players = []
if 'failed_players' not in st.session_state:
    st.session_state.failed_players = {}
if 'current_challenge' not in st.session_state:
    st.session_state.current_challenge = None
if 'current_player' not in st.session_state:
    st.session_state.current_player = None
if 'should_regenerate' not in st.session_state:
    st.session_state.should_regenerate = False
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'regenerate_count' not in st.session_state:
    st.session_state.regenerate_count = 0

# Streamlit UI
st.title("🎲 Truth or Dare Game")
st.write("Add participants and choose your intensity level for some fun!")

# Game settings in sidebar
with st.sidebar:
    st.header("Game Settings")
    if st.session_state.participants:
        intensity = st.radio(
            "Select Intensity Level",
            ["mild", "funny", "spicy", "drunk"],
            index=0
        )

        game_type = st.radio(
            "Choose Game Type",
            ["Truth", "Dare"],
            index=0
        )
    else:
        st.info("👆 Add participants to enable game settings")

# Participant Management
with st.expander("👥 Manage Participants", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter participant name:")
    with col2:
        gender = st.selectbox(
            "Select gender:", ["male", "female"], key="gender_select")

    if st.button("Add Participant"):
        if name:
            st.session_state.participants.append(
                {"name": name, "gender": gender})
            st.success(f"Added {name}!")
        else:
            st.warning("Please enter a name!")

# Display current participants with collapse/expand feature
if st.session_state.participants:
    # Add a button to toggle participants list visibility
    if st.button("👁️ Toggle Participants List"):
        st.session_state.show_participants = not st.session_state.show_participants

    if st.session_state.show_participants:
        st.subheader("Current Participants:")
        for i, participant in enumerate(st.session_state.participants):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"{i+1}. {participant['name']}")
            with col2:
                st.write(f"({participant['gender']})")
            with col3:
                if st.button("Remove", key=f"remove_{i}"):
                    st.session_state.participants.pop(i)
                    st.rerun()
    else:
        st.write(
            f"👥 {len(st.session_state.participants)} participants in the game")

# Main content
if st.session_state.participants:
    # Game control button (Start/End Game)
    if not st.session_state.game_started:
        if st.button("🎲 Start Game!", key="start_game"):
            st.session_state.game_started = True
            st.rerun()
    else:
        if st.button("🛑 End Game", key="end_game", type="primary"):
            st.session_state.game_started = False
            st.session_state.current_challenge = None
            st.session_state.current_player = None
            st.session_state.should_regenerate = False
            # Keep the participants and their status
            st.success("🎮 Game ended! Click 'Start Game' to begin a new round!")
            st.rerun()

    # Game content
    if st.session_state.game_started:
        # Get available players (those who haven't played yet)
        available_players = [
            p for p in st.session_state.participants if p not in st.session_state.played_players]

        # Reset played players if all have had a turn
        if not available_players:
            st.session_state.played_players = []
            available_players = st.session_state.participants
            st.success("🎉 Round complete! Starting new round!")

        # Select or maintain current player
        if not st.session_state.current_player:
            current_player = random.choice(available_players)
            st.session_state.current_player = current_player
            if current_player not in st.session_state.played_players:
                st.session_state.played_players.append(current_player)
        else:
            current_player = st.session_state.current_player

        st.markdown(f"### 🎯 {current_player['name']}'s Turn!")

        # Check if player failed previous challenge
        is_penalty_round = current_player['name'] in st.session_state.failed_players
        if is_penalty_round:
            st.warning(
                f"⚠️ {current_player['name']} failed their last challenge! Penalty round activated!")

        if game_type == "Truth":
            if is_penalty_round:
                st.markdown(f"### 🔍 Truth Questions (Penalty Round):")
            else:
                st.markdown(f"### 🔍 Truth Question:")
        else:
            if is_penalty_round:
                st.markdown(f"### 💪 Dare Challenge (Penalty Round):")
            else:
                st.markdown(f"### 💪 Dare Challenge:")

        # Generate challenge based on current state
        if st.session_state.regenerate_count == 0:
            # Generate initial challenge
            if game_type == "Truth":
                if is_penalty_round:
                    challenge1 = get_truth(
                        intensity, current_player['gender'])
                    challenge2 = get_truth(
                        intensity, current_player['gender'])
                    current_challenge = f"1. {challenge1}\n\n2. {challenge2}"
                else:
                    current_challenge = get_truth(
                        intensity, current_player['gender'])
            else:
                if is_penalty_round:
                    current_challenge = get_dare(
                        "spicy", current_player['gender'])
                else:
                    current_challenge = get_dare(
                        intensity, current_player['gender'])
        else:
            # Generate new challenge for regeneration
            if game_type == "Truth":
                if is_penalty_round:
                    challenge1 = get_truth(
                        intensity, current_player['gender'])
                    challenge2 = get_truth(
                        intensity, current_player['gender'])
                    current_challenge = f"1. {challenge1}\n\n2. {challenge2}"
                else:
                    current_challenge = get_truth(
                        intensity, current_player['gender'])
            else:
                if is_penalty_round:
                    current_challenge = get_dare(
                        "spicy", current_player['gender'])
                else:
                    current_challenge = get_dare(
                        intensity, current_player['gender'])

        # Display current challenge
        st.markdown(f"""
        <div class="challenge-text" style="background-color: #1E1E1E; color: white; border: 1px solid #333;">
            {current_challenge}
        </div>
        """, unsafe_allow_html=True)

        # Store the current challenge
        st.session_state.current_challenge = current_challenge

        # Add regenerate challenge button
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("### 🔄 Want a different challenge?")
        with col2:
            if st.button("🔄 Regenerate", key=f"regenerate_{st.session_state.regenerate_count}"):
                st.session_state.regenerate_count += 1
                st.rerun()

        # Add some fun emojis based on intensity
        if intensity == "mild":
            st.markdown("😊 Keep it light and fun!")
        elif intensity == "funny":
            st.markdown("😂 Let's get silly!")
        elif intensity == "spicy":
            st.markdown("🔥 Spice it up!")
        else:
            st.markdown("🍻 Let's get tipsy!")

        # Host verification buttons
        st.markdown("### 🎭 Host Verification")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Completed", key="completed"):
                if current_player['name'] in st.session_state.failed_players:
                    del st.session_state.failed_players[current_player['name']]
                st.success(
                    f"🎉 {current_player['name']} completed their challenge!")
                # Reset for next player
                st.session_state.current_player = None
                st.session_state.current_challenge = None
                st.session_state.regenerate_count = 0
                st.rerun()
        with col2:
            if st.button("❌ Failed", key="failed"):
                st.session_state.failed_players[current_player['name']] = True
                st.error(
                    f"😱 {current_player['name']} failed their challenge! Penalty next turn!")
                # Reset for next player
                st.session_state.current_player = None
                st.session_state.current_challenge = None
                st.session_state.regenerate_count = 0
                st.rerun()

        # Show remaining players with emoji
        remaining_count = len(st.session_state.participants) - \
            len(st.session_state.played_players)
        if remaining_count > 0:
            remaining_players = [
                p['name'] for p in st.session_state.participants if p not in st.session_state.played_players]
            st.info(
                f"🎮 {remaining_count} players remaining in this round: {', '.join(remaining_players)}")
        else:
            st.success(
                "🔄 All players have played! Next turn will start a new round!")

        # Reset regenerate flag after displaying everything
        st.session_state.should_regenerate = False
    else:
        st.info("👆 Add some participants to start playing!")
else:
    st.info("👆 Add some participants to start playing!")
