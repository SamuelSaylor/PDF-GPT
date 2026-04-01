import csv
import os
import fpdf

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
    with open('ignore_list.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([INPUT])

def ignoreListREMOVE(INPUT):
    with open('ignore_list.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] != INPUT]
    with open('ignore_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def ignoreListSHOW():
    print("#########################################\n\nIgnore List:\n")
    with open('ignore_list.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
    print("\n#########################################")

def PDFGPT(root_dir="."):
    IGNORE_LIST = []

    with open('ignore_list.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            IGNORE_LIST.append(row[0])
        
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if file in IGNORE_LIST or file_path in IGNORE_LIST:
                continue
            else:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        f.read(1)
                except (print("NOTE: File {} is not readable and will be skipped.".format(file_path))):
                    continue

if __name__ == "__main__":
    PDFGPT()