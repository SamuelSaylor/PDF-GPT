import csv
import os
from fpdf import FPDF
from sympy import content

ignorecsv = os.path.join(os.path.dirname(__file__), 'IGNORELIST.csv')

COMMAND_LIST = [
    "commandList - Provides a list of commands in the terminal.",
    "ignoreListADD - Adds a file to the ignore list based on its name.",
    "ignoreListREMOVE - Removes a file from the ignore list based on its name.",
    "ignoreListSHOW - Provides the contents of the ignore list in the terminal."
    "lastUpdate - Prints the latest update.",
    "repository - Prinst the link to the repository for PDF GPT."
]

def commandList():
    print("#########################################\nPDFGPT - Compiles all readable files into a PDF with instructions for a LLM to scan and interpret it.\n")
    for cmd in COMMAND_LIST: print(cmd)
    print("\n#########################################")

def lastUpdate(): print("#########################################\n\nLast updated: 03/30/2026 @ XX:XX\n\n#########################################")

def repository(): print("#########################################\n\nhttps://github.com/SamuelSaylor/PDF-GPT\n\n#########################################")

def copy():
    pass

def ignoreListADD(INPUT):
    with open(ignorecsv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([INPUT])

    print(f"#########################################\n\nAdded file: {INPUT} to ignore list.\n\n#########################################")

def ignoreListREMOVE(INPUT):

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
    
    IGNORE_LIST = []

    with open(ignorecsv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            IGNORE_LIST.append(row[0])

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if file in IGNORE_LIST or file_path in IGNORE_LIST:
                continue
            else:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except (UnicodeDecodeError, PermissionError,IsADirectoryError):
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

"""
if __name__ == "__main__":
    PDFGPT()
"""

ignoreListADD("PDFGPT.pdf")