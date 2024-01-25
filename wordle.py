import tkinter as tk
import random
import tkinter as tk


class WordleGame:
  class WordleGame: 
    def __init__(self):
      self.word = self.get_random_word()
      self.guesses = 0
      self.max_guesses = 6
      self.guessed_letters = set()

      self.root = tk.Tk()
      self.root.title("Wordle Game")
  

      # Styling
      self.root.configure(bg="#f2f2f2")
      self.root.option_add("*Font", "Arial 12")

      self.word_label = tk.Label(self.root, text=" ".join("_" * len(self.word)), bg="#f2f2f2", fg="#333333")
      self.word_label.pack(pady=10)

      self.guess_entry = tk.Entry(self.root, bg="#ffffff", fg="#333333", relief="solid", bd=1)
      self.guess_entry.pack(pady=5)

      self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, bg="#4caf50", fg="#ffffff", relief="flat")
      self.guess_button.pack(pady=5)

      self.result_label = tk.Label(self.root, text="", bg="#f2f2f2", fg="#333333")
      self.result_label.pack(pady=10)

    def get_random_word(self):
      words = ["apple", "banana", "cherry", "orange", "pear"]
      return random.choice(words)

    def make_guess(self):
      guess = self.guess_entry.get().lower()
      self.guess_entry.delete(0, tk.END)

      if guess in self.guessed_letters:
        self.result_label.config(text="You already guessed that letter!")
        return

      self.guessed_letters.add(guess)

      if guess in self.word:
        self.update_word_label()
        if self.word_label.cget("text") == self.word:
          self.result_label.config(text="Congratulations! You guessed the word!")
          self.guess_button.config(state=tk.DISABLED)
      else:
        self.guesses += 1
        self.result_label.config(text=f"Wrong guess! {self.max_guesses - self.guesses} guesses left.")
        if self.guesses == self.max_guesses:
          self.result_label.config(text=f"Game over! The word was {self.word}.")
          self.guess_button.config(state=tk.DISABLED)

    def update_word_label(self):
      word_with_guesses = ""
      for letter in self.word:
        if letter in self.guessed_letters:
          word_with_guesses += letter
        else:
          word_with_guesses += "_"
      self.word_label.config(text=word_with_guesses)

    def start(self):
      self.root.mainloop()

  # Usage example
  game = WordleGame()
  game.start()

  def make_guess(self):
    guess = self.guess_entry.get().lower()
    self.guess_entry.delete(0, tk.END)

    if guess in self.guessed_letters:
      self.result_label.config(text="You already guessed that letter!")
      return

    self.guessed_letters.add(guess)

    if guess in self.word:
      self.update_word_label()
      if self.word_label.cget("text") == self.word:
        self.result_label.config(text="Congratulations! You guessed the word!")
        self.guess_button.config(state=tk.DISABLED)
    else:
      self.guesses += 1
      self.result_label.config(text=f"Wrong guess! {self.max_guesses - self.guesses} guesses left.")
      if self.guesses == self.max_guesses:
        self.result_label.config(text=f"Game over! The word was {self.word}.")
        self.guess_button.config(state=tk.DISABLED)

  def update_word_label(self):
    word_with_guesses = ""
    for letter in self.word:
      if letter in self.guessed_letters:
        word_with_guesses += letter
      else:
        word_with_guesses += "_"
    self.word_label.config(text=word_with_guesses)

  def start(self):
    self.root.mainloop()

# Usage example
game = WordleGame("apple")
game.start()
