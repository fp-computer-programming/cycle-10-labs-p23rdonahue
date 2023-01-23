#author: RED 1/23/23

def indexed_names(list):
    newlst=[]
    for i, v in enumerate(list):
        newlst.append(f'{i}: {v}')
    print(newlst)

indexed_names(["John","Jane","Bob"])
indexed_names(["Vishnu","Joe", "Kevin", "Jack"])
