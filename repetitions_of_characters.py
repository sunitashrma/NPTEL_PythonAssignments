


def repfree (s ) :
    i =1
    for a in s :
        x = s [ i : ]
        i = i + 1
    for b in x :
        if ( a==b):
            return ( False )
    return ( True )

