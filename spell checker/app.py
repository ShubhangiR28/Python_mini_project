from textblob import TextBlob
from tkinter import *
from tkinter import filedialog


# Global variables to store the original and corrected words
original_word_global = ""
corrected_word_global = ""

def correct_spelling():
    global original_word_global, corrected_word_global
    
    get_data = entry1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    entry2.delete(0, END)
    entry2.insert(0, data)
    
    # Update global variables
    original_word_global = get_data
    corrected_word_global = data

def save_to_file():
    global original_word_global, corrected_word_global
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("C:\\Users\\shubh\\OneDrive\\Desktop\\spell checker\\Text files", "*.txt")])

    if file_path:
        with open(file_path, 'a') as file:
            file.write(f"Original Word: {original_word_global}\t Corrected Word: {corrected_word_global}\n")
        print(f"Words saved to {file_path}")
    save_to_file(original_word_global,corrected_word_global)
def main_window():
    global entry1, entry2

    win = Tk()   
    win.geometry("500x370")
    win.resizable(False, False)
    win.config(bg="Blue")
    win.title("Spell checker")

    Label1 = Label(win, text="Incorrect Spelling", font=("Time New Roman", 25, "bold"), bg="Blue", fg="white")
    Label1.place(x=100, y=20, height=50, width=300)
 
    entry1 = Entry(win, font=("Time new Roman", 20))
    entry1.place(x=50, y=80, height=50, width=400)

    Label2 = Label(win, text="Correct Spelling", font=("Time New Roman", 25, "bold"), bg="Blue", fg="white")
    Label2.place(x=100, y=140, height=50, width=300)
 
    entry2 = Entry(win, font=("Time new Roman", 20))
    entry2.place(x=50, y=200, height=50, width=400)

    button = Button(win, text="Done", font=("Time new Roman", 25, "bold"), bg="yellow", command=correct_spelling)
    button.place(x=150, y=280, height=50, width=200)

    # Add a button to save words to a file
    save_button = Button(win, text="Save to File", font=("Time new Roman", 15), bg="green", fg="white", command=save_to_file)
    save_button.place(x=180, y=330, height=30, width=150)

    win.mainloop()

main_window()
