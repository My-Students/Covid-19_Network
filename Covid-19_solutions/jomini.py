# Jomini Pietro
# 5/3/2020
# https://github.com/My-Students/Covid-19_Network

from sys import argv

def data2addict(fname):
    """
    Parse input data file into an adj dict
    """

    adj = {}

    try:
        with open(fname, 'r') as data:
            for line in data:
                case = [int(c) for c in line.strip().split(' ')]
                adj[case[0]] = case[1:]
    except FileNotFoundError:
        print(f'File {fname} not found!', file=sys.stderr)

    return adj


def addict2admat(addict):
    """
    Transpose an adj dict into an adj matrix
    """

    V = range(len(addict))
    admat = [[0 for i in V] for k in V]

    for node in addict:
        for link in addict[node]:
            admat[node][link] = 1

    return admat


def addict2p0(addict):
    """
    Retrieve patients zero from an adj dict
    """
    """
    A patient, to be a patient 0, must:
        - have infected at least one other patient -> `len(addict[node]) > 0`
        - can't be infected by any other patient
    hence we first build a list with every patient, then:
        for each patient:
            if it hasn't infected anyone remove him
            else remove every patient infected by him
    """

    p0 = [int(n) for n in addict.keys()]

    for node in addict:
        neighb = addict[node] if len(addict[node]) > 0 else [node]
        # p0 = [n for n in p0 if not n in neighb]
        p0 = list(set(p0) - set(neighb))

    return p0


def rotateMat90(mat):
    """
    Rotate a mat by 90 deg
    """
    return [list(el) for el in zip(*mat[::-1])]


def admat2p0(admat):
    """
    Retrieve patients zero from an adj mat
    """
    """
    A patient, to be a patient 0, must:
        - have infected at least one other patient -> `sum(y = patient) > 0`
        - can't be infected by any other patient -> `sum(x = patient) == 0`

    EG:

        0 0 0 0 0 0
        0 0 1 0 1 0
        0 0 0 0 0 1
        0 1 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0

        patients zero = [3]
    """

    mat90 = rotateMat90(admat)  # to easily get (x = k)
    p0 = []

    for node, y in enumerate(admat):
        if sum(y) > 0 and sum(mat90[node]) == 0:
            p0.append(node)

    return p0


def test_methods(data):
    """
    Test addict2p0 & admat2p0 with a given dataset
    """

    addict = data2addict(data)
    admat = addict2admat(addict)

    p0_dict = [el for el in addict2p0(addict)]
    p0_mat = admat2p0(admat)

    print(f'Dict method: {p0_dict}')
    print(f'Mat method: {p0_mat}')

    assert_equals = 'OK' if sorted(p0_dict) == sorted(p0_mat) else 'ERROR: not equals'
    print('Results given by two different methods should be equal: ' + assert_equals)


usage = """
ERROR: Wrong parameters number
USAGE: $ python jomini.py data
    - data: dataset path
"""

if __name__ == "__main__":

    if not len(argv) == 2: print(usage)
    else: test_methods(argv[1])