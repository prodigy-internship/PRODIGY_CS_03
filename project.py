
# import tkinter as tk
# from tkinter import messagebox
# import re
# import json
# import os
# import secrets
# import string

# # Function to load common passwords
# def load_common_passwords(file_path=r'E:\Saved Games\password_strength_checker\pass.txt'):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             return set(p.strip() for p in file.readlines())
#     return set()

# COMMON_PASSWORDS = load_common_passwords()

# # Function to generate a secure password
# def generate_strong_password(length=12):
#     chars = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(chars) for _ in range(length))

# # Password checker function with dynamic length
# def check_password_strength(password, desired_length):
#     suggestions = []

#     if password in COMMON_PASSWORDS:
#         suggestions.append("This password is too common. Avoid using it.")
    
#     if len(password) < desired_length:
#         suggestions.append(f"Password must be at least {desired_length} characters.")
#     if not re.search(r"[A-Z]", password):
#         suggestions.append("Add at least one uppercase letter.")
#     if not re.search(r"[a-z]", password):
#         suggestions.append("Add at least one lowercase letter.")
#     if not re.search(r"\d", password):
#         suggestions.append("Include at least one number.")
#     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         suggestions.append("Use at least one special character.")
    
#     if suggestions:
#         strength = "Weak"
#         sample_password = generate_strong_password(desired_length)
#         suggestions.append(f"Try something like: {sample_password}")
#     else:
#         strength = "Strong"
#         suggestions = ["Great job! Your password is strong."]
    
#     return strength, suggestions

# # Save result to specific JSON file based on length
# def save_to_json(password, strength, suggestions, desired_length):
#     filename = f"E:/Saved Games/password_strength_checker/password_check_log_{desired_length}.json"
#     log = {
#         "password": password,
#         "strength": strength,
#         "suggestions": suggestions
#     }

#     if os.path.exists(filename):
#         with open(filename, 'r') as file:
#             try:
#                 data = json.load(file)
#             except json.JSONDecodeError:
#                 data = []
#     else:
#         data = []

#     data.append(log)
#     with open(filename, 'w') as file:
#         json.dump(data, file, indent=4)

# # GUI logic
# def evaluate_password():
#     password = password_var.get()
#     length_choice = length_var.get()
#     desired_length = 8 if length_choice == "8 Characters" else 10

#     strength, suggestions = check_password_strength(password, desired_length)

#     result_var.set(f"Strength: {strength}")
#     suggestions_text.delete("1.0", tk.END)
#     for s in suggestions:
#         suggestions_text.insert(tk.END, f"- {s}\n")

#     save_to_json(password, strength, suggestions, desired_length)

# def reset_fields():
#     password_var.set("")
#     result_var.set("")
#     suggestions_text.delete("1.0", tk.END)

# def toggle_password_visibility():
#     if show_var.get():
#         password_entry.config(show="")
#     else:
#         password_entry.config(show="*")

# # GUI setup
# root = tk.Tk()
# root.title("Password Strength Checker")
# root.geometry("520x500")
# root.resizable(False, False)

# tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)

# password_var = tk.StringVar()
# password_entry = tk.Entry(root, textvariable=password_var, show="*", width=40)
# password_entry.pack()

# show_var = tk.BooleanVar()
# tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password_visibility).pack(pady=2)

# tk.Label(root, text="Select password length requirement:", font=("Arial", 10)).pack(pady=5)
# length_var = tk.StringVar(value="8 Characters")
# tk.OptionMenu(root, length_var, "8 Characters", "10 Characters").pack()

# tk.Button(root, text="Check Strength", command=evaluate_password, bg="blue", fg="white").pack(pady=5)
# tk.Button(root, text="Reset", command=reset_fields, bg="red", fg="white").pack(pady=5)

# result_var = tk.StringVar()
# tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold")).pack(pady=5)

# tk.Label(root, text="Suggestions:", font=("Arial", 10)).pack()
# suggestions_text = tk.Text(root, height=10, width=60)
# suggestions_text.pack()

# tk.Label(root, text="Logs are saved to separate JSON files for each password length.", fg="gray").pack(pady=5)

# root.mainloop()















