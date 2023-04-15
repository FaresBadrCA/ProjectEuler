/*

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Start with an array, p_arr, of primes below 1m
Then create an array, s_arr, of cumulative primes, where s_arr[i] is the sum of the first 'i' primes

go backwards through s_arr until we get to 1m. That is the first candidate. Test if it's prime. if it is, we're done.

Let the first candidate be s_arr[k]

then the second candidate is s_arr[k - 1]. It is the sum of k-1 consecutive primes.
There is another candidate with [k-1] consecutive primes: it's the sum of primes from p2 to pk, which is just s[k] - s[1]

The candidates with [k-2] consecutive primes are: s[k-2], s[k-1] - s[1], and s[k] - s[2]
continue this pattern until we find a prime that is less than one million

Additionally, we can skip some checks when we know the answer is even based on how many even/odd numbers we're adding

*/

#include <iostream>
#include <vector>

// return a boolean array where index [i] is true if 'i' is prime
std::vector<bool> primes_less_than_n(uint64_t n) {
	std::vector<bool> is_prime(n, true);
	uint64_t sqrt_n = floor(sqrt(n)); // all composite numbers above sqrt(n) have a prime factor below sqrt(n), so no need to run the sieve above sqrt(n)
	for (uint64_t p = 2; p <= sqrt_n; ++p) {

		if (!is_prime[p]) continue; // skip numbers that we know are composite, as they and all their multiples have been marked as False already

		// all composites before p^2 have already been taken care of, so we start at p^2
		for (uint64_t i = p * p; i < n; i += p) {
			is_prime[i] = false; // all multiples of p are composite 
		}
	}
	
	return is_prime;
}

int main() {

	uint64_t limit = 1e9;
	std::vector<bool>is_prime = primes_less_than_n(limit);

	std::vector<uint64_t> primes;
	std::vector<uint64_t> cumsum;
	primes.reserve(limit);
	cumsum.reserve(limit);
	cumsum.push_back(0); // Start at zero to have 1-indexing
	primes.push_back(0); // start at zero to have 1-indexing
	for (uint64_t i = 2; i < limit; ++i) {
		if (is_prime[i]) {
			primes.push_back(i); // primes is 1-indexed
		}
	}

	for (uint64_t i = 1; i < primes.size(); ++i) {
		uint64_t new_term = cumsum.back() + primes[i]; // cumsum[i] = sum up to the ith prime
		if (new_term >= limit) break;
		cumsum.push_back(new_term);
	}

	uint64_t k_max = cumsum.size() - 1;
	for (uint64_t k = k_max; k > 0; k--) {
		uint64_t candidate = cumsum[k];
		if (is_prime[candidate]) {
			std::cout << candidate << "\n";
			break;
		}

		for (uint64_t i = 0; i < (k_max - k); ++i) {
			candidate = cumsum[k + i + 1] - cumsum[i];

			if (candidate > limit) break; // candidate only grows larger in this loop
			if (is_prime[candidate]) {
				std::cout << candidate << "\n";
				goto done;
			}
		}	
	}
done:
	std::cout << "DONE!";
}