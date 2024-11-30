import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to generate QR code
def generate_qrcode():
    data = entry_data.get()
    filename = entry_filename.get()

    if not data:
        messagebox.showerror("Error", "Data field cannot be empty!")
        return
    if not filename:
        filename = "qrcode.png"

    if not filename.endswith(".png"):
        filename += ".png"

    try:
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10, 
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        messagebox.showinfo("Success", f"QR Code saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {e}")

# Function to browse file location
def browse_file():
    filename = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if filename:
        entry_filename.delete(0, tk.END)
        entry_filename.insert(0, filename)

# Create the main tkinter window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")

# Data input field
tk.Label(root, text="Enter Data:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_data = tk.Entry(root, width=40)
entry_data.grid(row=0, column=1, padx=10, pady=10)

# Filename input field
tk.Label(root, text="Save As:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_filename = tk.Entry(root, width=30)
entry_filename.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Browse button
btn_browse = tk.Button(root, text="Browse", command=browse_file)
btn_browse.grid(row=1, column=2, padx=10, pady=10)

# Generate button
btn_generate = tk.Button(root, text="Generate QR Code", command=generate_qrcode, bg="green", fg="white")
btn_generate.grid(row=2, column=1, pady=20)

# Run the tkinter event loop
root.mainloop()
