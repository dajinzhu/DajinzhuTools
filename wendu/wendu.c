#include <stdio.h>
void sszhs(void);
void hszss(void);
int main()
{
	int xz;
	printf("大金猪温度转换程序(Pre-alpha)\n");
	printf("-----------------------\n");
	printf("1.摄氏温度转华氏温度\n");
	printf("2.华氏温度转摄氏温度\n");
	printf("-----------------------\n");
	printf("请输入序号:");
	scanf_s("%d",&xz);
	if (xz == 1)
	{
		printf("-----------------------\n");
		printf("你选择的是摄氏温度转华氏温度\n");
		printf("-----------------------\n");
		sszhs();
	}
	else if (xz == 2)
	{
		printf("-----------------------\n");
		printf("你选择的是华氏温度转摄氏温度\n");
		printf("-----------------------\n");
		hszss();
	}
	else
	{
		printf("无此选项!!!");
	}
}
void sszhs(void)
{
	float f;
	float c;
	printf("请输入摄氏温度:");
	scanf_s("%f", &c);
	f = (c * 1.8) + 32.0;
	printf("华氏温度是 %f 。", &f);
}
void hszss(void)
{
	float c;
	float f;
	printf("请输入华氏温度:");
	scanf_s("%f", &f);
	c = (f - 32.0) / 1.8;
	printf("摄氏温度是 %f 。", &c);
}
