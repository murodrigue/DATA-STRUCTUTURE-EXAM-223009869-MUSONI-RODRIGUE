# C++ OOP Final Project – Contact & Group Organizer

## Assigned Task
- Define struct Contact with name and phone
- Create abstract class ContactBase with virtual void display()
- Derive FamilyContact and BusinessContact
- Use dynamic ContactBase* array for polymorphic behavior
- Create Group struct with ContactBase** members
- Implement addMember(), removeMember(), addGroup(), removeGroup()

## How It Works
- Contacts are created as Family or Business types
- All are stored as ContactBase* and displayed using polymorphism
- Groups hold dynamic arrays of contact pointers
- You can add or remove members and groups dynamically

## Code Summary
- Contact: stores name and phone
- ContactBase: base class for all contacts
- FamilyContact, BusinessContact: override display()
- Group: holds contact pointers and supports add/remove/display
- Global group list is resized on add/remove

## main() Demo
- Creates two contacts (rodrigue and murungi)
- Adds them to group "Friends"
- Displays group
- Removes murungi and displays again
- Cleans memory
## that are my codes
#include <iostream>      // For input/output operations
#include <cstring>       // For using string manipulation functions like strcpy and strcmp
using namespace std;     // To avoid writing std:: before standard library functions

// Define a simple structure to hold contact name and phone number
struct Contact { 
    char name[30], phone[15]; 
};

// Abstract base class for different types of contacts
class ContactBase {
public:
    Contact info;  // Holds the contact details

    // Constructor that initializes the contact info using provided name and phone
    ContactBase(const char* n, const char* p) {
        strcpy(info.name, n);           // Copy name into the structure
        strcpy(info.phone, p);          // Copy phone number into the structure
    }

    virtual void display() = 0;         // Pure virtual function to display contact details
    virtual ~ContactBase() {}           // Virtual destructor to ensure proper cleanup
};

// Derived class representing a family contact
class FamilyContact : public ContactBase {
public:
    // Constructor passes data to base class constructor
    FamilyContact(const char* n, const char* p) : ContactBase(n, p) {}

    // Override display to show that it's a family contact
    void display() override {
        cout << "[Family] " << info.name << " - " << info.phone << endl;
    }
};

// Derived class representing a business contact
class BusinessContact : public ContactBase {
public:
    // Constructor passes data to base class constructor
    BusinessContact(const char* n, const char* p) : ContactBase(n, p) {}

    // Override display to show that it's a business contact
    void display() override {
        cout << "[Business] " << info.name << " - " << info.phone << endl;
    }
};

// Group structure that holds multiple contacts
struct Group {
    char name[20];              // Name of the group
    ContactBase** members;      // Dynamic array of pointers to ContactBase
    int memberCount;            // Current number of members

    // Constructor to initialize the group with a name and empty members
    Group(const char* n) : memberCount(0) {
        strcpy(name, n);
        members = new ContactBase*[0];  // Initially empty
    }

    // Add a new member to the group
    void addMember(ContactBase* c) {
        ContactBase** temp = new ContactBase*[memberCount + 1]; // Allocate new array
        for (int i = 0; i < memberCount; i++) 
            temp[i] = members[i];          // Copy old members
        temp[memberCount++] = c;           // Add new member
        delete[] members;                  // Free old array
        members = temp;                    // Update pointer
    }

    // Remove a member by name
    void removeMember(const char* n) {
        int idx = -1;
        // Find index of member to remove
        for (int i = 0; i < memberCount; i++)
            if (strcmp(members[i]->info.name, n) == 0) { 
                idx = i; 
                break; 
            }
        if (idx >= 0) {
            ContactBase** temp = new ContactBase*[memberCount - 1]; // New array for remaining
            for (int i = 0, j = 0; i < memberCount; i++)
                if (i != idx) temp[j++] = members[i];               // Copy all except the one to remove
            delete[] members; members = temp; memberCount--;       // Update
        }
    }

    // Display all members of the group
    void displayGroup() {
        cout << "Group: " << name << endl;
        for (int i = 0; i < memberCount; i++) 
            members[i]->display();         // Call display for each member
    }

    // Destructor to free memory
    ~Group() { 
        delete[] members; 
    }
};

// Global variables for managing multiple groups
Group** groups = nullptr;  // Array of pointers to groups
int groupCount = 0;        // Number of groups

// Add a new group
void addGroup(const char* name) {
    Group** temp = new Group*[groupCount + 1]; // Allocate space for one more group
    for (int i = 0; i < groupCount; i++) 
        temp[i] = groups[i];                   // Copy existing groups
    temp[groupCount++] = new Group(name);      // Create and add the new group
    delete[] groups; groups = temp;            // Update pointer
}

// Remove a group by name
void removeGroup(const char* name) {
    int idx = -1;
    // Find index of group to remove
    for (int i = 0; i < groupCount; i++)
        if (strcmp(groups[i]->name, name) == 0) { 
            idx = i; 
            break; 
        }
    if (idx >= 0) {
        delete groups[idx];                           // Delete the group
        Group** temp = new Group*[groupCount - 1];    // Create new array
        for (int i = 0, j = 0; i < groupCount; i++)
            if (i != idx) temp[j++] = groups[i];      // Copy all except the one removed
        delete[] groups; groups = temp; groupCount--; // Update
    }
}

// Main function demonstrating usage
int main() {
    // Create contacts
    ContactBase* f1 = new FamilyContact("rodrigue", "0785530043");
    ContactBase* b1 = new BusinessContact("murungi", "0727776540");

    // Create a group and add contacts to it
    addGroup("Friends");
    groups[0]->addMember(f1);
    groups[0]->addMember(b1);

    // Display the group
    groups[0]->displayGroup();

    // Remove one contact and display again
    groups[0]->removeMember("murungi");
    cout << "\nAfter removing murungi:\n";
    groups[0]->displayGroup();

    // Clean up
    removeGroup("Friends");
    delete f1; delete b1;

    return 0;
}
