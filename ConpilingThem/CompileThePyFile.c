#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char input[100];
	char pyName[110];
	char sys[300]="D:\\PythonPrograms\\JustForCompiling\\Scripts\\pyaller.exe -F ";
	scanf("%s",&input);
	strcpy(pyName,input);
	strcat(pyName,".py");
	strcat(sys,pyName);
	strcat(sys," -w -i=\"icon.ico\"");
	system(sys);
	return 0;
} 
