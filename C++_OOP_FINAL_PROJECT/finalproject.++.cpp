#include <iostream>
#include <cstring>
using namespace std;

struct Contact { char name[30], phone[15]; };

class ContactBase {
public:
    Contact info;
    ContactBase(const char* n, const char* p) {
        strcpy(info.name, n); strcpy(info.phone, p);
    }
    virtual void display() = 0;
    virtual ~ContactBase() {}
};

class FamilyContact : public ContactBase {
public:
    FamilyContact(const char* n, const char* p) : ContactBase(n, p) {}
    void display() override {
        cout << "[Family] " << info.name << " - " << info.phone << endl;
    }
};

class BusinessContact : public ContactBase {
public:
    BusinessContact(const char* n, const char* p) : ContactBase(n, p) {}
    void display() override {
        cout << "[Business] " << info.name << " - " << info.phone << endl;
    }
};

struct Group {
    char name[20];
    ContactBase** members;
    int memberCount;
    Group(const char* n) : memberCount(0) {
        strcpy(name, n); members = new ContactBase*[0];
    }
    void addMember(ContactBase* c) {
        ContactBase** temp = new ContactBase*[memberCount + 1];
        for (int i = 0; i < memberCount; i++) temp[i] = members[i];
        temp[memberCount++] = c;
        delete[] members; members = temp;
    }
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
    void displayGroup() {
        cout << "Group: " << name << endl;
        for (int i = 0; i < memberCount; i++) members[i]->display();
    }
    ~Group() { delete[] members; }
};

Group** groups = nullptr;
int groupCount = 0;

void addGroup(const char* name) {
    Group** temp = new Group*[groupCount + 1];
    for (int i = 0; i < groupCount; i++) temp[i] = groups[i];
    temp[groupCount++] = new Group(name);
    delete[] groups; groups = temp;
}

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

int main() {
    ContactBase* f1 = new FamilyContact("rodrigue", "0785530043");
    ContactBase* b1 = new BusinessContact("murungi", "0727776540");

    addGroup("Friends");
    groups[0]->addMember(f1);
    groups[0]->addMember(b1);

    groups[0]->displayGroup();

    groups[0]->removeMember("murungi");
    cout << "\nAfter removing murungi:\n";
    groups[0]->displayGroup();

    removeGroup("Friends");
    delete f1; delete b1;
    return 0;
}
