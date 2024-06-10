import tkinter as tk
from scapper import run_downloader, setup

# Initialize the main application window
root = tk.Tk()
root.geometry("400x400")
root.title("Movie Downloader")

# Create and pack the label
label = tk.Label(root, text="Enter the name of the movie:")
label.pack(padx=5, pady=5)

# Create and pack the entry widget
entry = tk.Entry(root, width=50, font=('Helvetica', 12), relief='sunken')
entry.pack(padx=10, pady=10)

# Function to initiate the download process
def initiate_download():
    movie_name = entry.get()
    if movie_name.strip():
        driver = setup()  # setup returns driver and movie_name, but we don't need the second one here
        run_downloader(driver, movie_name)
    else:
        print("Please enter a movie name.")

# Create and pack the button
button = tk.Button(root, text="Download Movie", command=initiate_download, 
                   width=20, background='brown', fg='white')
button.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
