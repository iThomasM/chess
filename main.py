import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen_size = 1024
        self.board_size = 8
        self.tile_size = self.screen_size // self.board_size
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                      ["bp"] * 8,
                      ["-"] * 8,
                      ["-"] * 8,
                      ["-"] * 8,
                      ["-"] * 8,
                      ["wp"] * 8,
                      ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
        self.pieces = {}
        self.running = True
        self.turn = "w"
        self._load_pieces()
        self.selected_piece = None
        self.selected_tile = None
        self.clicks = 0

    def _load_pieces(self):
        pieces = ["br", "bn", "bb", "bq", "bk", "bp", "wr", "wn", "wb", "wq", "wk", "wp"]
        for piece in pieces:
            self.pieces[piece] = pygame.transform.scale(pygame.image.load(f"Pygame/chess-main/assets/{piece}.png"), (self.tile_size, self.tile_size))

    def run(self):
        while self.running:
            self._screen()
            self._events()

    def _screen(self):
        self._draw_board()
        self._draw_pieces()
        pygame.display.flip()

    def _draw_board(self):
        colors = ["white", "gray"]
        for i in range(self.board_size):
            for j in range(self.board_size):
                pygame.draw.rect(self.screen, pygame.Color(colors[(i + j) % 2]),
                                 pygame.Rect(i * self.tile_size, j * self.tile_size,
                                             self.tile_size, self.tile_size))
                
        for move in getattr(self, 'legal_moves', []):
            x, y = move
            pygame.draw.rect(self.screen, (0, 200, 0,), pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
        
        if self.selected_tile:
            pygame.draw.rect(self.screen, (0, 0, 200,), pygame.Rect(self.selected_tile[0] * self.tile_size, self.selected_tile[1] * self.tile_size, self.tile_size, self.tile_size))

    def _draw_pieces(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                piece = self.board[j][i]
                if piece != "-":
                    self.screen.blit(self.pieces[piece], pygame.Rect(i * self.tile_size, j * self.tile_size,
                                                                    self.tile_size, self.tile_size))

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected_tile = (pos[0] // self.tile_size, pos[1] // self.tile_size)

                if self.clicks == 0:
                    piece = self.board[selected_tile[1]][selected_tile[0]]
                    if piece != "-" and piece.startswith(self.turn):
                        self.selected_tile = selected_tile
                        self.selected_piece = piece
                        self.legal_moves = self.get_legal_moves(self.selected_tile)
                        self.clicks = 1

                elif self.clicks == 1:
                    if selected_tile in self.legal_moves:
                        self.move_piece(selected_tile, self.selected_tile)
                        self._turn()

                    self.legal_moves = []
                    self.clicks = 0

    def _turn(self):
        if self.turn == "w":
            self.turn = "b"
        else: 
            self.turn = "w"

    def move_piece(self, new_tile, prev_tile):
        self.board[new_tile[1]][new_tile[0]] = self.selected_piece
        self.board[prev_tile[1]][prev_tile[0]] = "-"


    def get_legal_moves(self, tile):
        piece_type = self.selected_piece[1]
        piece_color = self.selected_piece[0]
        col, row = tile
        piece = self.board[row][col]
        if piece == "-":
            return []
        
        if piece_type == "p":
            return self.get_pawn_moves(row, col, piece_color)
        elif piece_type == "n":
            return self.get_knight_moves(row, col, piece_color)
        elif piece_type == "b":
            return self.get_bishop_moves(row, col, piece_color)
        elif piece_type == "r":
            return self.get_rook_moves(row, col, piece_color)
        elif piece_type == "k":
            return self.get_king_moves(row, col, piece_color)
        elif piece_type == "q":
            return self.get_queen_moves(row, col, piece_color)
        
    def get_king_moves(self, row, col, color):
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        for r, c in directions:
            new_row, new_col = row + r, col + c
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                target = self.board[new_row][new_col]
                if target == "-" or not target.startswith(color):
                    moves.append((new_col, new_row))

        return moves

    def get_pawn_moves(self, row, col, color):
        moves = []
        direction = -1 if color == "w" else 1
        start_row = 6 if color == "w" else 1

        if self.board[row + direction][col] == "-":
            moves.append((col, row + direction))
            if row == start_row and self.board[row + 2 * direction][col] == "-":
                moves.append((col, row + 2 * direction))

        for captures in [-1, 1]:
            new_col = col + captures
            if 0 <= new_col < self.board_size and 0 <= row + direction < self.board_size:
                target = self.board[row + direction][new_col]
                if target != "-" and not target.startswith(color):
                    moves.append((new_col, row + direction))
        
        return moves
    
    def get_knight_moves(self, row, col, color):
        moves = []

        knight_moves = [(2, 1), (2, -1),
                        (-2, 1), (-2, -1),
                        (1, 2), (1, -2),
                        (-1, 2), (-1, -2)]
        
        for r, c in knight_moves:
            new_row, new_col = row + r, col + c
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                target = self.board[new_row][new_col]
                if not target.startswith(color):
                    moves.append((new_col, new_row))
    
        return moves
    
    def get_bishop_moves(self, row, col, color):
        moves = []
        
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for r, c in directions:
            new_row, new_col = row + r, col + c
            while 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                target = self.board[new_row][new_col]
                if target == "-":
                    moves.append((new_col, new_row))
                else:
                    if not target.startswith(color):
                        moves.append((new_col, new_row))
                    break
                new_row += r
                new_col += c
        
        return moves
    
    def get_rook_moves(self, row, col, color):
        moves = []

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for r, c in directions:
            new_row, new_col = row + r, col + c
            while 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                target = self.board[new_row][new_col]
                if target == "-":
                    moves.append((new_col, new_row))
                else:
                    if not target.startswith(color):
                        moves.append((new_col, new_row))
                    break
                new_row += r
                new_col += c
        
        return moves
    
    def get_queen_moves(self, row, col, color):
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        for r, c in directions:
            new_row, new_col = row + r, col + c
            while 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                target = self.board[new_row][new_col]
                if target == "-":
                    moves.append((new_col, new_row))
                elif not target.startswith(color):
                    moves.append((new_col, new_row))
                    break
                else:
                    break

                new_row += r
                new_col += c

        return moves
        
if __name__ == "__main__":
    game = Game()
    game.run()