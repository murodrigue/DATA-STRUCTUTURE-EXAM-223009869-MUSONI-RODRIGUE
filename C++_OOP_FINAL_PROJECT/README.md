ASSIGNED TASKS:

Develop a C++ application that:

1)Manages contacts (Family or Business).
2.Organizes them into groups
3.Allows dynamic addition/removal of contacts and groups
4.Uses Object-Oriented Programming (OOP) with inheritance, polymorphism, and dynamic memory

HOW TASKS ARE COMPLETED:

1.ContactBase: An abstract base class representing a generic contact.
2.FamilyContact & BusinessContact: Derived classes with customized display behavior.
3.Group: Manages a dynamic list of contacts using raw pointers.
4.Global Array: Groups are stored in a dynamically resizing global array.
5.OOP Principles: Polymorphism (display()), encapsulation, and dynamic memory are applied throughout.
6.Memory Management: Manual memory allocation and cleanup ensure no memory leaks.

ANNOTATED CODES:

#include <iostream>   // For input/output
#include <cstring>    // For string copying and comparison
using namespace std;

// Contact structure holds name and phone number
struct Contact { 
    char name[30], phone[15]; 
};

// Abstract base class for a contact
class ContactBase {
public:
    Contact info;  // Common contact info
    ContactBase(const char* n, const char* p) {
        strcpy(info.name, n); 
        strcpy(info.phone, p);
    }
    virtual void display() = 0; // Pure virtual function
    virtual ~ContactBase() {}   // Virtual destructor
};

// Family contact with custom display
class FamilyContact : public ContactBase {
public:
    FamilyContact(const char* n, const char* p) : ContactBase(n, p) {}
    void display() override {
        cout << "[Family] " << info.name << " - " << info.phone << endl;
    }
};

// Business contact with custom display
class BusinessContact : public ContactBase {
public:
    BusinessContact(const char* n, const char* p) : ContactBase(n, p) {}
    void display() override {
        cout << "[Business] " << info.name << " - " << info.phone << endl;
    }
};

// Group structure holds dynamic array of contact pointers
struct Group {
    char name[20];
    ContactBase** members;  // Dynamic array of ContactBase pointers
    int memberCount;

    Group(const char* n) : memberCount(0) {
        strcpy(name, n); 
        members = new ContactBase*[0]; // Initially empty
    }

    // Add new member to group
    void addMember(ContactBase* c) {
        ContactBase** temp = new ContactBase*[memberCount + 1];
        for (int i = 0; i < memberCount; i++) temp[i] = members[i];
        temp[memberCount++] = c;
        delete[] members; members = temp;
    }

    // Remove member by name
    void removeMember(const char* n) {
        int idx = -1;
        for (int i = 0; i < memberCount; i++)
            if (strcmp(members[i]->info.name, n) == 0) { idx = i; break; }
        if (idx >= 0) {
            ContactBase** temp = new ContactBase*[memberCount - 1];
            for (int i = 0, j = 0; i < memberCount; i++)
                if (i != idx) temp[j++] = members[i];
            delete[] members; members = temp; memberCount--;
        }
    }

    // Print all members of the group
    void displayGroup() {
        cout << "Group: " << name << endl;
        for (int i = 0; i < memberCount; i++) members[i]->display();
    }

    ~Group() { delete[] members; }  // Clean up memory
};

// Global dynamic list of groups
Group** groups = nullptr;
int groupCount = 0;

// Add a new group
void addGroup(const char* name) {
    Group** temp = new Group*[groupCount + 1];
    for (int i = 0; i < groupCount; i++) temp[i] = groups[i];
    temp[groupCount++] = new Group(name);
    delete[] groups; groups = temp;
}

// Remove a group by name
void removeGroup(const char* name) {
    int idx = -1;
    for (int i = 0; i < groupCount; i++)
        if (strcmp(groups[i]->name, name) == 0) { idx = i; break; }
    if (idx >= 0) {
        delete groups[idx];
        Group** temp = new Group*[groupCount - 1];
        for (int i = 0, j = 0; i < groupCount; i++)
            if (i != idx) temp[j++] = groups[i];
        delete[] groups; groups = temp; groupCount--;
    }
}

// Main program for demonstration
int main() {
    // Create contacts
    ContactBase* f1 = new FamilyContact("rodrigue", "0785530043");
    ContactBase* b1 = new BusinessContact("murungi", "0727776540");

    // Create group and add members
    addGroup("Friends");
    groups[0]->addMember(f1);
    groups[0]->addMember(b1);

    // Display group contents
    groups[0]->displayGroup();

    // Remove a member and re-display
    groups[0]->removeMember("murungi");
    cout << "\nAfter removing murungi:\n";
    groups[0]->displayGroup();

    // Cleanup memory
    removeGroup("Friends");
    delete f1; delete b1;
    return 0;
}
