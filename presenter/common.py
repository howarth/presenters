
def stim_ind(stim_seq):
    next_unique = 0;
    stim_to_ind = dict();
    ind_seq = len(stim_seq)*[-1]

    for i,c in enumerate(stim_seq):
        if c in stim_to_ind:
            ind_seq[i] = stim_to_ind[c]
        else:
            stim_to_ind[c] = next_unique
            ind_seq[i] = next_unique    
            next_unique += 1

    return stim_to_ind, ind_seq
