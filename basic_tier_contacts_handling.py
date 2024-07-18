import streamlit as st
import json
import os

# Archivo JSON para almacenar contactos
json_file = 'contacts.json'

# Funciones CRUD usando JSON
def load_contacts():
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_contacts(contacts):
    with open(json_file, 'w') as file:
        json.dump(contacts, file, indent=4)

def create_contact(name, status, email, phone):
    contacts = load_contacts()
    contact_id = len(contacts) + 1
    contacts.append({
        'id': contact_id,
        'name': name,
        'status': status,
        'email': email,
        'telefono': phone
    })
    save_contacts(contacts)

def read_contacts():
    return load_contacts()

def update_contact(contact_id, name, status, email, phone):
    contacts = load_contacts()
    for contact in contacts:
        if contact['id'] == contact_id:
            contact['name'] = name
            contact['status'] = status
            contact['email'] = email
            contact['phone'] = phone
            break
    save_contacts(contacts)

def delete_contact(contact_id):
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact['id'] != contact_id]
    save_contacts(contacts)

# Interfaz de usuario
st.sidebar.title("Sales contacts management app")

menu = st.sidebar.selectbox("Menu", ["Create Contact", "List Contacts", "Update Contact", "Delete Contact"])

if menu == "Create Contact":
    st.sidebar.subheader("Add new contact")
    name = st.sidebar.text_input("Name")
    status = st.sidebar.selectbox("Status", ["Contacted", "Presented", "Sale"])
    email = st.sidebar.text_input("Email")
    phone = st.sidebar.text_input("Phone")
    if st.sidebar.button("Create Contact"):
        create_contact(name, status, email, phone)
        st.sidebar.success("Contacto creado con éxito")

elif menu == "List Contacts":
    st.subheader("Contact list")
    contacts = read_contacts()
    if contacts:
        st.table(contacts)
    else:
        st.write("No available contacts")

elif menu == "Update Contact":
    st.sidebar.subheader("Update a contact")
    contact_id = st.sidebar.number_input("ID of Contacto", min_value=1)
    name = st.sidebar.text_input("New Name")
    status = st.sidebar.selectbox("New Status", ["Contacted", "Presented", "Sale"])
    email = st.sidebar.text_input("New Email")
    phone = st.sidebar.text_input("New Phone")
    if st.sidebar.button("Update Contact"):
        update_contact(contact_id, name, status, email, phone)
        st.sidebar.success("Contact updated successfully")

elif menu == "Delete Contact":
    st.sidebar.subheader("Eliminate a contact")
    contact_id = st.sidebar.number_input("ID of contact to eliminate", min_value=1)
    if st.sidebar.button("Delete Contact"):
        delete_contact(contact_id)
        st.sidebar.success("Contact deleted succesfully")
