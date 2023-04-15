#include <iostream>


// count the number of distinct divisors of a number, n
int count_divisors(int n) {
	int count = 0;
	for (int i = 1; i <= sqrt(n); ++i) {
		if (n % i == 0) {
			// then both n/i and i are divisors. if they're the same, increment count by one
			if (n / i == i) {
				count = count + 1;
			}
			else {
				count = count + 2;
			}
		}
	}
	return count;
}

int main() {
	uint64_t n = 1;
	while (n++) {
		uint64_t T = (n * (n + 1)) / 2;
		int n_divisors = count_divisors(T);

		std::cout << "n: " << n << ", #Divisors: " << n_divisors << "\n";
		if (n_divisors >= 500) {
			std::cout << "Triangle Number: " << T << "\n";
			return 0;
		}
	}

}