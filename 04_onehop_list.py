def onehop (l) :
    ans=list()
    l.sort()
    for x in range (len(l)):
        for y in range (len(l)):
            if l[x] != l[y]:
                if l[x][1] == l[y][0]:
                    q= l[x][0]
                    w= l[y][1]
                    if q != w:
                        t = [q,w]
                        t= tuple(t)
                        if t not in ans :
                           ans.append (tuple (t))
    ans.sort()
    return (ans)
