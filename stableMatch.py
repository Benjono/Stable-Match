def stableMatch(aPref, bPref):
    #all free to begin with
    freeInA = [i for i in range(0, len(aPref))]
    freeInAmatch = [0 for i in range(0,len(aPref))]
    freeInB = [i for i in range(0, len(bPref))]
    pairs = []
    while(len(freeInA)>0):
        i = freeInA[0]
        #If no more matches can be made for them
        if freeInAmatch[i]==len(aPref[i]): 
            #Remove from those that are free
            freeInA.remove(i) 
        else:
            #What is their top match
            topAmatch = aPref[i][freeInAmatch[i]]
            #Is their top match free?
            if topAmatch in freeInB:
                #Then pair them
                pairs.append([i,topAmatch])
                #Both aren't free
                freeInB.remove(topAmatch)
                freeInA.remove(i)
            else:
                #For each pair
                for pair in pairs:
                    #And there is a pairing where it is preferential
                    #for A
                    if topAmatch==pair[1]:
                        #If it is preferential for B also
                        if bPref[pair[1]].index(pair[0]) > bPref[pair[1]].index(i):
                            #change pairing
                            freeInA.append(pair[0]) 
                            pairs.remove(pair)
                            pairs.append([i,topAmatch]) 
                            freeInA.remove(i)
            freeInAmatch[i] = freeInAmatch[i]+1
            #regardless of if the pairings change, go to the next preference      
    return pairs

def stablePreWork(leftNames, rightNames):
    # Convert labels for the user to numbers for the backend.
    leftnamesToNums = {}
    rightnamesToNums = {}
    numNameAssign = 0
    for key in leftNames:
        leftnamesToNums[key] = numNameAssign
        numNameAssign += 1
    numNameAssign = 0
    for key in rightNames:
        rightnamesToNums[key] = numNameAssign
        numNameAssign += 1
    leftPref = [[rightnamesToNums[pref] for pref in leftNames[i]] for i in leftNames.keys()]
    rightPref = [[leftnamesToNums[pref] for pref in rightNames[i]] for i in rightNames.keys()]
    
    matches = stableMatch(leftPref, rightPref)
    
    #Convert backend numbers back to labels
    for i in range(len(matches)):
        matches[i][0] = list(leftnamesToNums.keys())[list(leftnamesToNums.values()).index(matches[i][0])]
        matches[i][1] = list(rightnamesToNums.keys())[list(rightnamesToNums.values()).index(matches[i][1])]
    return matches

pref1 = [[0,1],[0,0]]
# A | D, C
# B | C, C
pref2 = [[1,0],[1,0]]
# C | B, A
# D | B, A

preferences1 = {"Adam" : ["Beth", "Amy", "Diane", "Ellen", "Cara"], 
                "Bill" : ["Diane", "Beth", "Amy", "Cara", "Ellen"], 
                "Carl": ["Beth", "Ellen", "Cara", "Diane", "Amy"],
                "Dan": ["Amy", "Diane", "Cara", "Beth", "Ellen"],
                "Eric": ["Beth", "Diane", "Amy", "Ellen", "Cara"]}
preferences2 = {"Amy": ["Eric", "Adam", "Bill","Dan","Carl"],
                "Beth": ["Carl", "Bill", "Dan", "Adam", "Eric"],
                "Cara": ["Bill", "Carl", "Dan", "Eric", "Adam"],
                "Diane": ["Adam", "Eric", "Dan", "Carl", "Bill"],
                "Ellen": ["Dan", "Bill", "Eric", "Carl", "Adam"]}
print(stableMatch(pref1,pref2))
print(stablePreWork(preferences2, preferences1))
