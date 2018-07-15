#include<stdio.h>
#include<stdlib.h>

#pragma warning(disable: 4996)

#define MAX_TERMS 101

struct {
	float coef;
	int expon;
} terms[MAX_TERMS] = { {8,3},{7,1},{1,0},{10,3},{3,2},{1,0} };
int avail = 6;

char compare(int a, int b) {
	if (a > b) return '>';
	else if (a == b) return '=';
	else return '<';
}

void attach(float coef, int expon) {
	if (avail > MAX_TERMS) {
		fprintf(stderr, "항의 개수가 너무 많음\n");
		exit(1);
	}
	terms[avail].coef = coef;
	terms[avail++].expon = expon;

}

void poly_add2(int As, int Ae, int Bs, int Be, int *Cs, int *Ce) {
	float tempcoef;
	*Cs = avail;
	while (As <= Ae && Bs <= Be)
		switch (compare(terms[As].expon, terms[Bs].expon))
		{
		case '>':
			attach(terms[As].coef, terms[Bs].expon);
			As++;
			break;
		case '=':
			tempcoef = terms[As].coef + terms[Bs].coef;
			if( tempcoef)
				attach(tempcoef, terms[As].expon);
			As++;
			Bs++;
			break;
		case '<':
			attach(terms[Bs].coef, terms[Bs].expon);
			Bs++;
			break;
		}
	for (; As <= Ae; As++)
		attach(terms[As].coef, terms[As].expon);
	for (; Bs <= Be; Bs++)
		attach(terms[Bs].coef, terms[Bs].expon);

	*Ce = avail - 1;
}
void main() {
	int Cs, Ce;
	poly_add2(0, 2, 3, 5, &Cs, &Ce);


	for (int i = 0; i < avail; i++) {
		printf("coef : %f, expon: %d \n", terms[i].coef, terms[i].expon);
	}


	int exit = 0;
	scanf_s("%d", &exit);
}