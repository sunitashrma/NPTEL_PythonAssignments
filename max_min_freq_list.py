def frequency (l):
    SET=set(l)
    LIST=list(SET)
    newl=list( )
    for a in LIST:
        newl.append(l.count(a))
        mi=min(newl)
        ma=max(newl)
        mil= [ ]
        mal= [ ]
    for b in range (len(newl)) :
        if newl[b] == mi:
           mil.append(LIST[b])
        if newl[b] == ma:
            mal.append(LIST[b])
    mil.sort( )
    mal.sort( )
    return( mil,mal )
            
