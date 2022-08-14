
def leftrotate (mat) :
    q=[ ]
    for i in range (len(mat)) :
        s=[ ]
        for j in range (len(mat[i] )) :
            s.append(mat[j] [len(mat)-1-i])
        q.append(s)
    return(q)
  