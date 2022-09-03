import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT/DIMENSION
IMAGES = {}
FPS=144

def loadImages():
    pieces = ["bP","bQ","bK","bB","bN","bR","wP","wQ","wK","wB","wN","wR","bPt","bQt","bKt","bBt","bNt","bRt","wPt","wQt","wKt","wBt","wNt","wRt"]
    for piece in pieces:
        IMAGES[piece] = p.transform.smoothscale(p.image.load("Python/Chess/Images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))

def DrawState(screen,board,selected_piece,moves):
    x,y=p.mouse.get_pos()
    colours = [p.Color('white'),p.Color('brown')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour=colours[(r+c) % 2]
            p.draw.rect(screen,colour,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    if selected_piece != None:
        for m in moves:
            _,_,r1,c1,_ = ChessEngine.MoveToChange(m)
            p.draw.circle(screen,p.Color('green'),((c1+0.5)*SQ_SIZE,(r1+0.5)*SQ_SIZE),5)
        screen.blit(IMAGES[selected_piece],(x-0.5*SQ_SIZE,y-0.5*SQ_SIZE))

def squareUnderMouse(screen,board):
    x,y=p.mouse.get_pos()
    c,r=int(x//SQ_SIZE),int(y//SQ_SIZE)
    return board[r][c],r,c

def KeyPromote():
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p. KEYDOWN:
                if event.key == p.K_q:
                    return 'Q'
                if event.key == p.K_r:
                    return 'R'
                if event.key == p.K_n:
                    return 'N'
                if event.key == p.K_b:
                    return 'B'

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    gs = ChessEngine.GameState()
    selected_piece,promote,moves,r0,c0 = None,None,[],0,0
    loadImages()
    while True:
        DrawState(screen,gs.board,selected_piece,moves)
        piece,r,c=squareUnderMouse(screen,gs.board)
        for e in p.event.get():        
            if e.type == p.QUIT:
                return
            if e.type == p.MOUSEBUTTONDOWN:
                if piece != '--' and selected_piece == None:
                    moves = gs.GetValidMoves()
                    if gs.IsCheckMate(): print('Checkmate!')
                    if gs.IsStaleMate(): print('Checkmate!')
                    gs.board[r][c] = piece + 't'
                    gs.moveFunctions[piece[1]](r,c,moves)
                    moves = list(set([x for x in moves if moves.count(x) > 1]))
                    if moves != [] and len(moves[0]) == 6:
                        promote = True
                    selected_piece,r0,c0=piece,r,c
            if e.type == p.MOUSEBUTTONUP and selected_piece != None:
                if promote:
                    promote = KeyPromote()
                gs.board[r0][c0]=selected_piece
                gs.Move(r0,c0,r,c,promote)
                selected_piece,moves,promote=None,[],None
            if e.type == p.KEYDOWN:
                if e.key == p.K_1:
                    print(gs.movelog)
                if e.key == p.K_LEFT:
                    gs.Undo()
                if e.key == p.K_2:
                    print(gs.GetValidMoves())
                if e.key == p.K_3:
                    print(gs.IsCheck())
                if e.key == p.K_4:
                    print(gs.Kings)
        clock.tick(FPS)
        p.display.flip()
    
main()