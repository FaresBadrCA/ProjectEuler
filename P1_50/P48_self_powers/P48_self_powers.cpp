/*

Find the last 10 digits of sum(n^n) for n in 1..1000

Idea: iterate through n = 1 .. 1000 and add up n^n mod(10^10)

pow(n,n) % 10^10 will overflow, giving unexpected answers.

if I have a function to find n^n mod (10^10), then we just add its results

I'm still having trouble with overflow, so I will use gmp
install instructions here: https://stackoverflow.com/questions/4711315/build-gmp-on-64bit-windows



*/

#include <iostream>
#include <gmpxx.h>

int main() {

	mpz_t p, result, tmp;
	mpz_init_set_str(p, "10000000000", 10);
	mpz_init(result);
	mpz_init(tmp);

	for (uint32_t i = 1; i <= 1000; ++i) {
		mpz_set_ui(tmp, i); // tmp = i
		mpz_powm_ui(tmp, tmp, i, p); // (i^i)%p
		mpz_add(result, result, tmp );
		mpz_mod(result, result, p);
	}

	std::cout << mpz_get_str(NULL, 10, result) << "\n";
}