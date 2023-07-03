/*
Want (1) a^2 + b^2 = c^2
also want (2) a + b + c = 1000
square the second equation:
we get 2*(ab + ac + bc) + a^2 + b^2 + c^2 = 10^6

substitute equation (1), we get
2*(ab + ac + bc + c^2) = 10^6
ab + ac + bc + c^2 = 5*10^5
ab + c * (a+b+c) = 5*10^5

substitute equation (2), we get
ab + 1000*c = 500,000

This equation says: given 3 integers whose sum is 1000,
if they meet this equation, then they are a pythagorean triplet

Idea: iterate through values of 'c', which must be positive
then we know a^2 + b^2 and we know a^2 * b^2

solve for a^2 and b^2. If they are square numbers, the problem is solved.

Solution for simultaneous equations (a+b)/2 = m and (ab) = K:
a,b = m +- sqrt(m^2 - K)

PROBLEM: using m = (a+b)/2 means we have to represent m as a floating point or risk truncating (a+b)/2
thus, use m = (a+b)
*/

#include <iostream>

bool is_square(uint64_t n) {
	uint64_t sqrt_n = sqrt(n);
	return (sqrt_n * sqrt_n == n);
}

int main() {
	uint64_t c = 1;
	double m = 0; // I couldn't figure out how to do the calculation without using floating point numbers
	uint64_t K = 0;

	while (c++){
		std::cout << c << "\n";

		K = (500000 - 1000*c) * (500000 - 1000*c);
		m = (double)(c * c) / 2;

		double b_sq = m + sqrt(m * m - K);
		double a_sq = m - sqrt(m * m - K);

		if (is_square(a_sq) && is_square(b_sq) && c > sqrt(b_sq) ) {
			std::cout << "SOLUTION FOUND: \n";
			std::cout << "a = " << sqrt(a_sq) << "\n";
			std::cout << "b = " << sqrt(b_sq) << "\n";
			return 0;
		}

	}
}