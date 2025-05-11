import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Center the window on screen
def center_window(win, width=400, height=300):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")

# Main window setup
root = tk.Tk()
root.title("JPEG to PNG Converter")
center_window(root)
root.configure(bg="#2c3e50")
root.resizable(False, False)

# Global variable to store the image
im1 = None

# Heading label
label_title = tk.Label(root, text="Image Converter", bg="#2c3e50", fg="#ecf0f1",
                       font=("Helvetica", 20, "bold"))
label_title.pack(pady=20)

# Button style
button_style = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "#3498db",
    "fg": "white",
    "activebackground": "#2980b9",
    "activeforeground": "white",
    "relief": "flat",
    "padx": 20,
    "pady": 10,
    "bd": 0
}

# Function to import JPEG file
def getJPG():
    global im1
    file_path = filedialog.askopenfilename(
        filetypes=[("JPEG files", "*.jpg;*.jpeg")],
        title="Select a JPEG file"
    )
    if file_path:
        try:
            im1 = Image.open(file_path)
            messagebox.showinfo("Success", f"Loaded:\n{os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image:\n{e}")

# Function to convert and save as PNG
def convertToPNG():
    global im1
    if im1 is None:
        messagebox.showerror("Error", "No JPEG file selected!")
    else:
        file_path = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[("PNG files", "*.png")],
            title="Save as PNG"
        )
        if file_path:
            try:
                im1.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully as PNG!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save image:\n{e}")

# Import button
btn_import = tk.Button(root, text="Import JPEG File", command=getJPG, **button_style)
btn_import.pack(pady=10)

# Convert button
btn_convert = tk.Button(root, text="Convert to PNG", command=convertToPNG, **button_style)
btn_convert.pack(pady=10)

# Footer label
label_footer = tk.Label(root, text="Developed by Shaik Mohammad Haneef using Python & Tkinter",
                        bg="#2c3e50", fg="#95a5a6", font=("Helvetica", 9))
label_footer.pack(side="bottom", pady=10)

# Start GUI loop
root.mainloop()
