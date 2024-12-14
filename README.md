# QR Code Generator

This Python application generates and saves QR codes with a simple graphical user interface (GUI).

## Features

• Generates QR codes from user-supplied text.
• Saves generated QR codes as PNG files to the `qr-codes` directory.
• Includes a user-friendly GUI built with Pygame and a custom UI library (pgpyui). Adapt the code if your `pgpyui` differs.
• Handles potential errors (e.g., data overflow, file saving issues).

## Requirements

• Python  >  3.6
``` Terminal
pip install -r requirements.txt
```

## Installation

1. Clone this repository:  You'll need to provide a link here.  For example:  `git clone https://github.com/Memdved/qr-code-generator.git`
2. Navigate to the project directory: `cd qr-code-generator`
3. Install the required packages:
   
bash
   `pip install -r requirements.txt`
   (Create a requirements.txt file if you don't have one, listing the above packages.)

## Usage

1. Run the script: python main.py (or the name of your main Python file).
2. Enter the text you want to encode in the text area.
3. Click "Generate QR" to create the QR code.
4. Click "Save QR" to save the QR code as a PNG file. The file will be saved in the qr-codes directory.
5. Click "Clear QR" to clear the current QR code from the display.


## Error Handling

The application includes error handling for:

• **Data Overflow:** If the input text is too long for a QR code, an error message is displayed.
• **File Saving Errors:** If there are issues saving the QR code, an error message is displayed.


## Author

- Memdved

## License

MIT