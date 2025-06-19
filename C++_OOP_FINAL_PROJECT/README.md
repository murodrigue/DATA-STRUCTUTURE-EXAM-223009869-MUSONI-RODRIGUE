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
