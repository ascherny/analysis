#include <stdio.h>

int func1(int param);
int func2(int param);
int func3(int param);
int func4(int param);

int func1(int param)
{
    return func2(param+0x0010);
}

int func2(int param)
{
    return func3(param % 0x0025);
}

int func3(int param)
{
    return func4(param*0x0005);
}

int func4(int param)
{
    return param - 0x0015;
}

int main(int argc, char** argv)
{
    int data = 0x0001;
    data = func1(data);
    printf("%d\n", data);
}
