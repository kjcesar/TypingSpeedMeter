import tkinter as tk
from itertools import cycle
from random import choice
from time import sleep

# THings that Helped: https://www.geeksforgeeks.org/how-to-test-typing-speed-using-python/

FONT = 'JetBrainsMono NF'
MEDIUM_FONT = (FONT, 16)
SMALL_FONT = (FONT, 14)
BIG_FONT = (FONT, 20)
SUPERBIG = (FONT, 34)


class TypingSpeed:

    def __init__(self):
        self.window = tk.Tk()

        self.Title = tk.Label(self.window, text="Wellcome to my Typing Speed Test", font=SUPERBIG)
        self.Title.pack(padx=20, pady=10)

        self.words = [
            'python', 'programacion', 'velocidad', 'desarrollo', 'tecnologia', 'inteligencia',
            'artificial', 'aprendizaje', 'maquina', 'informacion', 'estructura', 'algoritmo',
            'computadora', 'interfaz', 'usuario', 'biblioteca', 'ingenieria', 'datos',
            'comunicacion', 'rendimiento', 'optimizacion', 'experiencia', 'informatica',
            'teclado', 'raton', 'pantalla', 'conexion', 'protocolo', 'rendimiento'
        ]

        self.word_cycle = cycle(self.words)
        self.tempo = 2000  # 2 segs

        self.words_frame = tk.Frame(self.window)
        self.words_frame.columnconfigure(0, weight=1)
        self.words_frame.columnconfigure(1, weight=1)

        self.word_to_write = tk.Label(self.words_frame, text="Word to Write:", font=SMALL_FONT, bg="green")
        self.word_to_write.grid(row=0, column=0, padx=20, pady=10)

        self.next_word = tk.Label(self.words_frame, text="Next Word:", font=SMALL_FONT, bg="blue", fg="white")
        self.next_word.grid(row=0, column=1, padx=20, pady=10)

        self.present_word = tk.Label(self.words_frame, text="Prepare Your self", font=SMALL_FONT, bg="green")
        self.present_word.grid(row=1, column=0, padx=20)

        self.future_word = tk.Label(self.words_frame, text=choice(self.words), font=SMALL_FONT, bg="blue", fg="white")
        self.future_word.grid(row=1, column=1, padx=20)

        self.words_frame.pack(padx=10, pady=10)

        self.start_button = tk.Button(self.window, text="START test", font=MEDIUM_FONT, command=self.iniciar)
        self.start_button.pack(pady=10)

        self.entry_frame = tk.Frame(self.window)

        self.entry_label = tk.Label(self.entry_frame, text="Entry your text here and then press Enter",
                                    font=MEDIUM_FONT)
        self.entry_label.grid(row=0, column=0)

        self.user_entry = tk.Entry(self.entry_frame, font=SMALL_FONT, state='disabled')
        self.user_entry.bind("<KeyPress>", self.adding_word)
        self.user_entry.grid(row=1, column=0)

        self.contador_label = tk.Label(self.entry_frame, text="", font=BIG_FONT)
        self.contador_label.grid(row=2, pady=20)

        self.words_written = tk.Listbox(self.entry_frame, font=SMALL_FONT)
        self.words_written.grid(row=3, column=0)

        self.entry_frame.pack(pady=30)

        self.result = tk.Label(self.window, text="", font=SUPERBIG)
        self.result.pack(pady=20)

        self.window.mainloop()

    def word_carousel(self):

        present_word = self.future_word.cget("text")
        future_word = next(self.word_cycle)

        # update labels
        self.present_word.config(text=f"{present_word}")
        self.future_word.config(text=f"{future_word}")

    def adding_word(self, event):
        correct = "lightgreen"
        incorrect = "red"

        if event.keysym == "Return":
            word = self.user_entry.get()
            if word:
                self.words_written.insert(tk.END, word)
                self.words_written.itemconfig(tk.END, {'bg': incorrect})
                if self.present_word.cget("text") == word:
                    self.words_written.itemconfig(tk.END, {'bg': correct})
                self.user_entry.delete(0, tk.END)
                self.word_carousel()

    def contador(self, segundos):
        self.contador_label['text'] = f"Time Remaining: {segundos} seg"
        if segundos > 0:
            self.window.after(1000, self.contador, segundos - 1)
        else:
            self.contador_label['text'] = "Time Out!!!"
            self.score()

    def iniciar(self):
        self.word_carousel()
        self.user_entry.config(state='normal')
        self.user_entry.focus_set()
        sleep(1)
        self.contador(15)
        self.start_button.config(state='disabled')

    def score(self):
        self.user_entry.config(state='disabled')
        elementos_correctos = [self.words_written.get(i) for i in range(self.words_written.size()) if
                               self.words_written.itemcget(i, 'bg') == "lightgreen"]
        cantidad_correctas = len(elementos_correctos)
        cantidad_total = self.words_written.size()
        self.result.config(
            text=f"Correct Words: {cantidad_correctas}\n Palabras Por Minuto = {cantidad_total / 10 * 60}")


TypingSpeed()
