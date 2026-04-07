# PDF-GPT
Have you ever tried to fix one of your coding problems but you found the process of slowly highlighting all text, copying it, pasting it into your LLM of choice, making minor edits with instructions, then doing that entire process for eery file you wish to address, just a little bit estrenuous? Now with PDF-GPT all you need to do is write six golden letters, _pdfgpt_, in your terminal and a .pdf file will magically appear right inside of your directory. All you have to do now is upload that .pdf file to your favorite LLM and save your precious seconds!

<sub>Disclaimer: I am not responsible for your beloved LLM messing up your program and/or hallucinating with solutions. PDF-GPT's PDFs work very well, it is your code that does not. If you decide to report your spaghetti code to the Issues tab, I may end up laughing at it, and if you're funny enough I'll print it out and tape it to my bedroom wall. So, if you're a comedian, please consider reporting your LLM's issues directly to the Issues tab.</sub>

## Installation
To install PDF-GPT, simply run the following command into your terminal:

```pip install pdfgpt-llm```

## Commands List

## Commands

This project includes several terminal commands for managing the workflow and accessing information. To run them, simply type the command of your choice Below is a list of available commands:

| Command                  | Description |
|---------------|-------------|
| `pdfgpt` | Run this command to have your entire repository compiled into one simple .pdf file that will be stored in the directory!|
| `commandlist` | Displays a list of all available commands in the terminal. |
| `ignoreadd <FILENAME>`   | Adds a file to the ignore list based on its filename. Starting with version 0.2.0 you can also include paths too. |
| `ignoreremove <FILENAME>`| Removes a file from the ignore list based on its filename. Starting with version 0.2.0 you can also include paths too. |
| `ignoreshow`  | Shows the current contents of the ignore list in the terminal. |
| `lastupdate`  | Displays information about the latest update. |
| `repository`  | Prints the link to the GitHub repository for PDFGPT. Chances are if you're reading this, you probably know how that command works! |

## Features Explained

### Ignore List
The Ignore List essentially acts as a .gitignore, as any file name added to the list will be... ignored... by PDFGPT. The program works with both file names as well as file paths.

<sub>Web devs, forgive me.</sub>

### Demo Run
Here's a quick demo of me using a PDFGPT-created .pdf file to have ChatGPT fix issues that it may find across ten different programs from ten different languages! Keep in mind this was done BEFORE I added terminal accessibility, so instead of being ran through the terminal, the PDF was compiled by running PDFGPT.py.

[![Demo Run](https://img.youtube.com/vi/jTag6m7WDIk/0.jpg)](https://www.youtube.com/watch?v=jTag6m7WDIk)

### Example Problems
Additional to the demo run video, I have created a folder in the repository, `Fun example problems!`. You can use that for testing if curious on as to how this program works. Please refer to the `readme.txt` file included inside of the folder for more information.
