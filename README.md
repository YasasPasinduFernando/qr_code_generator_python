# QR Code Generator

![QR Code Generator Icon](assets/qrcode-icon.png)

A simple, user-friendly QR Code generator built with Python. It allows users to generate QR codes from custom data, customize the appearance, and save the QR codes as PNG images. This application features real-time previews and supports adjustable error correction levels.

## Features

- ✨ **User-friendly interface** built with `tkinter`.
- 🎨 **Customizable QR codes** with user input.
- 🔧 **Save QR codes** as `.png` files.
- 🔢 **Adjustable error correction levels** (Low, Medium, Quartile, High).
- 🔍 **Preview generated QR codes** in real-time.
- 🔄 **Lightweight and responsive design**.

## Installation

### Prerequisites

Ensure you have Python 3.7 or later installed. Additionally, you will need the following Python libraries:

- `qrcode`
- `tkinter` (comes with standard Python)
- `Pillow` (for image handling)

To install the necessary libraries, use the following command:

```bash
pip install qrcode[pil] Pillow
