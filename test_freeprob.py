
from freeprob import compute_free_prob, compute_independent_prob, get_free_sequences
from collections import defaultdict


def test_compute_free_prob():
    probs = {('m_a',): 0.5, ('s_a',): 0.5}
    prob = compute_free_prob(probs.__getitem__, ('m_a', 's_a'))
    assert prob == 0.25


def test_free_sequences():
    sequence = ['s_a', 's_b', 'm_a', 's_b']
    free = get_free_sequences(sequence)
    assert free == [('s_a', 's_b'), ('m_a',), ('s_b',)]


def test_sneeze():
    sequence = 's_john v_likes o_mary s_mary v_likes o_barry'.split()
    #sequence = 'n_john v_sneezed'.split()
    probs = {
        1: 0.1,
        2: 0.2,
        3: 0.3,
        4: 0.4,
        }

    masses = {
        's_john': {1,2},
        's_mary': {2,3},
        'o_mary': {1,3},
        'o_barry': {2,3},
        'v_likes': {4},
        'c_and': {4},
        }

    def distribution(concepts):
        intersection = reduce(set.__and__, [masses[c] for c in concepts])
        return sum(probs[c] for c in intersection) or 0.0
        
    prob = compute_free_prob(distribution, sequence)
    print "Free: ", prob
    
    prob_ind = compute_independent_prob(distribution, sequence)
    print "Independent: ", prob_ind
