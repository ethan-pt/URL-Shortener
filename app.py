import tkinter as tk
import pyshorteners

class app:
    def __init__(self, master):
        self.master = master

        self.entry = tk.Entry(master, width=40)
        self.button = tk.Button(master, text='Go', command=self.shorten)
        self.label = tk.Text(master, width=35, height=1, )

        self.entry.grid(row=0, column=0, pady=15, padx=5)
        self.button.grid(row=0, column=1, padx=5)
        self.label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def shorten(self):
        short = pyshorteners.Shortener()
        shorturl = short.tinyurl.short(self.entry.get())
        self.label.delete(1.0, tk.END)
        self.label.insert(tk.END, shorturl)

def main():
    root = tk.Tk()
    root.title('URL Shortener')
    window = app(root)
    root.mainloop()

if __name__ == '__main__':
    main()