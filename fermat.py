__author__ = 'Derek'

def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def input_fermat():
    a = raw_input("What is the value of a?")
    b = raw_input("What is the value of b?")
    c = raw_input("What is the value of c?")
    n = raw_input("What is the value of n?")

    check_fermat(float(a), float(b), float(c), float(n))

input_fermat()





