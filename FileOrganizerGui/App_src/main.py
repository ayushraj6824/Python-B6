import tkinter as tk #GUI

from file_organizer import organize_files # type: ignore
# Create the main window

root = tk.Tk()
root.title("File Organizer") 
root.geometry("800x250")  # Set the window sizeFunction to be called when the button is clicked

def buttonfn():
    address = entry.get()  # Get text from the e
    organize_files(address)

label = tk.Label(root, text="Enter Address:")
label.pack(pady=10)  # Add padding around the labelEntry (input block) where user can type text

entry = tk.Entry(root, width=30)
entry.pack(pady=5)#Button to trigger the function show_input

button = tk.Button(root, text="Submit", command=buttonfn)

button.pack(pady=10)#Start the GUI event loop

root.mainloop()