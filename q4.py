import copy
def all_orderings(k):
    """
    Returns a list of all Boldon House orderings of size k.
    """
    remainingNumbers=[]
    for num in range(0,k):
        remainingNumbers.append(num)
    return nextTrial([],remainingNumbers,[])

def nextTrial(currentSolution,remainingNumbers, orderings):
    print(currentSolution)
    if isBoldenHouse(currentSolution):
        if len(remainingNumbers)==0:
            orderings.append(copy.deepcopy(currentSolution))
        else:
            for num in remainingNumbers:
                nextSolution = copy.deepcopy(currentSolution)
                newRemainingNumbers = copy.deepcopy(remainingNumbers)
                nextSolution.append(num)
                newRemainingNumbers.remove(num)
                nextTrial(nextSolution,newRemainingNumbers,orderings)
    return orderings

def isBoldenHouse(currentSolution):
    if len(currentSolution)<=2:
        return True
    else:
        differences=[]
        k=len(currentSolution)
        for i in range(1,k):
            differences.append((currentSolution[i]-currentSolution[i-1])%k)

        if isMonotoneIncreasing(differences):
            return True
        else:
            return False
    
def isMonotoneIncreasing(D):
    previousDifference = D[0]
    for difference in range(1,len(D)):
        if D[difference] < previousDifference:
            return False
        else:
            previousDifference=difference
    return True


def ordering(k):
    """
    Returns a Boldon House ordering of size k.
    """
# simple test for all_orderings(k) only
# you do not have to return the Boldon House orderings in exactly the same order as they appear in this test case

assert(set(tuple(o) for o in all_orderings(3)) == 
       set(tuple(o) for o in [[0, 2, 1], [0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))
print(all_orderings(4))