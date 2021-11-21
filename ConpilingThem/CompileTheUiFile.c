#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char input[100];
	char uiName[110];
	char pyName[110];
	char sys[300]="D:\\PythonPrograms\\PyQt\\venv\\Scripts\\pyuic5.exe -x ";
	scanf("%s",&input);
	strcpy(uiName,input);
	strcpy(pyName,input);
	strcat(uiName,".ui");
	strcat(pyName,".py");
	strcat(sys,uiName);
	strcat(sys," -o ");
	strcat(sys,pyName);
	system(sys);
	return 0;
} 
