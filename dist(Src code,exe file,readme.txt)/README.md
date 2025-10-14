## 👩‍💻 Developer

**Author:** Zainab Mughal

**Focus:** Cybersecurity & Web App Development

---

# CFG-Based Syntax Checker

This application is a **Context-Free Grammar (CFG)-based Syntax Checker** with **Parse Tree Visualization** and **Derivation Steps** support.  
It provides syntax validation for a mini programming language using the **Lark parser** and displays output in both **text** and **image** formats.

---

## 🛠 FEATURES
- Syntax checking for a mini programming language  
- Pretty-printed parse tree and derivation steps  
- Parse tree image generation (using **Graphviz**)  
- Save output to `.txt` file  
- GUI-based interface (built with **Tkinter**)  

---

## 💻 SYSTEM REQUIREMENTS
- **Python is NOT required** (standalone EXE)  
- **Windows OS**  
- [Optional] **Graphviz** installed for parse tree image generation  

---

## 📦 HOW TO USE
1. **Run the EXE**  
   Double-click `cfg_syntax_checker.exe` to launch the application.

2. **Enter Code**  
   Type your mini-language code in the input box.

3. **Check Syntax**  
   Click the **“Check Syntax”** button.  
   - ✅ If syntax is valid: parse tree and derivation steps will be shown.  
   - ❌ If there’s an error: error details will be displayed.

4. **View Parse Tree Image**  
   If Graphviz is installed, a file named **`parse_tree.png`** will be generated and opened automatically.

5. **Save Output**  
   Click **“Save Output”** to export the results (parse tree and derivation steps) to a `.txt` file.

---

## 📄 SUPPORTED GRAMMAR

### 🔹 Variable Declaration
```c
int x;
float y = 10;
````

### 🔹 Assignment

```c
x = 5 + 3 * 2;
```

### 🔹 Arithmetic Expressions

Supports `+`, `-`, `*`, `/` with proper precedence.
Parentheses for grouping:

```c
(a + b) * c
```

---

## ⚠ GRAPHVIZ WARNING

If **Graphviz** is **not installed**, the application will:

* Show a warning once per session
* Offer to download Graphviz
* Still work normally, but the parse tree image will **not** be generated

To enable image generation:
👉 Download Graphviz: [https://graphviz.org/download](https://graphviz.org/download)
👉 Add the Graphviz `bin` folder to your **system PATH**

---

## 📂 FILES GENERATED

| File Name           | Description                                 |
| ------------------- | ------------------------------------------- |
| `parse_tree.png`    | Parse tree image (if Graphviz is available) |
| `<your_output>.txt` | Output saved via "Save Output"              |

---

## 👨‍💻 DEVELOPER NOTES

* Developed using **Python**, **Tkinter**, **Lark**, and **Graphviz**
* Grammar defined using **Lark’s LALR parser** with token precedence

---

```

✅ **Instructions:**  
- Open VS Code  
- Create a file named `README.md`  
- Paste the above **as-is**  
- Then click **“Preview” (Ctrl+Shift+V)** to see the formatted Markdown  

Would you like me to make a **smaller version (under 80 lines)** suitable for Fiverr or GitHub description too?
```
