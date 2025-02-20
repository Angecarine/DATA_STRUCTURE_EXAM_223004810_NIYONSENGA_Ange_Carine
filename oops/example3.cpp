#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int age = 25;
if (age >= 18 && age < 60) {
    cout << "You are an adult." << endl;
} else if (age >= 60) {
    cout << "You are a senior citizen." << endl;
} else {
    cout << "You are a minor." << endl;
}

	return 0;
}
