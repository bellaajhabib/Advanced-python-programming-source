"""A local two-player chess game. Run: py chess_game.py

Install the chess rules library first: py -m pip install chess
Click a piece, then a highlighted square to move it.
"""

import tkinter as tk
from tkinter import simpledialog

import chess


class ChessGame:
    def __init__(self, root):
        self.root = root
        self.board = chess.Board()
        self.selected = None
        self.buttons = {}
        root.title("Simple Chess — Two Players")
        root.resizable(False, False)

        self.status = tk.StringVar()
        tk.Label(root, textvariable=self.status, font=("Arial", 14)).pack(pady=10)
        grid = tk.Frame(root)
        grid.pack(padx=12)

        for row in range(8):
            tk.Label(grid, text=str(8 - row)).grid(row=row, column=0)
            for column in range(8):
                square = chess.square(column, 7 - row)
                button = tk.Button(
                    grid, font=("Segoe UI Symbol", 30), width=2, height=1,
                    fg="#111111", relief="flat",
                    command=lambda square=square: self.click(square),
                )
                button.grid(row=row, column=column + 1)
                self.buttons[square] = button
        for column, letter in enumerate("abcdefgh"):
            tk.Label(grid, text=letter).grid(row=8, column=column + 1)

        tk.Label(root, text="Click a piece, then a highlighted square.").pack(pady=5)
        tk.Button(root, text="New game", command=self.restart).pack(pady=(0, 12))
        self.refresh()

    def refresh(self):
        targets = {
            move.to_square for move in self.board.legal_moves
            if move.from_square == self.selected
        }
        for square, button in self.buttons.items():
            piece = self.board.piece_at(square)
            light = (chess.square_rank(square) + chess.square_file(square)) % 2
            color = "#f0d9b5" if light else "#b58863"
            if square == self.selected:
                color = "#f6e05e"
            elif square in targets:
                color = "#9ccc65"
            button.config(text=piece.unicode_symbol() if piece else "",
                          bg=color, activebackground=color)

        outcome = self.board.outcome()
        if outcome:
            if outcome.winner is None:
                message = "Draw"
            else:
                message = ("White" if outcome.winner else "Black") + " wins"
            reason = outcome.termination.name.replace("_", " ").lower()
            self.status.set(f"{message} — {reason}")
        else:
            player = "White" if self.board.turn else "Black"
            self.status.set(f"{player} to move" + (" — Check!" if self.board.is_check() else ""))

    def click(self, square):
        if self.board.is_game_over():
            return

        # Clicking your own piece selects it and shows its legal destinations.
        piece = self.board.piece_at(square)
        if piece and piece.color == self.board.turn:
            self.selected = None if square == self.selected else square
            self.refresh()
            return

        if self.selected is None:
            return
        candidates = [move for move in self.board.legal_moves
                      if move.from_square == self.selected and move.to_square == square]
        if not candidates:
            return

        move = candidates[0]
        if move.promotion:
            choice = simpledialog.askstring(
                "Promote pawn", "Choose Q (queen), R (rook), B (bishop), or N (knight):",
                initialvalue="Q", parent=self.root,
            )
            if choice is None:
                return
            promotions = {"q": chess.QUEEN, "r": chess.ROOK,
                          "b": chess.BISHOP, "n": chess.KNIGHT}
            promotion = promotions.get(choice.strip().lower())
            if promotion is None:
                return
            move = chess.Move(self.selected, square, promotion=promotion)

        self.board.push(move)
        self.selected = None
        self.refresh()

    def restart(self):
        self.board.reset()
        self.selected = None
        self.refresh()


if __name__ == "__main__":
    window = tk.Tk()
    ChessGame(window)
    window.mainloop()
