from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_corrected():
    """Verify 'Too High' returns 'Go LOWER!' message (bug fix)"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_too_low_message_corrected():
    """Verify 'Too Low' returns 'Go HIGHER!' message (bug fix)"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_win_message():
    """Verify correct guess returns full message"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"
