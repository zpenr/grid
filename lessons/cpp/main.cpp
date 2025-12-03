#include <iostream>

using namespace std;

int fib(const int size){
	int fib[size] = {1,1};
	for(int i = 2; i < size; i++){
		fib[i] = fib[i-1]+fib[i-2];
	} 
	return fib
}

int main()
{
	fib = fib(10000);
	return 0;
}