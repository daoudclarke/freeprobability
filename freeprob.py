
 # phi( (a - phi(a))(b - phi(b)) ) = 0
 # phi( (ab - phi(a)*b - a*phi(b) + phi(a)*phi(b)) ) = 0
 # phi(ab) - phi(a)*phi(b) - phi(a)*phi(b) + phi(a)*phi(b) = 0

from itertools import product, groupby




def compute_free_prob(prob_func, input_sequence):
    """
    Compute the probability of the sequence, expressed as a
    space-separated string. Elements starting with m_ and s_ are
    treated as free respectively.

    Input: prob_func: function taking a tuple of symbols and returning probabilities
           sequence: a tuple for which to compute the probability
    """
    multiplier = 1.0
    for s in input_sequence:
        if type(s) == float:
            multiplier *= s
    sequence = [s for s in input_sequence if type(s) != float]

    if len(sequence) == 0:
        return multiplier

    free_sequence = get_free_sequences(sequence)

    if len(free_sequence) == 1:
        return multiplier*prob_func(free_sequence[0])

    poly = [(s, -prob_func(s)) for s in free_sequence]
    expressions = product(*poly)

    total = 0.0
    # Skip the first expression, which is what we're trying to compute
    next(expressions)
    for expression in expressions:
        unpacked = []
        for e in expression:
            if type(e) == float:
                unpacked.append(e)
            else:
                unpacked += list(e)
        total -= compute_free_prob(prob_func, unpacked)

    print input_sequence, multiplier*total
    return multiplier * total


def get_free_sequences(sequence):
    """
    Return tuples of sequences which combine freely (which we are
    assuming have different first characters).
    """
    return [tuple(group) for _, group in groupby(sequence, lambda s: s[0])]
