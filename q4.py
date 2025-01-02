def all_orderings(k):
    """
    Returns a list of all Boldon House orderings of size k.
    """
    remainingNumbers=[]
    for num in range(0,k):
        remainingNumbers.append(num)
    recursion([],remainingNumbers,[])

def recursion(currentsolution, remainingNumbers, totalSolutions):
    if isBoldenHouse(currentsolution):
        if len(remainingNumbers)==0:
            totalSolutions.append(currentsolution)
            print(totalSolutions)
        else:
            for num in remainingNumbers:
                currentsolution.append(num)
                remainingNumbers.remove(num)
                recursion(currentsolution)   



def ordering(k):
    """
    Returns a Boldon House ordering of size k.
    """
    R = []

def isBoldenHouse(R):
    D=[]
    k=len(R)
    for i in range(1,k):
        D.append((R[i]-R[i-1])%k)
    
    if isMonotoneIncreasing(D):
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

# simple test for all_orderings(k) only
# you do not have to return the Boldon House orderings in exactly the same order as they appear in this test case

assert(set(tuple(o) for o in all_orderings(3)) == 
       set(tuple(o) for o in [[0, 2, 1], [0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))