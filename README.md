# DATA_STRUCTURE_EXAM_223004810_NIYONSENGA_Ange_Carine
Insurance Quote System

Project 80: Description of Insurance Quote system 
This C++ project implements an Insurance Quote System that calculates insurance premiums based on an applicant's age using customizable rate brackets. The system supports two types of policy engines: Basic and Premium, both of which inherit from a common abstract base class.The system demonstrates key object-oriented programming concepts such as inheritance, polymorphism, and dynamic memory management.
The Insurance Quote System is a C++ program designed to compute insurance premiums for applicants based on defined age brackets, It supports two types of engines:
BasicEngine: Calculates premiums directly based on the applicant’s age bracket.
PremiumEngine: Adds a 50% surcharge to the base premium.

Features of Insurance Quote system
•	Add and remove rate brackets
•	List current rate brackets
•	Search brackets by age range
•	Quote premiums for applicants
•	Dynamically add or remove rate brackets
•	Calculate insurance premiums based on applicant's information
Explanation of this code:
#include <iostream>
#include <cstring>
using namespace std;
<iostream>: //  For input/output operations using cin and cout
 <cstring>:// For C-style string functions like strcmp()
 using namespace std;:// Avoids the need to prefix standard library components with std::
1.Struct Definitions
struct Applicant {
    char vin[17];       
    int age;             
   char type[10]; 
};
Defines a structure for storing applicant data
•	vin: Vehicle Identification Number (16 characters + null terminator)
•	age: Age of the applicant
•	type: Type of policy ("Basic" or "Premium")

struct RateBracket {
    float minAge, maxAge, premium;
};
Defines age-based premium brackets:
•	minAge, maxAge: Age range.
•	premium: Premium charged for this range
•	float minAge;   // Minimum age for bracket
•	float maxAge;   // Maximum age for bracket
•	float premium;  // Premium amount for that age range

2 .Abstract Base Class and inheritance
class QuoteEngine {
protected: //Members declared as protected can be accessed from within the class ,its subclasses and within the same package
    RateBracket* brackets; 
    int size;                       
•	brackets: Dynamic array of rate brackets
•	size: Current number of brackets

Public: //Members declared as public can be accessed from anywhere both inside and outside the class and by any other class such as derived class
.QuoteEngine() : brackets(nullptr), size(0) {}

virtual ~QuoteEngine() {
    delete[] brackets; // Cleanup memory
}
    virtual float calculate(const Applicant* applicant) = 0; // Abstract method

    // Add a new rate bracket to the engine
    void addBracket(const RateBracket& rb);

    // Remove a bracket by index
    void removeBracket(int index);

    // List all current rate brackets
    void listBrackets() const;
    // Search for brackets in a given age range
    void searchBracket(float minAge, float maxAge) const;
protected: //Members declared as protected can be accessed from within the class ,its subclasses and within the same package
    // Return premium based on applicant's age
    float findPremium(int age);
};
3 .Derived Classes
BasicEngine
class BasicEngine : public QuoteEngine {
public:// Members declared as public can be accessed from anywhere for both inside and outside the class
    float calculate(const Applicant* applicant) override {
return findPremium(applicant->age); // Return base premium
    }
};
 PremiumEngine
class PremiumEngine : public QuoteEngine {
public:
  float calculate(const Applicant* applicant) override {
        float base = findPremium(applicant->age);
        return base < 0 ? -1 : base * 1.5f; // Add 50% surcharge if bracket found
    }	
};
 4. User Interaction
 Menu Function
void displayMenu() {
    cout << "\n--- Insurance Quote System Menu ---\n";
    cout << "1. Add Rate Bracket to Engine\n";
    cout << "2. Remove Rate Bracket from Engine\n";
    cout << "3. List All Brackets for Engine\n";
    cout << "4. Quote an Applicant\n";
    cout << "5. Search Bracket Range\n";
    cout << "6. Exit\n";
    cout << "Enter your choice: ";
}
Main Function
int main() {
        int engineCount;
    cout << "Enter number of engines you want to create: ";
    cin >> engineCount;
	
    QuoteEngine  engines = new QuoteEngine*[engineCount]; // Create engine array

    // Select engine types
    for (int i = 0; i < engineCount; ++i) {
        int choice;
        cout << "Select type for engine #" << i + 1 << " (1 = Basic, 2 = Premium): ";
        cin >> choice;
        engines[i] = (choice == 1) ? static_cast<QuoteEngine*>(new BasicEngine()) : static_cast<QuoteEngine*>(new PremiumEngine());
    }
    bool running = true;
    while (running) {
        displayMenu();
        int option;
        cin >> option;
        switch (option) {
        case 1: // Add bracket
            int engineIndex;
            RateBracket rb;
            cout << "Select engine index (0 to " << engineCount - 1 << "): ";
            cin >> engineIndex;
            cout << "Enter minAge: "; cin >> rb.minAge;
            cout << "Enter maxAge: "; cin >> rb.maxAge;
            cout << "Enter premium: "; cin >> rb.premium;
            engines[engineIndex]->addBracket(rb);
            break;
        case 2: // Remove bracket
            int bracketIndex;
            cout << "Select engine index (0 to " << engineCount - 1 << "): ";
            cin >> engineIndex;
            cout << "Enter index of bracket to remove: ";
            cin >> bracketIndex;
            engines[engineIndex]->removeBracket(bracketIndex);
            break;

        case 3: // List brackets
            cout << "Select engine index (0 to " << engineCount - 1 << "): ";
            cin >> engineIndex;
            engines[engineIndex]->listBrackets();
           break;
        case 4: // Quote applicant
            Applicant app;
            cout << "Enter VIN (e.g., RAB1234567890123): ";
            cin.ignore();
            cin.getline(app.vin, 17);
            cout << "Enter Age (e.g., 30): ";
            cin >> app.age;
            cout << "Enter Policy Type (e.g., Basic): ";
            cin.ignore();
            cin.getline(app.type, 10);

            cout << "--- Quotes ---\n";
            for (int i = 0; i < engineCount; ++i) {
                float premium = engines[i]->calculate(&app);
                if (premium < 0)
                    cout << "Engine #" << i << ": No matching rate bracket found.\n";
                else
                    cout << "Engine #" << i << ": Premium = " << premium << " RWF\n";
            }
            Break;
    case 5:  // These are search bracket
                        float minAge, maxAge;
            cout << "Select engine index (0 to " << engineCount - 1 << "): ";
                 cin >> engineIndex;
        cout << "Enter search minimum age: ";
            cin >> minAge;
        cout << "Enter search maximum age: ";
                    cin >> maxAge;
            engines[engineIndex]->searchBracket(minAge, maxAge);
        break
        case 6:
            running= false;
break;
defaut:
            Cout<<”invalid option.\n”;
    }
} 
For(int i=0; i<enginecount; ++i)
- Handles menu choices

Cleanup
delete engines[i];
delete[] engines;
return 0;
. Frees memory allocated for engines


