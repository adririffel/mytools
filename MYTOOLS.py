import math
PI_INT = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

E_INT = 718281828490452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

def pi_real(n):
    pi = '3,'+str(PI_INT)
    if n==0:
        return '3'
    else:
        new_pi = pi[0:n+2]
        return new_pi

def e_real(n):
    e = '2,'+str(E_INT)
    if n==0:
        return '2'
    else:
        new_e = e[0:n+2]
        return new_e

