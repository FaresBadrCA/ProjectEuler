/*
Use the Sieve of Eratosthenes, going up to some upper bound on values of the Nth prime number.
*/

#include <iostream>
#include <cmath>
#include "math_utility.hpp"

int main() {
	// Q: What is the upper bound on the 10,001st prime?
	uint64_t n = 10001;
	double upper_bound = ceil(n * (log(n)) * log(log(n))); // No idea how to prove this. https://en.wikipedia.org/wiki/Prime_number_theorem
	std::vector<uint64_t> primes = primes_less_than_n(upper_bound);
	std::cout << primes[n - 1] << "\n"; // recall zero-indexing
}