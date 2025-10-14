from lark import Lark, Token, Tree, UnexpectedInput
from graphviz import Digraph
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os
import subprocess
import webbrowser

# -----------------------------
# Graphviz Check & Prompt Logic
# -----------------------------
graphviz_warning_suppressed = False  # Session flag to prevent repeat

def try_common_graphviz_paths():
    likely_paths = [
        r"C:\Program Files\Graphviz\bin\dot.exe",
        r"C:\Program Files (x86)\Graphviz2.38\bin\dot.exe"
    ]
    for path in likely_paths:
        if os.path.exists(path):
            os.environ["PATH"] += os.pathsep + os.path.dirname(path)
            return True
    return False

def check_graphviz_installed():
    try:
        subprocess.run(["dot", "-V"], capture_output=True, check=True)
        return True
    except:
        return try_common_graphviz_paths()

def prompt_graphviz_warning():
    global graphviz_warning_suppressed
    if graphviz_warning_suppressed:
        return
    if not check_graphviz_installed():
        response = messagebox.askyesno(
            "Graphviz Not Found",
            "Graphviz is not installed or its path is not set.\n\n"
            "Parse tree images (parse_tree.png) will NOT be generated unless Graphviz is available.\n\n"
            "Would you like to download Graphviz now?"
        )
        if response:
            webbrowser.open("https://graphviz.org/download")

        suppress = messagebox.askyesno(
            "Disable Future Warnings?",
            "Do you want to disable this Graphviz warning for the rest of this session?"
        )
        if suppress:
            graphviz_warning_suppressed = True


# Define CFG for mini programming language
grammar = '''
?start: statement+

statement: decl_stmt
         | assign_stmt

decl_stmt: TYPE IDENTIFIER ("=" expr)? ";"
assign_stmt: IDENTIFIER "=" expr ";"

?expr: term
     | expr "+" term   -> add
     | expr "-" term   -> sub

?term: factor
     | term "*" factor -> mul
     | term "/" factor -> div

?factor: IDENTIFIER
       | NUMBER
       | "(" expr ")"

TYPE.2: "int" | "float"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /[0-9]+/

%import common.WS
%ignore WS
'''

parser = Lark(grammar, parser="lalr", start="start", keep_all_tokens=True)

# -----------------------------
# Draw Parse Tree
# -----------------------------
def draw_tree(tree: Tree, filename="parse_tree"):
    dot = Digraph()
    counter = [0]

    def add_nodes(node, parent_id=None):
        node_id = str(counter[0])
        counter[0] += 1

        label = node.data if isinstance(node, Tree) else str(node)
        dot.node(node_id, label)

        if parent_id is not None:
            dot.edge(parent_id, node_id)

        if isinstance(node, Tree):
            for child in node.children:
                add_nodes(child, node_id)

    add_nodes(tree)
    dot.render(filename, format='png', cleanup=True)

# -----------------------------
# Derivation Steps
# -----------------------------
def get_derivation_steps(tree):
    steps = []

    def expand(node):
        if isinstance(node, Tree):
            rhs = []
            for child in node.children:
                if isinstance(child, Tree):
                    rhs.append(child.data)
                elif isinstance(child, Token):
                    rhs.append(str(child))
            steps.append(f"{node.data} → {' '.join(rhs)}")
            for child in node.children:
                if isinstance(child, Tree):
                    expand(child)

    expand(tree)
    return steps

# -----------------------------
# Syntax Checking
# -----------------------------
def check_syntax():
    code = text_input.get("1.0", END).strip()
    if not code:
        messagebox.showwarning("Input Required", "Please enter some code.")
        return

    try:
        tree = parser.parse(code)
        result_output.config(text="✅ Syntax Valid!")

        # Show Parse Tree
        tree_output.delete("1.0", END)
        tree_output.insert(END, "=== Parse Tree ===\n")
        tree_output.insert(END, tree.pretty())

        # Show Derivation Steps
        derivation_steps = get_derivation_steps(tree)
        tree_output.insert(END, "\n\n=== Derivation Steps ===\n")
        for step in derivation_steps:
            tree_output.insert(END, step + "\n")

        # Visual tree
        draw_tree(tree)
        try:
            os.startfile("parse_tree.png")
        except:
            messagebox.showwarning("Graphviz PNG Missing", "Parse tree image could not be opened. Ensure Graphviz is installed.")

    except UnexpectedInput as e:
        result_output.config(text="❌ Syntax Error")
        tree_output.delete("1.0", END)
        tree_output.insert(END, str(e))

# -----------------------------
# Save Output to File
# -----------------------------
def save_output():
    output = tree_output.get("1.0", END).strip()
    if not output:
        messagebox.showinfo("No Output", "Nothing to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)
        messagebox.showinfo("Saved", f"Output saved to {file_path}")

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("CFG-Based Syntax Checker with Derivation")
root.geometry("1000x780")
root.configure(bg="#f2f2f2")

Label(root, text="CFG Syntax Checker", font=("Helvetica", 20, "bold"), bg="#f2f2f2").pack(pady=10)

# Input Box
input_frame = tk.Frame(root, bg="#f2f2f2")
input_frame.pack(pady=5)
Label(input_frame, text="Enter Code Below:", font=("Helvetica", 12), bg="#f2f2f2").grid(row=0, column=0, sticky="w")
text_input = Text(input_frame, height=8, width=100, font=("Courier New", 10))
text_input.grid(row=1, column=0, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)
Button(button_frame, text="Check Syntax", font=("Helvetica", 12, "bold"), bg="#007acc", fg="white", command=check_syntax).grid(row=0, column=0, padx=10)
Button(button_frame, text="Save Output", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", command=save_output).grid(row=0, column=1, padx=10)

# Result Label
result_output = Label(root, text="", font=('Helvetica', 14, 'bold'), bg="#f2f2f2")
result_output.pack()

# Output Viewer
output_frame = tk.Frame(root, bg="#f2f2f2")
output_frame.pack(pady=10)
Label(output_frame, text="Parse Tree + Derivation Steps / Errors:", font=("Helvetica", 12), bg="#f2f2f2").pack(anchor="w")

scrollbar = Scrollbar(output_frame)
scrollbar.pack(side=RIGHT, fill=Y)

tree_output = Text(output_frame, height=25, width=110, font=("Courier New", 10), yscrollcommand=scrollbar.set)
tree_output.pack(side="left", padx=10)
scrollbar.config(command=tree_output.yview)

# Run Graphviz check and launch GUI
prompt_graphviz_warning()
root.mainloop()
