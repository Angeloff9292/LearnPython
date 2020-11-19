def whos_first(p1, p2):
    pl1 = []
    pl2 = []
    for i in p1:
        if i.isalpha() == False:
            pl1.append(i)
        else:
            break
    for i in p2:
        if i.isalpha() == False:
            pl2.append(i)
        else:
            break
    if len(pl1) > len(pl2):
        return "p2"
    elif len(pl2) > len(pl1):
        return "p1"
    else:
        return "tie"


def shotdown(p1, p2):
    diff = p1.find("B") - p2.find("B")
    if diff < 0:
        return 'p1'
    elif diff <0:
        return 'p2'
    else:
        return 'tie'