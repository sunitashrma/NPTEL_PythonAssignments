
def frequency (l):
    unique_l=list(set(l))
    freq_list=[l.count(x) for x in unique_l]
    min_freq_list=[unique_l[x] for x in range (len(freq_list)) if freq_list[x] == min (freq_list)]
    max_freq_list=[unique_l[x] for x in range (len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return(min_freq_list,max_freq_list)
                  


