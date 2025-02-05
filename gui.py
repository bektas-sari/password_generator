import customtkinter as ctk
import random
import string

# Şifre oluşturma fonksiyonu
def generate_password():
    try:
        length = int(entry_length.get())  # Kullanıcının girdiği uzunluğu al
        if length < 4:
            result_label.configure(text="Error: Minimum 4 characters!", text_color="red")
            return
        characters = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.configure(text=f"Generated: {password}", text_color="white")
    except ValueError:
        result_label.configure(text="Enter a valid number!", text_color="red")

# Arayüzü oluştur
ctk.set_appearance_mode("dark")  # Koyu mod
ctk.set_default_color_theme("blue")  # Mavi tema

app = ctk.CTk()
app.title("Password Generator")
app.geometry("400x300")
app.resizable(False, False)

# Şifre uzunluğu girişi
entry_length = ctk.CTkEntry(app, placeholder_text="Enter length", font=("Arial", 18))
entry_length.pack(pady=20)

# Şifre oluştur butonu
generate_button = ctk.CTkButton(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Sonuç etiketi
result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=20)

# Copyright Etiketi
copyright_label = ctk.CTkLabel(app, text="© 2025 - Bektas", font=("Arial", 12), text_color="gray")
copyright_label.pack(pady=10)


app.mainloop()
