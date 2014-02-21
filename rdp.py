import numpy as np


def pldist(x0, x1, x2):
    return np.divide(np.linalg.norm(np.linalg.det([x2 - x1, x1 - x0])),
                     np.linalg.norm(x2 - x1))


def rdp(M, epsilon=0, dist=pldist):
    dmax = 0.0
    index = -1

    for i in xrange(1, M.shape[0]):
        d = dist(M[i], M[0], M[-1])

        if d > dmax:
            index = i
            dmax = d

    if dmax > epsilon:
        r1 = rdp(M[:index + 1], epsilon)
        r2 = rdp(M[index:], epsilon)

        return np.vstack((r1[:-1], r2))
    else:
        return np.vstack((M[0], M[-1]))


def rdp_nn(seq, epsilon=0, dist=pldist):
    return rdp(np.array(seq), epsilon, dist).tolist()
