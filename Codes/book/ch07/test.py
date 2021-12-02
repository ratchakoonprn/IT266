from math import *
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    total = len(arrivals)
    print('total = ',total)
    position = ceil(total/2)
    print('position = ',position)
    late = arrivals[position:total-1]
    print(late)
    return name in late

arrivals=['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(arrivals,'May'))