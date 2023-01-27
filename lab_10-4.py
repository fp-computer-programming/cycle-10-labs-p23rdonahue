#author: RED 1/23/23

def indexed_names(list):
    newlst=[] #new empty list
    for i, v in enumerate(list):
        newlst.append(f'{i}: {v}') #adding to the list
    print(newlst)

indexed_names(["John","Jane","Bob"]) #test cases
indexed_names(["Vishnu","Joe", "Kevin", "Jack"])
