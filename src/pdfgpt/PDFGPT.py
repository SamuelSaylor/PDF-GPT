import csv
import os
import sys
from fpdf import FPDF

ignorecsv = os.path.join(os.path.dirname(__file__), 'IGNORELIST.csv')

COMMAND_LIST = [
    "commandlist - Provides a list of commands in the terminal.",
    "ignoreadd - Adds a file or path to the ignore list.",
    "ignoreremove - Removes a file or path from the ignore list.",
    "ignoreshow - Provides the contents of the ignore list in the terminal.",
    "lastupdate - Prints the latest update.",
    "repository - Prinst the link to the repository for PDF GPT."
]

def commandList():
    print("#########################################\nPDFGPT - Compiles all readable files into a PDF with instructions for a LLM to scan and interpret it.\n")
    for cmd in COMMAND_LIST: print(cmd)
    print("\n#########################################")

def lastUpdate(): print("#########################################\n\nLast updated: 03/31/2026 @ 11:00 PM CDT\n\n#########################################")

def repository(): print("#########################################\n\nhttps://github.com/SamuelSaylor/PDF-GPT\n\n#########################################")

def ignoreListADD():
    INPUT = sys.argv[1]

    with open(ignorecsv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([INPUT])

    print(f"#########################################\n\nAdded file: {INPUT} to ignore list.\n\n#########################################")

def ignoreListREMOVE():
    INPUT = sys.argv[1]

    with open(ignorecsv, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] != INPUT]
    with open(ignorecsv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"#########################################\n\nRemoved file: {INPUT} from ignore list.\n\n#########################################")

def ignoreListSHOW():
    print("#########################################\n\nIgnore List:\n")
    with open(ignorecsv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
    print("\n#########################################")

def PDFGPT(root_dir="."):
    print("#########################################\n\nGenerating PDF...")
    
    ignore_names = set()
    ignore_paths = []
    root_abs = os.path.abspath(root_dir)

    with open(ignorecsv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            entry = row[0].strip()
            if not entry:
                continue

            if os.path.sep in entry or '/' in entry or '\\' in entry:
                normalized = os.path.normpath(entry)
                if os.path.isabs(normalized):
                    ignore_paths.append(normalized)
                else:
                    ignore_paths.append(os.path.normpath(os.path.join(root_abs, normalized)))
            else:
                ignore_names.add(entry)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_abs = os.path.abspath(file_path)
            if file in ignore_names:
                continue
            if any(file_abs == path or file_abs.startswith(path + os.path.sep) for path in ignore_paths):
                continue
            else:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except (UnicodeDecodeError, PermissionError, IsADirectoryError):
                    print(f"NOTE: File {file_path} is not readable and will be skipped.")
                    continue
            
            pdf.set_font("Arial", 'B',10) # filename
            pdf.multi_cell(0, 5, file)
            pdf.ln(2)

            pdf.set_font("Arial",size = 10)
            for line in content.splitlines():
                pdf.multi_cell(0, 5, line)
            pdf.ln(5)

    pdf.output("PDFGPT.pdf")
    print("\nPDF successfully generated. Check the root directory for PDFGPT.pdf.\n\nTIP: Ignore files you don't want by using the ignoreListADD command.\n##########################################")

if __name__ == "__main__":
    PDFGPT()