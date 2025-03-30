import pygame

class Chess:
    def __init__(self, main):
        self.game = main
        self.turn = "w"
        self.selected_piece = None
        self.board = [["br", "bkn", "bb", "bq", "bk", "bb", "bkn", "br"],
                      ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                      ["wr", "wkn", "wb", "wq", "wk", "wb", "wkn", "wr"]]
        
    def select_piece(self, pos):
        self.og_pos = pos
        piece = self.board[pos[1]][pos[0]]
        if piece != "--" and piece.startswith(self.turn):
            self.selected_piece = piece
        else:
            self.game.clicks = 0
            return
            
    def move_piece(self, pos):
        if self.selected_piece == f"{self.turn}p":
            self.pawn(pos)
        elif self.selected_piece == f"{self.turn}kn":
            self.knight(pos)
        elif self.selected_piece == f"{self.turn}b":
            self.bishop(pos)
        elif self.selected_piece == f"{self.turn}r":
            self.rook(pos)
        elif self.selected_piece == f"{self.turn}q":
            self.queen(pos)
        elif self.selected_piece == f"{self.turn}k":
            self.king
        self.selected_piece = None
        
    def _player_turn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
    
    def pawn(self, pos):
        if self.turn == "w":
            allowed_movement = (-1, 0)
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) == allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        else:
            allowed_movement = (1, 0)
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) == allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        
    def knight(self, pos):
        allowed_movement = [(-2, 1), (-2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2), (2, 1), (2, -1)]
        if self.turn == "w":
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        else:
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
    
    def bishop(self, pos):
        allowed_movement = []
        for i in range(1, self.game.BOARD_SIZE + 1):
            allowed_movement.append((i, i))
            allowed_movement.append((-i, -i))
            allowed_movement.append((i, -i))
            allowed_movement.append((-i, i))
        if self.turn == "w":
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        else:
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        
    def rook(self, pos):
        allowed_movement = []
        for i in range(1, self.game.BOARD_SIZE + 1):
            allowed_movement.append((i, 0))
            allowed_movement.append((-i, 0))
            allowed_movement.append((0, -i))
            allowed_movement.append((0, i))
        if self.turn == "w":
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        else:
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
            
    def king(self, pos):
        allowed_movement = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        if self.turn == "w":
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        else:
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
            
    def queen(self, pos):
        allowed_movement = []
        for i in range(1, self.game.BOARD_SIZE + 1):
            allowed_movement.append((i, i))
            allowed_movement.append((-i, -i))
            allowed_movement.append((i, -i))
            allowed_movement.append((-i, i))
            allowed_movement.append((i, 0))
            allowed_movement.append((-i, 0))
            allowed_movement.append((0, -i))
            allowed_movement.append((0, i))
        if self.turn == "w":
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return
        else:
            if (pos[1] - self.og_pos[1], pos[0] - self.og_pos[0]) in allowed_movement:
                self.board[pos[1]][pos[0]] = self.selected_piece
                self.board[self.og_pos[1]][self.og_pos[0]] = "--"
                self._player_turn()
            else:
                return