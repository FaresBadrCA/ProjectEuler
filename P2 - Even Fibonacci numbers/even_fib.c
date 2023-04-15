#include <stdio.h>
#include <stdint.h>

int main() {
	uint64_t limit = 4000000;
	printf("%d \n", limit);
	
	uint64_t n1 = 1;
	uint64_t n2 = 2;
	
	uint64_t sum = 2;
	
	while (n2 < (limit - n1) ){
		n2 = n1 + n2;
		printf("%d \n", n2);
		n1 = n2 - n1; // n1 is now the previous n2 value
		if ( (n2 % 2) == 0){
			sum += n2;
		}
	}
	
	printf("%d \n", sum);
	
}