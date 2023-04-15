#pragma once
#include <vector>

// Use sieve of Eratosthenes to get all primes less than or equal to n. 
std::vector<uint64_t> primes_less_than_n(uint64_t n) {
	std::vector<bool> is_prime(n, true);
	uint64_t sqrt_n = floor(sqrt(n)); // all composite numbers above sqrt(n) have a prime factor below sqrt(n), so no need to run the sieve above sqrt(n)
	for (uint64_t p = 2; p <= sqrt_n; ++p) {

		if (!is_prime[p]) continue; // skip numbers that we know are composite, as they and all their multiples have been marked as False already

		// all composites before p^2 have already been taken care of, so we start at p^2
		for (uint64_t i = p * p; i < n; i += p) {
			is_prime[i] = false; // all multiples of p are composite 
		}
	}

	std::vector<uint64_t> primes;
	primes.reserve(n);
	for (uint64_t i = 2; i < n; ++i) {
		if (is_prime[i]) {
			primes.push_back(i);
		}
	}
	return primes;
}