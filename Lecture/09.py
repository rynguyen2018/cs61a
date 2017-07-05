def link(first, rest):
    return [first, rest]

def first(s):
    assert s != empty, 'empty linked list has no first'
    return s[0]

def rest(s):
    assert s != empty, 'empty linked list has no rest'
    return s[1]

four = link(1, link(2, link(3, link(4, empty))))
march = link(1, link(2, link(1, link(2, empty))))
v1 = link(march, four)
v2 = link(march, link(four, empty))
first(rest(rest(rest(v1))
# Which of these evaluates to 3?
# first(rest(rest(first(rest(v2)))))
# first(rest(first(rest(rest(v2)))))
# first(rest(first(rest(first(v2)))))
# first(rest(rest(rest(first(v2)))))
# first(first(rest(rest(first(v2)))))