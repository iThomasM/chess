import pygame
from chess import Chess

class Main:
    def __init__(self):
        self.pieces = {}
        self.WIDTH, self.HEIGHT = 500, 500
        self.BOARD_SIZE = 8
        self.TILE_SIZE = (self.WIDTH // self.BOARD_SIZE, self.HEIGHT // self.BOARD_SIZE)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.load_images()
        self.running = True
        self.clicks = 0
        self.chess = Chess(self)
        self.board = self.chess.board

    #load images
    def load_images(self):
        pieces = ["bp", "br", "bkn", "bb", "bq", "bk", "wp", "wr", "wkn", "wb", "wq", "wk"]
        for piece in pieces:
            self.pieces[piece] = pygame.transform.scale(pygame.image.load(f"pygame/assets/{piece}.svg"), self.TILE_SIZE)

    #draw board
    def draw_board(self):
        colors = ["white", "gray"]
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                pygame.draw.rect(self.screen, pygame.Color(colors[(i + j) % 2]), 
                                 pygame.Rect(i*self.TILE_SIZE[0], j*self.TILE_SIZE[1],
                                              self.TILE_SIZE[0], self.TILE_SIZE[1]))

    #draw pieces
    def draw_pieces(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                piece = self.board[j][i]
                if piece != "--":
                    self.screen.blit(self.pieces[piece], pygame.Rect(i*self.TILE_SIZE[0], j*self.TILE_SIZE[1],
                                                                    self.TILE_SIZE[0], self.TILE_SIZE[1]))
                    
    #take player input
    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks += 1
                mouse_pos = pygame.mouse.get_pos()
                piece = mouse_pos[0] // self.TILE_SIZE[0], mouse_pos[1] // self.TILE_SIZE[1]
                if self.clicks == 1:
                    self.chess.select_piece(piece)
                elif self.clicks == 2:
                    self.chess.move_piece(piece)
                    self.clicks = 0

    #update screen
    def _screen(self):
        self.draw_board()
        self.draw_pieces()
        pygame.display.update()

    def run(self):
        while self.running:
            self._screen()
            self._events()

if __name__ == "__main__":
    game = Main()
    game.run()
    