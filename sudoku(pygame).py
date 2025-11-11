#!/usr/bin/env python3
import pygame, sys, random, copy

pygame.init()
WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku (Pygame)")

FONT = pygame.font.SysFont("arial", 36)
SMALL = pygame.font.SysFont("arial", 24)
BLACK, WHITE, GREY, BLUE, RED, GREEN = (0,0,0), (255,255,255), (200,200,200), (30,144,255), (255,0,0), (0,180,0)

# --- Sudoku utility logic ---
def valid(board, r, c, v):
    for j in range(9):
        if board[r][j] == v: return False
    for i in range(9):
        if board[i][c] == v: return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if board[i][j] == v: return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None

def solve_board(board):
    spot = find_empty(board)
    if not spot: return True
    r,c = spot
    for n in range(1,10):
        if valid(board,r,c,n):
            board[r][c] = n
            if solve_board(board): return True
            board[r][c] = 0
    return False

def generate_full_board():
    b = [[0]*9 for _ in range(9)]
    def fill():
        pos = find_empty(b)
        if not pos: return True
        r,c = pos
        nums = list(range(1,10))
        random.shuffle(nums)
        for n in nums:
            if valid(b,r,c,n):
                b[r][c] = n
                if fill(): return True
                b[r][c] = 0
        return False
    fill()
    return b

def make_puzzle(level="medium"):
    full = generate_full_board()
    if level=="easy": clues=random.randint(36,40)
    elif level=="hard": clues=random.randint(22,29)
    else: clues=random.randint(30,35)
    puzzle = copy.deepcopy(full)
    cells=[(r,c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for i in range(81-clues):
        r,c=cells[i]
        puzzle[r][c]=0
    return puzzle, full

# --- Drawing and gameplay ---
def draw_grid():
    WIN.fill(WHITE)
    for i in range(10):
        thick = 4 if i%3==0 else 1
        pygame.draw.line(WIN, BLACK, (i*60,0), (i*60,540), thick)
        pygame.draw.line(WIN, BLACK, (0,i*60), (540,i*60), thick)

def draw_board(board, selected, original):
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val!=0:
                color = BLACK if original[r][c]!=0 else BLUE
                text = FONT.render(str(val), True, color)
                WIN.blit(text, (c*60+20, r*60+10))
    if selected:
        r,c = selected
        pygame.draw.rect(WIN, RED, (c*60+2, r*60+2, 56,56), 3)

def draw_buttons():
    pygame.draw.rect(WIN, GREY, (20,550,120,40))
    pygame.draw.rect(WIN, GREY, (210,550,120,40))
    pygame.draw.rect(WIN, GREY, (400,550,120,40))
    WIN.blit(SMALL.render("New Game", True, BLACK), (30,560))
    WIN.blit(SMALL.render("Hint", True, BLACK), (250,560))
    WIN.blit(SMALL.render("Solve", True, BLACK), (430,560))

def get_cell(pos):
    x,y = pos
    if y>540: return None
    return y//60, x//60

def main():
    puzzle, solution = make_puzzle("medium")
    original = copy.deepcopy(puzzle)
    working = copy.deepcopy(puzzle)
    selected = None
    running=True

    while running:
        draw_grid()
        draw_board(working, selected, original)
        draw_buttons()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if 20<=x<=140 and 550<=y<=590:
                    puzzle, solution = make_puzzle("medium")
                    original = copy.deepcopy(puzzle)
                    working = copy.deepcopy(puzzle)
                    selected=None
                elif 210<=x<=330 and 550<=y<=590:
                    empties=[(r,c) for r in range(9) for c in range(9) if working[r][c]==0]
                    if empties:
                        r,c=random.choice(empties)
                        working[r][c]=solution[r][c]
                elif 400<=x<=520 and 550<=y<=590:
                    working = copy.deepcopy(solution)
                else:
                    selected=get_cell(event.pos)
            elif event.type==pygame.KEYDOWN and selected:
                r,c=selected
                if original[r][c]!=0: continue
                if event.key in (pygame.K_BACKSPACE, pygame.K_DELETE, pygame.K_0):
                    working[r][c]=0
                elif pygame.K_1<=event.key<=pygame.K_9:
                    num=event.key-pygame.K_0
                    if valid(working,r,c,num):
                        working[r][c]=num
                elif event.key==pygame.K_RETURN:
                    if working==solution:
                        print("🎉 You solved it!")
                        running=False

    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()
