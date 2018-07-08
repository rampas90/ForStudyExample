#include<stdio.h>

int get_gcd(int u, int v) {
	int t;
	while (u) {
		if (u < v) {
			t = u;
			u = v;
			v = t;
		}
		u = u - v;
	}
	return v;
}
int gcd_modulus(int u, int v) {
	int t;
	while (v) {
		t = u % v;
		u = v;
		v = t;
	}
	return u;
}

int gcd_recursion(int u, int v) {
	if (v == 0) return u;
	else return gcd_recursion(v, u%v);
}
void main(void) {
	int u, v;
	puts("\n EUCLID1 : Get GCD of two positive integer"
		"\n				Input 0 to end program");

	while (1) {
		puts("\n\n Input two positive intger -> ");
		scanf_s("%d %d", &u, &v);
		if(u<0 || v<0)
			continue;
		if (u == 0 || v == 0) break;
		printf("\n	GCD of %d and %d is %d.", u, v, get_gcd(u, v));

	}

}