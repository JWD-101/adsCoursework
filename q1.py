def compute_winner(history_A, history_B):
    """
    Compute the winner of a game, given the histories of player A and player B.

    Returns 'A' if player A wins, 'B' if player B wins, and 'D' if a tie. 
    """
    headCountA = 0
    highestCountA = 0
    for trial in history_A:
        if trial == "H":
            headCountA+=1
        else:
            headCountA=0
        if headCountA > highestCountA:
                highestCountA = headCountA

    headCountB = 0
    highestCountB = 0
    for trial in history_B:
        if trial == "H":
            headCountB+=1
        else:
            
            headCountB=0
        if headCountB > highestCountB:
                highestCountB = headCountB
    
    if highestCountA > highestCountB:
        return('A')
    elif highestCountB > highestCountA:
        return('B')
    else:
        return('D')

def encode(history):
    """
    Given a string representation of a game history, compresses the history.

    Returns a string with the compressed representation of a game history 
    described in the question.
    """

def decode(compressed_history):
    """
    Given a compressed string representation of a game history, 
    uncompress the history.

    Returns a string with the uncompressed representation of a game history 
    described in the question
    """

def compute_winner_compressed(compressed_history_A, compressed_history_B):
    """
    Compute the winner of a game, given the compressed histories of player A
    and player B.

    Returns 'A' if player A wins, 'B' if player B wins, and 'D' if a tie. 
    """

# simple tests
assert(compute_winner('HHH', 'TTT') == 'A')
assert(compute_winner('THTH', 'THHT') == 'B')
assert(compute_winner('HH', 'HH') == 'D')

assert(encode('HTTH') == 'H1T2H1')
assert(encode('TTTT') == 'T4')

assert(decode('T2') == 'TT')
assert(decode('T1H2T1') == 'THHT')

assert(compute_winner_compressed('H3', 'T3') == 'A')
assert(compute_winner_compressed('T1H1T1H1', 'T1H2T1') == 'B')
assert(compute_winner_compressed('T2', 'T2') == 'D')