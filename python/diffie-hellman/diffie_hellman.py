def private_key(p):
    import random
    return random.randint(2, p-2)


def public_key(p, g, private):
    return pow(g, private, p)


def secret(p, public, private):
    return pow(public, private, p)