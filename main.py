import qrcode
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

class QRCodeGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f2f5")
        
        # Configure styles
        self.setup_styles()
        
        # Setup UI components
        self.create_ui()
        
        # Preview image holder
        self.preview_image = None
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure common styles
        self.style.configure(
            "TLabel",
            font=("Segoe UI", 11),
            background="#f0f2f5"
        )
        self.style.configure(
            "Header.TLabel",
            font=("Segoe UI", 16, "bold"),
            background="#1a73e8",
            foreground="white",
            padding=10
        )
        self.style.configure(
            "Footer.TLabel",
            font=("Segoe UI", 9),
            background="#f0f2f5",
            foreground="#666666"
        )
        self.style.configure(
            "TButton",
            font=("Segoe UI", 11),
            padding=5
        )
        self.style.configure(
            "Generate.TButton",
            font=("Segoe UI", 11, "bold"),
            background="#1a73e8",
            foreground="white"
        )

    def create_ui(self):
        # Header
        header = ttk.Label(
            self.root,
            text="QR Code Generator",
            style="Header.TLabel",
            anchor="center"
        )
        header.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Main content frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.configure(style="Main.TFrame")

        # Data input
        ttk.Label(main_frame, text="Enter Data:").grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.data_entry = ttk.Entry(main_frame, width=50)
        self.data_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 15))

        # QR Code settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="QR Code Settings", padding=10)
        settings_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 15))

        # File name input
        ttk.Label(settings_frame, text="Save As:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.filename_entry = ttk.Entry(settings_frame, width=35)
        self.filename_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Browse button
        ttk.Button(
            settings_frame,
            text="Browse",
            command=self.browse_file
        ).grid(row=0, column=2, padx=5, pady=5)

        # Error correction level
        ttk.Label(settings_frame, text="Error Correction:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.error_level = ttk.Combobox(
            settings_frame,
            values=["Low", "Medium", "Quartile", "High"],
            state="readonly",
            width=15
        )
        self.error_level.set("High")
        self.error_level.grid(row=1, column=1, sticky="w", pady=5)

        # Generate button
        generate_btn = ttk.Button(
            main_frame,
            text="Generate QR Code",
            command=self.generate_qrcode,
            style="Generate.TButton"
        )
        generate_btn.grid(row=3, column=0, columnspan=2, pady=15)

        # Preview frame
        self.preview_label = ttk.Label(main_frame, text="Preview will appear here")
        self.preview_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Footer
        footer = ttk.Label(
            self.root,
            text="Developed with ❤️ using Python | v1.1",
            style="Footer.TLabel"
        )
        footer.grid(row=2, column=0, columnspan=3, pady=10)

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

        # Validation
        if not data:
            messagebox.showerror("Error", "Please enter data for the QR code!")
            return

        if not filename:
            filename = "qrcode.png"
        if not filename.endswith(".png"):
            filename += ".png"

        try:
            # Error correction mapping
            error_levels = {
                "Low": qrcode.constants.ERROR_CORRECT_L,
                "Medium": qrcode.constants.ERROR_CORRECT_M,
                "Quartile": qrcode.constants.ERROR_CORRECT_Q,
                "High": qrcode.constants.ERROR_CORRECT_H
            }

            # Generate QR code
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

            # Show preview
            preview_size = (150, 150)
            preview = img.copy()
            preview.thumbnail(preview_size)
            photo = ImageTk.PhotoImage(preview)
            
            self.preview_label.configure(image=photo, text="")
            self.preview_label.image = photo  # Keep a reference

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