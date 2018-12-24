from itertools import product

delta_t, epsilon, T = 0.01, 0.001, []


def test(k1, k2, j, b, la, ra, x10, x20, x30):
	t, x1, x2, x3 = 0, x10, x20, x30

	d1, d3 = 1, ra + b * la / j + 1 / j

	d2 = (la * k2 - b * (b * la / j) + 1) / k2 + k1 + 1 / k2

	while abs(x1) > epsilon or abs(x2) > epsilon or abs(x3) > epsilon:
		t += delta_t

		x1_next = x1 + x2 * delta_t
		x2_next = x2 + (- b / j * x2 + k2 / j * x3) * delta_t
		x3_next = x3 + (d1 / la * x1 + (d2 - k1) / la * x2 + (d3 - ra) / la * x3) * delta_t

		x1, x2, x3 = x1_next, x2_next, x3_next

	T.append(t)


K1, K2 = [1, 3, 10], [1, 3, 10] 
J = [1, 3, 10]
B = [-1, 1, 3]
La, Ra = [-1, 1, 3], [-1, 1, 3]  
X10, X20, X30 = [-1, 1, 3], [-1, 1, 3], [-1, 1, 3]


it = 0
for k1, k2, j, b, la, ra, x10, x20, x30 in product(K1, K2, J, B, La, Ra, X10, X20, X30):
	it += 1
	if it % 100 == 0:
		print(it, f'{100*it/19683:0.2f}%')
	test(k1, k2, j, b, la, ra, x10, x20, x30)


print(sum(T) / len(T))

print('max(T)', max(T), T.index(max(T)))

print('min(T)', min(T), T.index(min(T)))
