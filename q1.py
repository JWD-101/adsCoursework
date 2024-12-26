def compute_winner(history_A, history_B):
    headRunsA = set(history_A.split("T"))
    headRunsB = set(history_B.split("T"))
    highestCountA=0
    highestCountB=0
    for run in headRunsA:
        if len(run)>highestCountA:
            highestCountA=len(run)
    for run in headRunsB:
        if len(run)>highestCountB:
            highestCountB=len(run)
    
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
    encodedHistory = ""
    previousTrial = history[0]
    currentTrialCount = 1

    for trial in history[1::]:
        if trial == previousTrial:
            currentTrialCount += 1
        else:
            encodedHistory+=previousTrial
            encodedHistory+=str(currentTrialCount)
            currentTrialCount = 1
        previousTrial = trial

    encodedHistory+=previousTrial
    encodedHistory+=str(currentTrialCount)
    return(encodedHistory)

def decode(compressed_history):
    trial = compressed_history[0:2:]
    compressed_history = compressed_history[2::]
    if len(compressed_history)!=0:
        decodedHistory = trial[0]*int(trial[1])+decode(compressed_history)
        return(decodedHistory)
    else:
        decodedHistory = trial[0]*int(trial[1])
        return(decodedHistory)

def compute_winner_compressed(compressed_history_A, compressed_history_B):
    """
    Compute the winner of a game, given the compressed histories of player A
    and player B.

    Returns 'A' if player A wins, 'B' if player B wins, and 'D' if a tie. 
    """
    highestCountA = 0
    for trial in range(0,len(compressed_history_A),2):
        if compressed_history_A[trial] == "H":
            if int(compressed_history_A[trial+1])>highestCountA:
                highestCountA=int(compressed_history_A[trial+1])
    highestCountB = 0
    for trial in range(0,len(compressed_history_B),2):
        if compressed_history_B[trial] == "H":
            if int(compressed_history_B[trial+1])>highestCountB:
                highestCountB=int(compressed_history_B[trial+1])
    if highestCountA > highestCountB:
        return('A')
    elif highestCountB > highestCountA:
        return('B')
    else:
        return('D')


# simple tests
assert(compute_winner('HHH', 'TTT') == 'A')
assert(compute_winner('THTH', 'THHT') == 'B')
assert(compute_winner('HH', 'HH') == 'D')
assert(compute_winner('HHHTTH', 'TTTHH') == 'A')
assert(compute_winner('HHHHTHTHHHH', 'THHHHHTHH') == 'B')
assert(compute_winner('HHTTHHH', 'HHHTTH') == 'D')

assert(encode('HTTH') == 'H1T2H1')
assert(encode('TTTT') == 'T4')

assert(decode('T2') == 'TT')
assert(decode('T1H2T1') == 'THHT')
assert(decode('T2H4') == 'TTHHHH')
assert(decode('H2T1') == 'HHT')
assert(decode('H5T2H2') == 'HHHHHTTHH')
assert(decode('T2H2T1H1T1H1') == 'TTHHTHTH')

assert(compute_winner_compressed('H3', 'T3') == 'A')
assert(compute_winner_compressed('T1H1T1H1', 'T1H2T1') == 'B')
assert(compute_winner_compressed('T2', 'T2') == 'D')