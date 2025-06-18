#include <iostream>
#include <cstring>
#include <limits>

using namespace std;

// Define Applicant structure
struct Applicant {
    char vin[17];
    int age;
    char type[10];
};

// Define RateBracket structure
struct RateBracket {
    float minAge;
    float maxAge;
    float premium;
};

// Abstract base class for quote engine
class QuoteEngine {
protected:
    RateBracket* brackets;
    int size;

public:
    QuoteEngine() : brackets(nullptr), size(0) {}
    virtual ~QuoteEngine() {
        delete[] brackets;
    }

    virtual float calculate(const Applicant* applicant) = 0;

    void addBracket(const RateBracket& rb) {
        RateBracket* newBrackets = new RateBracket[size + 1];
        for (int i = 0; i < size; ++i)
            newBrackets[i] = brackets[i];
        newBrackets[size] = rb;
        delete[] brackets;
        brackets = newBrackets;
        ++size;
    }

    void removeBracket(int index) {
        if (index < 0 || index >= size) return;
        RateBracket* newBrackets = new RateBracket[size - 1];
        for (int i = 0, j = 0; i < size; ++i) {
            if (i != index)
                newBrackets[j++] = brackets[i];
        }
        delete[] brackets;
        brackets = newBrackets;
        --size;
    }

    void listBrackets() const {
        if (size == 0) {
            cout << "No rate brackets available.\n";
            return;
        }
        for (int i = 0; i < size; ++i) {
            cout << "Bracket #" << i << ": Age " << brackets[i].minAge << "-" << brackets[i].maxAge
                 << ", Premium = " << brackets[i].premium << "\n";
        }
    }

    void searchBracket(float minAge, float maxAge) const {
        bool found = false;
        for (int i = 0; i < size; ++i) {
            if (brackets[i].minAge >= minAge && brackets[i].maxAge <= maxAge) {
                cout << "Bracket #" << i << ": Age " << brackets[i].minAge << "-" << brackets[i].maxAge
                     << ", Premium = " << brackets[i].premium << "\n";
                found = true;
            }
        }
        if (!found)
            cout << "No matching brackets found in range.\n";
    }

protected:
    float findPremium(int age) {
        for (int i = 0; i < size; ++i) {
            if ((brackets + i)->minAge <= age && age <= (brackets + i)->maxAge)
                return (brackets + i)->premium;
        }
        return -1.0f; // Not found
    }
};

// BasicEngine derived class
class BasicEngine : public QuoteEngine {
public:
    float calculate(const Applicant* applicant) override {
        float basePremium = findPremium(applicant->age);
        return basePremium;
    }
};

// PremiumEngine derived class
class PremiumEngine : public QuoteEngine {
public:
    float calculate(const Applicant* applicant) override {
        float base = findPremium(applicant->age);
        return base < 0 ? -1 : base * 1.5f; // 50% surcharge
    }
};

// Clear input buffer
void clearInputBuffer() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

// New helper function to prompt engine index selection
void promptEngineIndex(int engineCount) {
    cout << "Select engine index";
    if (engineCount == 1) {
        cout << ": 0\n";
    } else {
        cout << " from: ";
        for (int i = 0; i < engineCount; ++i) {
            cout << i;
            if (i != engineCount - 1) cout << ", ";
        }
        cout << "\n";
    }
}

// Menu display function
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

int main() {
    int engineCount;
    cout << "Enter number of engines you want to create: ";
    cin >> engineCount;

    // Create dynamic array of engines
    QuoteEngine** engines = new QuoteEngine*[engineCount];

    // Select engine type for each engine
    for (int i = 0; i < engineCount; ++i) {
        int choice;
        cout << "Select type for engine #" << i + 1 << " (1 = Basic, 2 = Premium): ";
        cin >> choice;
        engines[i] = (choice == 1) ? static_cast<QuoteEngine*>(new BasicEngine())
                                   : static_cast<QuoteEngine*>(new PremiumEngine());
    }

    bool running = true;
    while (running) {
        displayMenu();
        int option;
        cin >> option;

        switch (option) {
        case 1: {
            int engineIndex;
            RateBracket rb;
            promptEngineIndex(engineCount);
            cin >> engineIndex;
            cout << "Enter minAge: ";
            cin >> rb.minAge;
            cout << "Enter maxAge: ";
            cin >> rb.maxAge;
            cout << "Enter premium: ";
            cin >> rb.premium;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                engines[engineIndex]->addBracket(rb);
                cout << "Bracket added! Current brackets for Engine #" << engineIndex << ":\n";
                engines[engineIndex]->listBrackets();
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 2: {
            int engineIndex, bracketIndex;
            promptEngineIndex(engineCount);
            cin >> engineIndex;
            cout << "Enter index of bracket to remove: ";
            cin >> bracketIndex;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                engines[engineIndex]->removeBracket(bracketIndex);
                cout << "Bracket removed! Current brackets for Engine #" << engineIndex << ":\n";
                engines[engineIndex]->listBrackets();
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 3: {
            int engineIndex;
            promptEngineIndex(engineCount);
            cin >> engineIndex;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                engines[engineIndex]->listBrackets();
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 4: {
            Applicant app;
            cout << "Enter VIN (max 16 characters): ";
            clearInputBuffer();
            cin.getline(app.vin, 17);
            cout << "Enter Age: ";
            cin >> app.age;
            cout << "Enter Policy Type: ";
            clearInputBuffer();
            cin.getline(app.type, 10);

            cout << "--- Quotes ---\n";
            for (int i = 0; i < engineCount; ++i) {
                float premium = engines[i]->calculate(&app);
                if (premium < 0)
                    cout << "Engine #" << i << ": No matching rate bracket found.\n";
                else
                    cout << "Engine #" << i << ": Premium = " << premium << " RWF\n";
            }
            break;
        }
        case 5: {
            int engineIndex;
            float minAge, maxAge;
            promptEngineIndex(engineCount);
            cin >> engineIndex;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                cout << "Enter search minimum age: ";
                cin >> minAge;
                cout << "Enter search maximum age: ";
                cin >> maxAge;
                engines[engineIndex]->searchBracket(minAge, maxAge);
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 6:
            running = false;
            break;
        default:
            cout << "Invalid option.\n";
        }
    }

    // Clean up dynamic memory
    for (int i = 0; i < engineCount; ++i)
        delete engines[i];
    delete[] engines;

    return 0;
}
