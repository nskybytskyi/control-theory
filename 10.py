import numpy as np
from itertools import product
from numpy.linalg import eig

delta_t = 0.01
t_max = 1000
epsilon = 0.001
T = []


def test(k1, k2, j, b, la, ra, x10, x20, x30):
	t = 0

	x1, x2, x3 = x10, x20, x30

	d3 = ra + (b * la) / j + 1

	d1 = 1

	d2 = (((j * la * k2 * d1) / (b * la - j * (d3 - ra)) - b * (d3 - ra)) + k1) / k2 + k1 + 1

	A = np.matrix([[0, 1, 0], [0, -b/j, k2/j], [d1/la, (d2-k1)/la, (d3-ra)/la]])

	print(f'\tmax lambda = {np.max(eig(A)[0])}\n')

	input()

	while (abs(x1) > epsilon or abs(x2) > epsilon or abs(x3) > epsilon) and t < t_max:
		t += delta_t

		x1_next = x1 + x2 * delta_t
		x2_next = x2 + (- b / j * x2 + k2 / j * x3) * delta_t
		x3_next = x3 + (d1 / la * x1 + (d2 - k1) / la * x2 + (d3 - ra) / la * x3) * delta_t

		x1, x2, x3 = x1_next, x2_next, x3_next

	if t >= t_max:
		print(f'Has not converged for params = {k1, k2, j, b, la, ra, x10, x20, x30},\n'
			f'\tmax lambda = {np.max(eig(A)[0])},\n'
			f'\tx now = {x1, x2, x3},\n'
			f'A = {A}.\n')

	T.append(t)


K1 = [1, 3, 10]
K2 = [1, 3, 10] 
J = [1, 3, 10]
B = [-1, 1, 3]
La = [-1, 1, 3]
Ra = [-1, 1, 3]  
X10 = [1]  # [-1, 1, 3]
X20 = [1]  # [-1, 1, 3]
X30 = [1]  # [-1, 1, 3]


it = 0
for k1, k2, j, b, la, ra, x10, x20, x30 in product(K1, K2, J, B, La, Ra, X10, X20, X30):
	it += 1
	if it % 10 == 0:
		print(it, f'{100*it/729:0.2f}%')
	test(k1, k2, j, b, la, ra, x10, x20, x30)


print(sum(T) / len(T))

print('max(T)', max(T), T.index(max(T)))

print('min(T)', min(T), T.index(min(T)))
