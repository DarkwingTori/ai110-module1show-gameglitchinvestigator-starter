# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- 
- When it tells me to go lower it wants me to go higher 
- When I click new game the game does not restart 
- I noticed normal has a range from 1 to 100 but hard has a range from 1 to 50


## 2. How did you use AI as a teammate?

**AI tools used:** GitHub Copilot in Agent mode for autonomous code refactoring, and inline suggestions for identifying bugs and writing tests.

**Example of correct AI suggestion:** When you asked to refactor logic into `logic_utils.py`, Copilot Agent mode autonomously moved the four functions while preserving the bug fixes (reversed messages). I verified this by running all 6 pytest tests and confirming they passed. The refactoring worked perfectly and actually improved code organization by separating business logic from UI.

**Example that needed correction:** The original starter tests expected only an outcome string (e.g., `assert result == "Win"`), but `check_guess()` actually returns a tuple with both outcome and message. Copilot's initial test designs didn't account for this return type. I caught this when the first three tests failed, then updated them to unpack both values. This taught me that AI suggestions need validation against actual function signatures and return types before acceptance.

## 3. Debugging and testing your fixes

**Testing approach:**
- Created three new pytest tests in `tests/test_game_logic.py` specifically targeting the reversed feedback bug
- Tests verified:
  - `test_too_high_message_corrected()`: Confirmed guess of 60 vs secret 50 returns "Too High" outcome with "📉 Go LOWER!" message
  - `test_too_low_message_corrected()`: Confirmed guess of 40 vs secret 50 returns "Too Low" outcome with "📈 Go HIGHER!" message  
  - `test_win_message()`: Verified correct guess returns full outcome + message tuple

**How I verified the fixes:**
1. Ran `python3 -m pytest tests/test_game_logic.py -v` and confirmed all 6 tests pass (3 new + 3 existing)
2. The corrected messages in the pytest output showed the reversed feedback was fixed
3. Updated existing starter tests to unpack the tuple return value from `check_guess()`, showing the refactoring worked correctly

**AI collaboration on testing:** Copilot suggested simple, focused tests that directly verify the specific bug fixes rather than complex integration tests. This made it easy to validate that each fix worked in isolation.

## 4. What did you learn about Streamlit and state?

**Why the secret number kept changing:** In the original app, every time you submitted a guess, Streamlit would rerun the entire script from top to bottom. If the secret number wasn't stored in `st.session_state`, a new random number would be generated on each rerun. The app initialized the secret once with `if "secret" not in st.session_state`, but the "New Game" button wasn't properly resetting all state variables, so the game logic got confused.

**Explaining Streamlit reruns and session state to a friend:** Streamlit is like a magic whiteboard that reruns your whole script whenever the user interacts with it (clicks a button, enters text, changes a slider). Session state is like the app's memory—it's a special dictionary that survives across reruns and stays with that specific user's session. Without session state, all your variables reset every rerun. With it, you can "remember" important things like the secret number, attempt count, or game status.

**What finally gave the game a stable secret number:** I fixed the "New Game" button handler to completely reset ALL session state variables (attempts, secret, status, history, score) instead of just a few. I also changed the random number generation to use the actual range variables (`low` and `high`) from the difficulty setting instead of hardcoded "1 to 100". This, combined with the initial `if "secret" not in st.session_state` check, ensured the secret stayed stable throughout the game and only changed when "New Game" was clicked.

## 5. Looking ahead: your developer habits

**One habit to reuse:** Writing focused unit tests that target specific bugs rather than broad integration tests. The three new pytest tests (`test_too_high_message_corrected`, `test_too_low_message_corrected`, `test_win_message`) were simple and directly proved the reversed feedback bug was fixed. This approach is much clearer than trying to test the entire Streamlit UI, and it makes debugging faster when tests fail.

**What I'd do differently with AI next time:** I'd spend more time understanding function signatures, return types, and existing test patterns before asking AI to generate code. The issue with starter tests not unpacking the tuple return value could have been avoided if we'd reviewed the actual `check_guess()` implementation upfront. Reading the code first saves time compared to debugging failed tests later.

**How this project changed your thinking about AI-generated code:** AI-generated code is powerful for scaffolding and refactoring, but it's not "fire and forget"—it needs careful review for correctness, edge cases, and consistency with the codebase. The reversed feedback bug was your human observation, but the fix and refactoring greatly benefited from AI collaboration and structured testing. AI works best as a teammate that you verify and guide, not as a replacement for critical thinking.
