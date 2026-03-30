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
    for i in range(len(COMMAND_LIST)): print(COMMAND_LIST[i])
    print("\n#########################################")

def lastUpdate(): print("#########################################\n\nLast updated: 03/30/2026 @ XX:XX\n\n#########################################")

def repository(): print("#########################################\n\nhttps://github.com/SamuelSaylor/PDF-GPT\n\n#########################################")

def ignoreListADD():
    pass

def ignoreListREMOVE():
    pass

def ignoreListSHOW():
    pass

def PDFGPT():
    pass

lastUpdate()
repository()
commandList()