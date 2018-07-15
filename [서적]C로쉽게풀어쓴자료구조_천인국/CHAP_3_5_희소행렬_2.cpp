#include<stdio.h>

#include<stdlib.h>

#pragma warning(disable: 4996)

#define ROWS 3
#define COLS 3
#define MAX_TERMS 10

typedef struct {
	int row;
	int col;
	int value;
} element;

typedef struct SparseMatrix {
	element data[MAX_TERMS];
	int rows;
	int cols;
	int terms;
} SparseMatrix;


SparseMatrix sparse_matrix_add2(SparseMatrix a, SparseMatrix b)
{
	SparseMatrix c;
	int ca = 0, cb = 0, cc = 0;//각 배열의 항목을 가리키는 인덱스
	if (a.rows != b.rows || a.cols != b.cols) {
		fprintf(stderr, "희소행렬 크기에러ㅜ \n");
		exit(1);
	}

	c.rows = a.rows;
	c.cols = a.cols;
	c.terms = 0;

	while (ca < a.terms && cb < b.terms) {
		//각 항목의 순차적인 번호를 계산하다.
		int inda = a.data[ca].row * a.cols + a.data[ca].col;
		int indb = b.data[cb].row * b.cols + b.data[cb].col;
		if (inda < indb) {
			//a배열에 항목이 앞에 있으면
			c.data[cc++] = a.data[ca++];
		}
		else if (inda == indb) {
			if ((a.data[ca].value +
				b.data[cb].value) != 0) {
				c.data[cc].row = a.data[ca].row;
				c.data[cc].col = a.data[ca].col;
				c.data[cc++].value = a.data[ca++].value + b.data[cb++].value;
			}
			else {
				ca++;
				cb++;
			}
		}
		else
			c.data[cc++] = b.data[cb++];
	}
	for (; ca < a.terms; )
		c.data[cc++] = a.data[ca++];
	for(; cb<b.terms; )
		c.data[cc++] = b.data[cb++];
	c.terms = cc;
	return c;
}
void main() {
	SparseMatrix m1 = { {{1,1,5},{2,2,9}},3,3,2 };
	SparseMatrix m2 = { {{0,0,5},{2,2,9}},3,3,2 };
	SparseMatrix m3;

	m3 = sparse_matrix_add2(m1, m2);

	int i;
	for (i=0; i < m3.terms; i++) {
		printf("%d %d %d \n", m3.data[i].row, m3.data[i].col, m3.data[i].value);
	}
	int exit = 0;
	scanf_s("%d", &exit);
}
