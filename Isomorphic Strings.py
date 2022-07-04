s = "egg"
#print(set(s))
t = "add"
map_s = {}
if (len(set(s)) != len(set(t))):
    print("Not Isomorphic Strings")
    print(set(s))
for i in range(len(s)):
    if s[i] not in map_s :
        print ("Value of t:",t[i])
        print ("Value of S:",s[i])
        map_s[(s[i])]= t[i]
        print ("Value of Map-s:",map_s[(s[i])])
        print ("Value of map:",map_s)
        # for i in range(len(s)):
        # print( map_s[(s[i])], t[i] )
        if map_s[(s[i])] != t[i]:
            #print("Not Isomorphic Strings")
            print(" ")
    #print("Not Isomorphic Strings")
    print(" ")