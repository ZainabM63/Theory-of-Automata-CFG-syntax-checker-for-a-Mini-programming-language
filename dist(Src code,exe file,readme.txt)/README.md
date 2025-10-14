CFG-Based Syntax Checker

This application is a Context-Free Grammar (CFG)-based Syntax Checker with Parse Tree Visualization and Derivation Steps support.
It provides syntax validation for a mini programming language using the Lark parser and displays output in both text and image formats.

🛠 Features

✔ Syntax checking for a mini programming language

✔ Pretty-printed parse tree and derivation steps

✔ Parse tree image generation (using Graphviz)

✔ Save output to .txt file

✔ GUI-based interface (built with Tkinter)

💻 System Requirements

Python is NOT required (standalone EXE)

Windows OS

[Optional] Graphviz installed for parse tree image generation

📦 How to Use

Run the EXE
Double-click cfg_syntax_checker.exe to launch the application.

Enter Code
Type your mini-language code in the input box.

Check Syntax
Click the “Check Syntax” button.

✅ If syntax is valid: parse tree and derivation steps will be shown.

❌ If there’s an error: error details will be displayed.

View Parse Tree Image
If Graphviz is installed, a file named parse_tree.png will be generated and opened automatically.

Save Output
Click “Save Output” to export the results (parse tree and derivation steps) to a .txt file.

📄 Supported Grammar

The mini language supports:

🔹 Variable Declaration
int x;
float y = 10;

🔹 Assignment
x = 5 + 3 * 2;

🔹 Arithmetic Expressions

Supports +, -, *, / with proper precedence

Parentheses for grouping:

(a + b) * c

⚠ Graphviz Warning

If Graphviz is not installed, the application will:

Show a warning once per session

Offer to download Graphviz

Still work normally, but the parse tree image will not be generated

To enable image generation:
👉 Download Graphviz: https://graphviz.org/download

👉 Add the Graphviz bin folder to your system PATH

📂 Files Generated
File Name	Description
parse_tree.png	Parse tree image (if Graphviz is available)
<your_output>.txt	Output saved via "Save Output"
👨‍💻 Developer Notes

Developed using Python, Tkinter, Lark, and Graphviz

Grammar defined using Lark’s LALR parser with token precedence