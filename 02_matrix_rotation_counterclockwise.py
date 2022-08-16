
def leftrotate (m) :
    q=[ ]
    for i in range (len(m)) :
        s=[ ]
        for j in range (len(m[i] )) :
            s.append(m[j] [len(m)-1-i])
        q.append(s)
    return(q)
  
