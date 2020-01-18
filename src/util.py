def field_first_to_row(d):
    l = []
    k = d.keys()
    i = 0
    while i < len(d[k[0]]):
        dn = {}
        for j in k:
            dn[j] = d[j][i]
        l.append(dn)
        i += 1
    return l

def row_to_field_first(d):
    pass

def find_by_field(d, f, v):
    l = []
    i = 0
    while i < len(d):
        if v in d[i][f]:
            l.append(d[i])
        i += 1
    return l
