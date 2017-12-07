"""
set() - function
set object
    sets are curly brackets { }
    sets are mutable
    creates unordered collection of unique and immutable objects
    can't contain mutable objects
    does not output doubles

frozenset() - function
frozenset object
    like sets, but are immutable

set operations:
    add()
    clear()
    copy()
    difference() or " - "
    difference_update() or " -= "
    x.discard(a)
        removes a from set x
    x.remove(a)
        like discard but raises KeyError if a not in set x
    x.union(y) or "x | y"
        returns set of all elements of both sets x and y
    x.intersection(y) or "x & y"
        returns set of shared elements of sets x and y
    isdisjoint()
        returns true for no intersection
    x.issubset(y)
        returns True if x is a subrset of y
    x.issuperset(y)
        returns True if x is a superset of y
    pop()
        removes and returns a random element
        KeyError if empty set
"""
x = set("super foods are tight")
print(x)
#output: {'o', 'h', 'u', 'e', 't', 's', 'g', 'i', 'r', ' ', 'p', 'a', 'd', 'f'}

y = set(["PHP", "Python", "Swift", "PHP"])
y.add("Java")
print(y)
#output: {'PHP', 'Python', 'Swift', 'Java'}
#look at output - doubling doesn't happen
