#include<stdio.h>
#define ROWS 3
#define COLS 3

#pragma warning(disable: 4996)

void sparse_matrix_add1(int A[ROWS][COLS], int B[ROWS][COLS], int C[ROWS][COLS]) {
	int r, c;
	for(r = 0; r < ROWS; r++)
		for(c = 0; c < COLS; c++)
		C[r][c] = A[r][c] + B[r][c];
}

void main() {
	int array1[ROWS][COLS] = { {2,3,0},{8,9,1},{7,0,5} };
	int array2[ROWS][COLS] = { {1,0,0},{1,0,0}, {1,0,0} };

	int array3[ROWS][COLS];

	sparse_matrix_add1(array1, array2, array3);


	int r, c;
	for (r = 0; r < ROWS; r++) {
		for (c = 0; c < COLS; c++)
			printf("%d ", array3[r][c]);
		printf("\n");
	}

	int exit = 0;
	scanf_s("%d", &exit);
}
