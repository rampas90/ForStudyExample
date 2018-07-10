#include<stdio.h>

#pragma warning(disable: 4996)
#define TRUE  1

int is_prime(int n) {
	int i;
	for (i = 2; i < n; i++)
		if (n%i == 0)
			return !TRUE;
	return TRUE;
}
void main() {
	int n;
	puts("\n PRIME1		: TEST that input number is prime or not.\n			Input 0 to end program.");
	while (TRUE) {
		printf("\nInput number to test ->");
		scanf("%d", &n);
		if (n < 0)
			continue;
		if (n == 0) break;
		printf("\n	Ans : %d is %s prime number", n, is_prime(n) ? "" : " not");

	}
}