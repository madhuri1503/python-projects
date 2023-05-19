import tkinter as tk
import random
import time

class TypingTest:
    def __init__(self, master):
        self.master = master
        self.sentences = ['She does not study German on Monday', 'Does she live in Paris?', 'He doesnot teach math', 'Cats hate water', 'I scream, you scream, we all scream for ice cream']
        self.current_sentence = ""
        self.current_sentence_index = 0
        self.score = 0
        self.time_start = 0
        self.time_end = 0

        self.label = tk.Label(master, text="Type the sentence:")
        self.label.pack()

        self.sentence_label = tk.Label(master, text="")
        self.sentence_label.pack()

        self.input_box = tk.Entry(master)
        self.input_box.pack()

        self.score_label = tk.Label(master, text="")
        self.score_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, state="disabled")
        self.stop_button.pack()

    def start(self):
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.score = 0
        self.time_start = time.time()
        self.get_new_sentence()

    def stop(self):
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.input_box.delete(0, tk.END)
        self.time_end = time.time()
        self.label.config(text=f"Your score: {self.score} | Time taken: {round(self.time_end - self.time_start, 2)} seconds")
        self.sentence_label.config(text="")
        self.score_label.config(text="")

    def get_new_sentence(self):
        self.current_sentence = random.choice(self.sentences)
        self.current_sentence_index = 0
        self.sentence_label.config(text=self.current_sentence)

    def check_input(self):
        input_text = self.input_box.get()
        if input_text == self.current_sentence:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.input_box.delete(0, tk.END)
            self.get_new_sentence()
        else:
            self.input_box.delete(0, tk.END)

    def handle_keypress(self, event):
        if event.keysym == "Return":
            self.check_input()
        elif event.keysym == "BackSpace":
            self.input_box.delete(len(self.input_box.get())-1, tk.END)
        elif len(event.char) == 1:
            if event.char == self.current_sentence[self.current_sentence_index]:
                self.current_sentence_index += 1
                if self.current_sentence_index == len(self.current_sentence):
                    self.check_input()

root = tk.Tk()
root.title("Typing Test")
typing_test = TypingTest(root)
root.bind("<Key>", typing_test.handle_keypress)
root.mainloop()
