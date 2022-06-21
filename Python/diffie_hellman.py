from random import random

def private_key(p):
    
    return round(random()*p)


def public_key(p, g, private):
    return (g ** private) % p


def secret(p, public, private):
    return (public ** private) % p
