
from freeprob import compute_free_prob, get_free_sequences
from collections import defaultdict


# def test_compute_free_prob():
#     probs = {
#         'm_john': 0.5,
#         'm_sneezed': 0.5,
#         'm_someone': 0.4,
#         'm_coughed': 0.6,
#         'm_john m_

def test_compute_free_prob():
    probs = {('m_a',): 0.5, ('s_a',): 0.5}
    prob = compute_free_prob(probs.__getitem__, ('m_a', 's_a'))
    assert prob == 0.25


def test_free_sequences():
    sequence = ['s_a', 's_b', 'm_a', 's_b']
    free = get_free_sequences(sequence)
    assert free == [('s_a', 's_b'), ('m_a',), ('s_b',)]


def test_sneeze():
    sequence = 'm_john s_n m_sneezed s_v m_someone s_n m_coughed s_v'.split()
    #sequence = 'm_john s_n m_sneezed s_v'.split()
    probs = {
        1: 0.1,
        2: 0.2,
        3: 0.3,
        4: 0.4,
        }

    masses = {
        'm_john': {3},
        'm_someone': {1, 3},
        'm_sneezed': {3},
        'm_coughed': {2, 3, 4},
        }

    def distribution(concepts):
        if concepts[0].startswith('m'):
            intersection = reduce(set.__and__, [masses[c] for c in concepts])
            return sum(probs[c] for c in intersection) or 0.0
        
        sequence = ' '.join(concepts)
        p = 0.0
        if sequence in 's_n s_v s_n s_v':
            p += 0.5
        if sequence in 's_n s_v':
            p += 0.5
        return p

    prob = compute_free_prob(distribution, sequence)
    print prob
