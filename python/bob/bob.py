def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if hey_bob.isupper() and '?' in hey_bob:
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if not hey_bob:
        return 'Fine. Be that way!'
    if hey_bob.endswith('?'):
        return "Sure."
    return "Whatever."