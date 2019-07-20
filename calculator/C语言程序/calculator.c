#include<stdio.h>
int main(void)
{
	printf("欢迎来到大金猪计算器C语言版！！！\n");
	printf("---------------------------------\n");
	int a;
	int b;
	int H;
	printf("请输入一个数:");
	scanf_s("%d", &a);
	printf("再输入一个数:");
	scanf_s("%d", &b);
	H = a + b;
	printf("---------------------------------\n");
	printf("你的得数是%d。", H);
	getchar();
	getchar();
}
