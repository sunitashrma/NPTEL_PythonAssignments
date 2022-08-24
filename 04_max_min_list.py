import time
start_time = time.time()


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
l= [10,4,10,5,10,5,5]
#freq_list = frequency (l)
print(frequency(l))

end_time=time.time()-start_time
print(" ( %s ) sec"%end_time)
