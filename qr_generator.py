import qrcode
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

class QRCodeGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        self.root.minsize(500, 650)  # Increased minimum height for footer
        self.root.geometry("500x650")
        self.root.resizable(True, True)
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        
        self.setup_styles()
        self.create_ui()
        
        self.preview_image = None
        
    def setup_styles(self):
        self.style = ttk.Style()
        
        bg_color = "#ffffff"
        accent_color = "#1976D2"
        self.root.configure(bg=bg_color)
        
        # Previous styles remain the same...
        self.style.configure("Main.TFrame", background=bg_color)
        self.style.configure("TLabel", background=bg_color, font=("Segoe UI", 10))
        self.style.configure("Header.TLabel", background=accent_color, foreground="white", 
                           font=("Segoe UI", 16, "bold"), padding=10)
        self.style.configure("TButton", font=("Segoe UI", 10), padding=5)
        self.style.configure("Generate.TButton", font=("Segoe UI", 11, "bold"), padding=10)
        self.style.configure("TEntry", padding=5)
        self.style.configure("TCombobox", padding=5)
        self.style.configure("TLabelframe", background=bg_color)
        self.style.configure("TLabelframe.Label", background=bg_color, font=("Segoe UI", 10, "bold"))
        
        # New style for footer
        self.style.configure(
            "Footer.TLabel",
            background="#f0f0f0",
            foreground="#666666",
            font=("Segoe UI", 9),
            padding=8
        )

    def create_ui(self):
        # Previous UI elements remain the same...
        header = ttk.Label(
            self.root,
            text="QR Code Generator",
            style="Header.TLabel",
            anchor="center"
        )
        header.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 20))

        main_frame = ttk.Frame(self.root, padding=20, style="Main.TFrame")
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20)
        main_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(main_frame, text="Enter Data:").grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.data_entry = ttk.Entry(main_frame)
        self.data_entry.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 20))

        settings_frame = ttk.LabelFrame(
            main_frame,
            text="QR Code Settings",
            padding=15
        )
        settings_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 20))
        settings_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(settings_frame, text="Save As:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.filename_entry = ttk.Entry(settings_frame)
        self.filename_entry.grid(row=0, column=1, sticky="ew", padx=5)
        
        browse_btn = ttk.Button(
            settings_frame,
            text="Browse",
            command=self.browse_file
        )
        browse_btn.grid(row=0, column=2, padx=(5, 0))

        ttk.Label(settings_frame, text="Error Correction:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.error_level = ttk.Combobox(
            settings_frame,
            values=["Low", "Medium", "Quartile", "High"],
            state="readonly"
        )
        self.error_level.set("High")
        self.error_level.grid(row=1, column=1, sticky="w", pady=5)

        generate_btn = ttk.Button(
            main_frame,
            text="Generate QR Code",
            command=self.generate_qrcode,
            style="Generate.TButton"
        )
        generate_btn.grid(row=3, column=0, columnspan=3, pady=20)

        preview_frame = ttk.LabelFrame(
            self.root,
            text="Preview",
            padding=15
        )
        preview_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=(0, 20))
        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_rowconfigure(0, weight=1)

        self.preview_label = ttk.Label(preview_frame, text="QR code preview will appear here")
        self.preview_label.grid(row=0, column=0, sticky="nsew")

        # Create footer frame with gradient-like effect
        footer_frame = tk.Frame(self.root, bg="#f0f0f0", height=40)
        footer_frame.grid(row=3, column=0, sticky="ew")
        footer_frame.grid_columnconfigure(0, weight=1)
        
        # Add bottom border to footer
        border_frame = tk.Frame(footer_frame, bg="#e0e0e0", height=1)
        border_frame.grid(row=0, column=0, sticky="ew")
        
        # Creator credit
        creator_label = ttk.Label(
            footer_frame,
            text="Created by Yasas Pasindu Fernando",
            style="Footer.TLabel",
            anchor="center"
        )
        creator_label.grid(row=1, column=0, sticky="ew")

    # Rest of the methods (browse_file, generate_qrcode) remain the same...
    def browse_file(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            initialfile="qrcode.png"
        )
        if filename:
            self.filename_entry.delete(0, tk.END)
            self.filename_entry.insert(0, filename)

    def generate_qrcode(self):
        data = self.data_entry.get().strip()
        filename = self.filename_entry.get().strip()

        if not data:
            messagebox.showerror("Error", "Please enter data for the QR code!")
            return

        if not filename:
            filename = "qrcode.png"
        if not filename.endswith(".png"):
            filename += ".png"

        try:
            error_levels = {
                "Low": qrcode.constants.ERROR_CORRECT_L,
                "Medium": qrcode.constants.ERROR_CORRECT_M,
                "Quartile": qrcode.constants.ERROR_CORRECT_Q,
                "High": qrcode.constants.ERROR_CORRECT_H
            }

            qr = qrcode.QRCode(
                version=1,
                error_correction=error_levels[self.error_level.get()],
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filename)

            # Update preview
            preview_size = (200, 200)
            preview = img.copy()
            preview.thumbnail(preview_size)
            photo = ImageTk.PhotoImage(preview)
            
            self.preview_label.configure(image=photo, text="")
            self.preview_label.image = photo

            messagebox.showinfo(
                "Success",
                f"QR Code successfully saved as:\n{os.path.basename(filename)}"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to generate QR Code:\n{str(e)}"
            )

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QRCodeGenerator()
    app.run()