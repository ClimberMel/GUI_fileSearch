'''
In this version, the results listbox is replaced with a treeview widget
I have the frame containing the treeview resize when window is resized.
The find_files function from findFile_21.py is used to search for the files.
Compare the find_files function with the code in findDirectory.py
That code will find files or directories, this code only seems to find files.
findDirectory also has code I should add in to write the results to a file.
'''

import os
import fnmatch
import tkinter as tk
from tkinter import filedialog, ttk

def find_files(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def search():
    pattern = pattern_entry.get()
    path = path_entry.get()
    result_list.delete(0, tk.END) # clear the list
    if not pattern or not path:
        result_list.insert(tk.END, 'Please enter a pattern and a path')
        return
    files = find_files(pattern, path)
    if not files:
        result_list.insert(tk.END, 'No files found')
    else:
        for file in files:
            result_list.insert(tk.END, file)
    # Adjust the size of the listbox based on the number of items
    result_list.config(height=min(len(files), 10))

def browse_path():
    path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, path)

root = tk.Tk()
root.title('File Search')

# Pattern entry
pattern_label = tk.Label(root, text='Pattern:')
pattern_entry = tk.Entry(root)

# Path entry
path_label = tk.Label(root, text='Path:')
path_entry = tk.Entry(root)
browse_button = tk.Button(root, text='Browse', command=browse_path)

# Search button
search_button = tk.Button(root, text='Search', command=search)

# Results list
result_list = tk.Listbox(root, width=50, height=15)

# Use a scrollbar for the results list
scrollbar = ttk.Scrollbar(root, orient='vertical', command=result_list.yview)
result_list['yscrollcommand'] = scrollbar.set

# Layout
pattern_label.grid(row=0, column=0, sticky='W')
pattern_entry.grid(row=0, column=1, sticky='W')
path_label.grid(row=1, column=0, sticky='W')
path_entry.grid(row=1, column=1, sticky='W')
browse_button.grid(row=1, column=2, sticky='W')
search_button.grid(row=2, column=1, sticky='W')
result_list.grid(row=3, column=0, columnspan=3, sticky='EW', padx=5, pady=5)
scrollbar.grid(row=3, column=3, sticky='NSEW', padx=5, pady=5)

# Allow the results list to be resized
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()