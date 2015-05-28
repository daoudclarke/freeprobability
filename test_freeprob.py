
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
    #sequence = 'm_john s_n m_sneezed s_v m_someone s_n m_coughed s_v'.split()
    sequence = 'm_john s_n m_sneezed s_v'.split()
    #probs = defaultdict(float, {
    probs = {
        ('m_john',): 0.5,
        ('m_sneezed',): 0.4,
        ('m_sneezed', 'm_someone'): 0.4,
        ('m_john', 'm_sneezed'): 0.3,
        ('m_someone',): 0.7,
        ('m_coughed',): 0.6,
        ('m_john', 'm_someone'): 0.5,
        ('m_sneezed', 'm_coughed'): 0.4,
        ('m_someone', 'm_coughed'): 0.4,
        ('m_john', 'm_coughed'): 0.5,
        ('m_john', 'm_sneezed', 'm_someone'): 0.3,
        ('m_sneezed', 'm_someone', 'm_coughed'): 0.2,
        ('m_john', 'm_sneezed', 'm_coughed'): 0.3,
        ('m_john', 'm_someone', 'm_coughed'): 0.2,
        ('m_john', 'm_sneezed', 'm_someone', 'm_coughed'): 0.2,
        ('s_n',): 0.9,
        ('s_v',): 0.9,
        ('s_n', 's_v'): 0.8,
        ('s_v', 's_n'): 0.5,
        ('s_n', 's_n'): 0.1,
        ('s_v', 's_v'): 0.1,
        ('s_n', 's_v', 's_n'): 0.4,
        ('s_n', 's_n', 's_v'): 0.1,
        ('s_v', 's_n', 's_v'): 0.4,
        ('s_n', 's_v', 's_v'): 0.1,
        ('s_n', 's_v', 's_n', 's_v'): 0.3,
        }

    prob = compute_free_prob(probs.__getitem__, sequence)
    print prob
