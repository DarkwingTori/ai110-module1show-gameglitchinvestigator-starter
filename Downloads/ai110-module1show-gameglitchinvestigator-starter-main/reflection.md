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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

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

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
