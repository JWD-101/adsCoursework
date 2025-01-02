import copy
def all_orderings(k):
    """
    Returns a list of all Boldon House orderings of size k.
    """
    #creates a list of numbers that will be permuted to form the Bolden House orderings
    remainingNumbers=[]
    for num in range(0,k):
        remainingNumbers.append(num)
    return nextTrial([],remainingNumbers,[]) #begins the search with ALL possible numbers < k still to be checked

def nextTrial(currentSolution,remainingNumbers, orderings):
    if isBoldenHouseDifferences(currentSolution): #checks if the current solution is a bolden house
        if len(remainingNumbers)==0: #no numbers remaining to check = completed bolden house
            orderings.append(copy.deepcopy(currentSolution))
        else:
            for num in remainingNumbers: #for remaining numbers to check, transfers next number into current solution 
                newCurrentSolution = (copy.deepcopy(currentSolution)).append(num)
                newRemainingNumbers = copy.deepcopy(remainingNumbers).remove(num)
                nextTrial(newCurrentSolution,newRemainingNumbers,orderings) #repeats on the new current solution
    return orderings

def isBoldenHouseDifferences(currentSolution):
    #function checks if a set is a Bolden House (in terms of differences, not whether it is a permutation of natural numbers up to k)
    if len(currentSolution)<=2:
        #any set below length 3 is automatically a Bolden House
        return True
    else:
        #otherwise, create an array of the differences and check if it is monotonically increasing
        differences=[]
        length=len(currentSolution)

        for i in range(1,length):
            differences.append((currentSolution[i]-currentSolution[i-1])%length)

        return isMonotoneIncreasing(differences)
    
def isMonotoneIncreasing(D):
    #function checks if a set is monotonically increasing
    previous = D[0]

    for d in range(1,len(D)):
        if D[d] < previous:
            return False
        else:
            previous=d
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