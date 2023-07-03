/*
Find the largest palindrome made from the product of two 3-digit numbers.
*/
#include <iostream>

bool is_palindrome(uint64_t n);

int main(){
	
	uint64_t a_best = 0;
	uint64_t b_best = 0;
	for (uint64_t a = 100; a < 1000; ++a) {
		for (uint64_t b = 100; b < 1000; ++b) {
			if (is_palindrome(a * b)) {
				if (a * b > a_best * b_best) {
					a_best = a;
					b_best = b;
				}
			}
		}
	}
	std::cout << a_best << "\n";
	std::cout << b_best << "\n";
	std::cout << a_best * b_best << "\n";
}

bool is_palindrome(uint64_t n) {
	uint8_t digits[6];
	uint8_t n_digits = 0;
	
	// count the digits of n and put them in an array
	while (n) {
		n_digits++;
		digits[n_digits - 1] = n % 10; // first digit is in 0th index, etc.
		n = n / 10;
	}

	for (int i = 0; i <= n_digits / 2; ++i) {
		if (digits[i] != digits[n_digits - 1 - i]) {
			return false;
		}
	}

	return true;
}