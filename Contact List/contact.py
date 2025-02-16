import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(contacts)
        refresh_list()
    else:
        messagebox.showerror("Error", "Name and Phone Number are required!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    results = [c for c in contacts if query in c["name"] or query in c["phone"]]
    
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected_index = contact_list.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Select a contact to update")
        return
    
    index = selected_index[0]
    contact = contacts[index]
    
    new_name = simpledialog.askstring("Update Contact", "Enter New Name:", initialvalue=contact["name"])
    new_phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:", initialvalue=contact["phone"])
    new_email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contact["email"])
    new_address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contact["address"])
    
    contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
    save_contacts(contacts)
    refresh_list()

def delete_contact():
    selected_index = contact_list.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Select a contact to delete")
        return
    
    index = selected_index[0]
    contacts.pop(index)
    save_contacts(contacts)
    refresh_list()

def refresh_list():
    view_contacts()

contacts = load_contacts()

root = tk.Tk()
root.title("Contact Book")

frame = tk.Frame(root)
frame.pack(pady=10)

contact_list = tk.Listbox(frame, width=50, height=10)
contact_list.pack()

btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.pack(pady=2)

btn_view = tk.Button(root, text="View Contacts", command=view_contacts)
btn_view.pack(pady=2)

btn_search = tk.Button(root, text="Search Contact", command=search_contact)
btn_search.pack(pady=2)

btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.pack(pady=2)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.pack(pady=2)

refresh_list()
root.mainloop()