
def frequency (l):
    SET=set(l)
    LIST=list(SET)
    newl=list( )
    for a in LIST:
        newl.append(l.count(a))
    MIN=min(newl)
    MAX=max(newl)
    min_list= [ ]
    max_list= [ ]
    for b in range (len(newl)) :
        if newl[b] == MIN:
           min_list.append(LIST[b])
        if newl[b] == MAX:
            max_list.append(LIST[b])

    min_list.sort( )
    max_list.sort( )
    return (min_list,max_list)
