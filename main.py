from typing import List

from tkinter import Tk
from tkinter import ttk


class App:
    def form(self, window) -> None:
        window.title('capture video Pro alpha 0.1')
        window.geometry("680x480")
        window.resizable(False, False)
        book = ttk.Notebook(window)
        book.grid(column=0, row=0)
        book.pack(pady=10, expand=True)
        self.pagina1(window, book)
        self.pagina2(window, book)

    def pagina1(self, window, book):
        video = ttk.Frame(book, width=660, height=450)
        video.pack(fill='both', expand=True)
        book.add(video, text="Capture video")

    def pagina2(self, window, book):
        settings = ttk.Frame(book, width=660, height=450)
        settings.pack(fill='both', expand=True)
        book.add(settings, text="Settings video")


def main(args:List[str]) -> int:
    app = App()
    window = Tk()
    app.form(window)
    window.mainloop()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
