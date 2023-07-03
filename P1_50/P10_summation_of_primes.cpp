#include <iostream>
#include "math_utility.hpp"

int main() {
	uint64_t limit = 2000000;

	auto primes_v = primes_less_than_n(limit);

	uint64_t sum = 0;
	for (uint64_t p : primes_v) {
		sum += p;
	}

	std::cout << sum;
}