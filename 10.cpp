#include <iostream>
#include <vector>

using namespace std;

typedef long double ldouble;

ldouble det(ldouble A[3][3]) {
  return A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1] - 
    A[0][0] * A[1][2] * A[2][1] - A[0][1] * A[1][0] * A[2][2] - A[0][2] * A[1][1] * A[2][0];
}

int main() {
	ldouble Ra, La, B, J, K1, K2;
	
	cout << "\nВведіть опір обмотки Ra: ";
	cin >> Ra;
	
	cout << "\nВведіть індукцію La != 0: ";
	cin >> La;
	while (La == 0) {
		cout << "\nВи ввели некоректне значення La. Введіть La != 0: ";
		cin >> La;
	}
	
	cout << "\nВведіть параметр тертя B: ";
	cin >> B;
	
	cout << "\nВведіть момент інерції арматури і груза J > 0: ";
	cin >> J;
	while (J <= 0) {
		cout << "\nВи ввели некоректне значення J. Введіть J > 0: ";
		cin >> J;
	}

	cout << "\nВведіть K1 > 0: ";
	cin >> K1;
	while (K1 <= 0) {
		cout << "\nВи ввели некоректне значення K1. Введіть K1 > 0: ";
		cin >> K1;
	}

	cout << "\nВведіть K2 > 0: ";
	cin >> K2;
	while (K2 <= 0) {
		cout << "\nВи ввели некоректне значення K2. Введіть K2 > 0: ";
		cin >> K2;
	}

	ldouble A[3][3] = {{0, 1, 0}, {0, - B / J, K2 / J}, {0, -K1 / La, -Ra / La}};

	ldouble C[3][1] = {{0}, {0}, {1 / La}};

	return 0;
}