#include <stdio.h>
#include <stdint.h>
#include <math.h>


uint64_t find_divisor(uint64_t n){
	uint64_t i = 2;
	uint64_t lim = floor(sqrt(n));
	while(i < sqrt(n)){
		if (n % i == 0){
			printf("%d \n", i);
			return n / i;
		}
		// printf("%lu cannot divide %lu \n", i, n);
		i++;
	}
	printf("DONE: %d \n", n);
	return 0;
}

int main() {
	uint64_t n = 600851475143LL;
	while(n = find_divisor(n)){
	}
	
}


