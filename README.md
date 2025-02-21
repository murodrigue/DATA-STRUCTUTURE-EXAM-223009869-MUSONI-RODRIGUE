Q1. It’s about a simple program which print a “ hello word”

#include <iostream>
using namespace std;
int main ()
{
cout << "Hello, World!"; 
	return 0;
}



•	#include  : This includes a library that allows us to print anything by using "cout".
•	<iostream : incuding input and output in a program you are doing.
•	using namespace std  : help programer to write in easy way without wring std::.... IN each line of code.
•	int main ()  :  its a function where program start .
•	cout :  help programmmer to print output on screen.
•	return 0 : it end the program successfull with  zero error.


Q2. This question is dealing with variables, data type and values of variables.

here : variable:age 
     data type : int
     values =20

  in this question there is also what we call initalizatin by giving variables their values
#include <iostream>

using namespace std;
int main() {
    int age = 20;  //declaration and initalizatin
    double price = 19.99;  
    char grade = 'A'; 
    string name = "Alice"; 

    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Price: $" << price << endl;
    cout << "Grade: " << grade << endl;
    
	return 0;
 }

 Q3. QUESTION 3.
 
#include <iostream>
using namespace std;

int main() {
    string name;
    int age;

    cout << "Enter your name: ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Hello, " << name << "! You are " << age << " years old." << endl;

    return 0;
}

Q4. QUESTION 4.

#include <iostream>
using namespace std;

int main() {
	int a = 10, b = 3;
cout << "Sum: " << a + b << endl;
cout << "Difference: " << a - b << endl;
cout << "Product: " << a * b << endl;
cout << "Quotient: " << a / b << endl;
cout << "Remainder: " << a % b << endl;

    return 0;
}


Q5. QUESTION FIVE DEAL WITH   Modify the user input program to take a favorite color and print a message like:
"Wow! Blue is a great color!"

#include <iostream>
using namespace std;
int main() {
	string favoriteColor;
	cout << "Enter your favorite color: ";
	cin >> favoriteColor;
	cout << "Wow! " << favoriteColor <<" is a great color!" <<endl;
return 0;
}
