#define _CRT_CECURE_NO_WARNINGS

int main(void) {

	int T;
	int test_case;

	freopen("input.txt", "r", stdin);

	setbuf(stdout.NULL);
	scanf_s("%d", &T);


	for (test_case = 1; test_case <= T; ++test_case){
		int num[10];
		for (int i = 0; i < 10; i++) {
			scanf_s("%d", &num[i]);
		}

		for (int i = 0; i < 10; i++) {
			printf("%d",num[i]);
		}
	}
}