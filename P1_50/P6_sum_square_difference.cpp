/*
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

The sum of first n numbers is: S = n*(n+1)/2

For the sum of the first n numbers squared, try telescoping sum:
SUM{ (n+1)^3 - n^3 } = (N+1)^3 - 1

but the telescoping sum can also be expanded to: (Let S be sum of squares of integers from 1 to N)
3 * (S + (N^2 + N)/2) + N = N^3 + 3*N^2 + 3*N

solving for S: S = (1/6)*N*(N+1)*(2*N+1)

*/

#include <iostream>
#include<cmath>

int main() {
	int64_t N = 100;

	int64_t square_of_sums = pow( (N * (N + 1)) / 2, 2);
	int64_t sum_of_squares = (N * (2 * N + 1) * (N + 1)) / 6;

	std::cout << square_of_sums << "\n";
	std::cout << sum_of_squares << "\n";

	int64_t result = square_of_sums - sum_of_squares;

	std::cout << result << "\n";


}