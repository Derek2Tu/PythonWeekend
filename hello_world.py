__author__ = 'Derek'


def do_four(e):
    e()
    e()
    e()
    e()

def print_bar1():
    print "+", "-"*4,

def print_beam():
    do_four(print_bar1)
    print "+"

def print_bar2():
    print '|' + ' '*5,

def print_beam2():
    do_four(print_bar2)
    print '|'

def print_row():
    print_beam()
    do_four(print_beam2)

def print_grid():
    do_four(print_row)
    print_beam()

print_grid()





# def print_grid(f, g):
#    print_beam(f)
#    print_beam2(g)

# print_grid(print_bar1, print_bar2)










