from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.constants import *
from PIL import ImageTk
from pytube import YouTube


app = ttk.Window(title="YTGet v. 0.1", themename="superhero", iconphoto ='yt32.png', size=(1000, 800))
app.place_window_center()

colors = app.style.colors

img1 = ImageTk.PhotoImage(file="info_2_32.png")
img2 = ImageTk.PhotoImage(file="trash_1_32.png")


def get_video():

    url = ytlink.get()

    if len(url) > 0:
        st1.insert(END, '\nPobieram ...\n')
        app.update()
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            filename = stream.default_filename
            file_size = stream.filesize
            stream.download('./video')
            st1.insert(END, f"Pobrano: {file_size/1024/1024:.2f} MB")
        except:
            st1.insert(END, '\nBłąd pobierania pliku !\n')    
            messagebox.showinfo(title="Błąd", message="Błąd pobrania pliku z YouTube")

    else:
        messagebox.showinfo(title="Informacja", message="Wprowadż link do filmu na YouTube")

     
def clear_notes():
    st1.delete('1.0', END)
    question_entry.delete(0, END)

def about():
    messagebox.showinfo(title="Informacja", message="YTGet 0.1\n\nUmożliwia ściągnięcie filmu z YouTube\n\nAutor: Leszek Owczarek, Dimex\nLicencja: MIT")

container1 = ttk.Frame()
container1.pack(fill=X, expand=YES, pady=5)
ytlink = ttk.StringVar()
question_entry = ttk.Entry(master=container1, textvariable=ytlink)
question_entry.pack(side=LEFT, pady=5, expand=YES, fill=BOTH)
ask_button = ttk.Button(master=container1, text="Download", bootstyle=SUCCESS, command=get_video)
ask_button.pack(side=LEFT,pady=5, padx=5)
clear_button = ttk.Button(master=container1, image=img2, command=clear_notes)
clear_button.pack(side=LEFT,pady=5, padx=5)
b5 = ttk.Button(master=container1, image=img1, command=about)
b5.pack(side=RIGHT, padx=5, pady=5)

# NOTES Z WYNIKIEM
st1 = ScrolledText(app, padding=5, height=25, autohide=True)
st1.pack(fill=BOTH, expand=YES)


if __name__ == "__main__":
    app.mainloop()