# Primitive expressions

2017
201.7
'Hello world!'
True
False
[2, 0, 'one', 'seven']


# Operators

2000 + 17
2001 + 4 ** 2
4034 // 2
-1 + 0 + 1 * 2 ** 3 * 4 // 5 * 6 * 7 * 8 * 9 // 10 + 11 + 12 + 13 * 14 - 1
'Hello ' + 'world!'
[2, 0] + ['one', 'seven']


# Call expressions

from operator import add, mul
add(2000, 17)
mul(1009, 2)
abs(-2017)
pow(2, 100)

from math import sqrt
sqrt(2017)

from math import sin, pi
sin(pi)


# Nested call expressions

add(add(6, mul(4, 6)), mul(3, 5))


# Shakespeare demo
# Note: Download from http://composingprograms.com/shakespeare.txt

shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:15]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets have no repeated elements
words = set(text)
len(words)
max(words)
max(words, key=len)

# Reversing a word
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w) > 4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}