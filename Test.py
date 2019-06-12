from utils import*



G = numpy.polynomial.Polynomial([2,4,5])

G2 = numpy.polynomial.Polynomial([2,4,5])

H = mimotf([[tf([1,1],[1,2]),tf(1,[1,1])],
                [tf(1,[1,1]),tf(1,[1,1])]])
Ac, Bc, Cc, Dc = tf2ss(H)
print(Ac)
    # matrix([[ 0.,  1.,  0.],
    #         [-2., -3.,  0.],
    #         [ 0.,  0., -1.]])
print(Bc)
    # matrix([[0., 0.],
    #         [1., 0.],
    #         [0., 1.]])
print(Cc)
    # matrix([[-1., -1.,  1.],
    #         [ 2.,  1.,  1.]])
print(Dc)
    # matrix([[1., 0.],
    #         [0., 0.]])

print(num_denom(G))
