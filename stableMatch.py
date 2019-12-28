def stableMatch(aPref, bPref):
    freeA = [i for i in range(0, len(aPref))]
    #all free to begin with
    freeAmatch = [0 for i in range(0,len(aPref))]
    freeB = [i for i in range(0, len(bPref))]
    pairs = []
    while(len(freeA)>0):
        i = freeA[0]
        if freeAmatch[i]==len(aPref[i]):
            freeA.remove(i)
        else:
            topAmatch= aPref[i][freeAmatch[i]]
            foundMatch = True
            if topAmatch in freeB:
                #aPref[i] is preferences of a
                #aPref[i][freeAmatch[i]] is B, or the next best partner of a according to preferences
                pairs.append([i,topAmatch])
                #Add the pair i and i's preference
                freeB.remove(topAmatch)
                freeA.remove(i)
            else:
                for pair in pairs:
                    if topAmatch==pair[1]:
                        #if there is a pairing with this partner
                        #aPref[i] is the preferences of a
                        #aPref[i][freeAmatch[i]] is B, or the next best partner of a according to preferences
                        #pair[1] is 
                        if bPref[pair[1]].index(pair[0]) > bPref[pair[1]].index(i):
                            #freeB[pair[1]] is the current partners preferences
                            #.index(pair[0]) is ranking of current partner, a'
                            #.index(i) is ranking of proposed partner, a
                            #then if B prefers a
                            freeA.append(pair[0]) #a' will be free soon
                            pairs.remove(pair) #a' pair will be removed
                            pairs.append([i,topAmatch]) #add pair [i, a]
                            freeA.remove(i) #remove A from being free
            freeAmatch[i] = freeAmatch[i]+1
            #regardless of if the pairings change, go to the next preference      
    return pairs
pref1 = [[0,1],[0,0]]
# A | D, C
# B | C, C
pref2 = [[1,0],[1,0]]
# C | B, A
# D | B, A
print(stableMatch(pref1,pref2))
    
