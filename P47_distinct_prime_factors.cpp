/*

Find the first four consecutive integers to have four distinct prime factors each.

re-use the sieve of eratosthenes, but this time, use it to calculate the number of distinct factors
for each number in the sieve
 
*/

#include <iostream>
#include <vector>

// Find the number of distinct factors for each number below n
std::vector<uint32_t> distinct_factors_array(uint64_t n) {
	std::vector<uint32_t> distinct_factors_count(n, 0); // initialize as if all numbers are prime, not counting themselves as a factor

	// We can't stop at sqrt_n like in the sieve of Eratosthenes, because we have to count primes above sqrt(n) as distinct factors as well 
	for (uint64_t p = 2; p < n; ++p) {
		if (distinct_factors_count[p] > 0) continue; // skip numbers that we know are composite, as they don't add distinct factors

		for (uint64_t i = p; i < n; i += p) {
			distinct_factors_count[i] += 1; // all multiples of p have p as a factor
		}
	}
	return distinct_factors_count;
}

int main() {
	uint64_t MAX = 1000000;
	auto df_arr = distinct_factors_array(MAX);

	// Check for 4 numbers in a row with #distinct factors >= 4
	for (size_t i = 2; i < MAX - 4; ++i) {
		if (df_arr[i] < 4) continue;

		if (df_arr[i + 1] >= 4 && df_arr[i + 2] >= 4 && df_arr[i + 3] >= 4) {
			std::cout << i << "\n";
			return 0;
		}
	}

}