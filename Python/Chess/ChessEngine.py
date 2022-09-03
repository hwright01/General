import numpy

def MoveToChange(move):
    r1=r2=c1=c2=0
    c1,c2 = ord(move[0])-97,ord(move[2])-97
    r1,r2 = 8-int(move[1]),8-int(move[3])
    if len(move) == 6:
        return r1,c1,r2,c2,move[5]
    return r1,c1,r2,c2,None

def ChangeToMove(r1,c1,r2,c2):
    return ''.join((chr(c1+97),str(8-r1),chr(c2+97),str(8-r2)))

class GameState():
    def __init__(self):
        self.un = self.v = False
        self.castle = [True,True]
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.Kings = [[7,4],[0,4]]
        self.whiteToMove = True
        self.movelog = []
        self.moveFunctions = {'P' : self.GetPawnMoves, 'R' : self.GetRookMoves, 'B' : self.GetBishopMoves, 'N' : self.GetKnightMoves, 'Q' : self.GetQueenMoves, 'K' : self.GetKingMoves, }
        
    def Move(self,r1,c1,r2,c2,piece):
        if r1 == r2 and c1 == c2:
            return
        if not self.v:
            moves = self.GetValidMoves()
            if ChangeToMove(r1,c1,r2,c2) not in moves:
                if ChangeToMove(r1,c1,r2,c2) + '=Q' not in moves:
                    return
        if piece != None:
            self.board[r2][c2] = self.board[r1][c1][0] + piece
            self.board[r1][c1] = '--'
            if self.un == False:
                self.movelog.append(ChangeToMove(r1,c1,r2,c2) + '=' + piece)
            if [r1,c1] in self.Kings:
                    self.Kings[self.Kings.index([r1,c1])] = [r2,c2]
            self.whiteToMove = not self.whiteToMove
        else:
            if self.board[r1][c1][1] == 'P' and self.board[r2][c2] == '--':
                self.board[r2][c2] = self.board[r1][c1]
                self.board[r1][c2] = self.board[r1][c1] = '--'
            else:
                self.board[r2][c2] = self.board[r1][c1]
                self.board[r1][c1] = '--'
            if self.board[r2][c2][1] == 'K' and abs(c2-c1) > 1:
                if self.whiteToMove:
                    self.board[r1][c2-numpy.sign(c2-c1)] = 'wR'
                    self.board[r1][int(3.5*(1+numpy.sign(c2-c1)))] = '--'
                    self.castle[0] = False
                else:
                    self.board[r1][c2-numpy.sign(c2-c1)] = 'bR'
                    self.board[r1][int(3.5*(1+numpy.sign(c2-c1)))] = '--'
                    self.castle[1] = False
            if self.un == False:
                self.movelog.append(ChangeToMove(r1,c1,r2,c2))
            if [r1,c1] in self.Kings:
                 self.Kings[self.Kings.index([r1,c1])] = [r2,c2]
            self.whiteToMove = not self.whiteToMove
        return

    def Undo(self):
        if len(self.movelog) == 0:
            return
        self.un = self.v = True
        del(self.movelog[-1])
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.Kings = [[7,4],[0,4]]
        self.whiteToMove = True
        self.castle = [True,True]
        for moves in self.movelog:
            if len(moves) == 4:
                self.Move(MoveToChange(moves)[0],MoveToChange(moves)[1],MoveToChange(moves)[2],MoveToChange(moves)[3],None)
            elif len(moves) == 6:
                self.Move(MoveToChange(moves)[0],MoveToChange(moves)[1],MoveToChange(moves)[2],MoveToChange(moves)[3],moves[5])
        self.un = self.v = False
        return
    
    def GetPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (self.whiteToMove == True and turn == 'w') or (self.whiteToMove == False and turn == 'b'):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r,c,moves)
        return moves

    def GetValidMoves(self):
        moves = self.GetPossibleMoves()
        validMoves = []
        for m in moves:
            self.v = True
            r1,c1,r2,c2,piece = MoveToChange(m)
            if self.board[r1][c1][1] == 'K' and abs(c2-c1) > 1:
                for i in range(c1+1,c2+numpy.sign(c2-c1),numpy.sign(c2-c1)):
                    self.v = True
                    self.Move(r1,c1,r2,i,piece)
                    self.whiteToMove = not self.whiteToMove
                    if self.IsCheck():
                        self.Undo()
                        break
                    self.Undo()
                    if i == c2: validMoves.append(m)
            else:
                self.Move(r1,c1,r2,c2,piece)
                self.whiteToMove = not self.whiteToMove
                if  not self.IsCheck():
                    validMoves.append(m)
                self.Undo()
        self.v = False
        return validMoves
    
    def IsCheck(self):
        moves = []
        [[r,c],enemyColour] = [self.Kings[0],'b'] if self.whiteToMove else [self.Kings[1],'w']
        for p in self.moveFunctions:
            self.moveFunctions[p](r,c,moves)
            for m in moves:
                _,_,r1,c1,piece = MoveToChange(m)
                if piece == None:
                    if self.board[r1][c1] == enemyColour+p:
                        return True
                elif self.board[r1][c1] == enemyColour+piece:
                    return True
            moves = []
        return False
    
    def IsCheckMate(self):
        moves = self.GetValidMoves()
        if self.IsCheck() and moves == []:
            return True
        return False
    
    def IsStaleMate(self):
        moves = self.GetValidMoves()
        if not self.IsCheck() and moves == []:
            return True
        return False

    def GetPawnMoves(self,r,c,moves):
        if self.whiteToMove == True:
            if self.board[r-1][c] == '--':
                moves.append(ChangeToMove(r,c,r-1,c))
                if r == 6 and self.board[r-2][c] == '--':
                    moves.append(ChangeToMove(r,c,r-2,c))
                if r == 1:
                    moves.extend([moves[-1]+'=Q',moves[-1]+'=R',moves[-1]+'=N',moves[-1]+'=B',])
                    del moves[-5]
            if c-1 >= 0:
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(ChangeToMove(r,c,r-1,c-1))
                    if r == 1:
                        moves.extend([moves[-1]+'=Q',moves[-1]+'=R',moves[-1]+'=N',moves[-1]+'=B',])
                        del moves[-5]
                elif r == 3 and self.board[r][c-1] == 'bP' and self.movelog[-1] == ChangeToMove(r-2,c-1,r,c-1):
                    moves.append(ChangeToMove(r,c,r-1,c-1))
            if c+1 <= 7:
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(ChangeToMove(r,c,r-1,c+1))
                    if r == 1:
                        moves.extend([moves[-1]+'=Q',moves[-1]+'=R',moves[-1]+'=N',moves[-1]+'=B',])
                        del moves[-5]
                elif r == 3 and self.board[r][c+1] == 'bP' and self.movelog[-1] == ChangeToMove(r-2,c+1,r,c+1):
                    moves.append(ChangeToMove(r,c,r-1,c+1))
        else:
            if self.board[r+1][c] == '--':
                moves.append(ChangeToMove(r,c,r+1,c))
                if r == 1 and self.board[r+2][c] == '--':
                    moves.append(ChangeToMove(r,c,r+2,c))
                if r == 6:
                    moves.extend([moves[-1]+'=Q',moves[-1]+'=R',moves[-1]+'=N',moves[-1]+'=B',])
                    del moves[-5]
            if c-1 >= 0:
                if self.board[r+1][c-1][0] == 'w':
                    moves.append(ChangeToMove(r,c,r+1,c-1))
                    if r == 6:
                        moves.extend([moves[-1]+'=Q',moves[-1]+'=R',moves[-1]+'=N',moves[-1]+'=B',])
                        del moves[-5]
                elif r == 4 and self.board[r][c-1] == 'wP' and self.movelog[-1] == ChangeToMove(r+2,c-1,r,c-1):
                    moves.append(ChangeToMove(r,c,r+1,c-1))
            if c+1 <= 7:
                if self.board[r+1][c+1][0] == 'w':
                    moves.append(ChangeToMove(r,c,r+1,c+1))
                    if r == 6:
                        moves.extend([moves[-1]+'=Q',moves[-1]+'=R',moves[-1]+'=N',moves[-1]+'=B',])
                        del moves[-5]
                elif r == 4 and self.board[r][c+1] == 'wP' and self.movelog[-1] == ChangeToMove(r+2,c+1,r,c+1):
                    moves.append(ChangeToMove(r,c,r+1,c+1))
    
    def GetRookMoves(self,r,c,moves):
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        enemyColour = 'b' if self.whiteToMove else 'w'
        for d in directions:
            for i in range(1,8):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    if self.board[endrow][endcol] == '--':
                        moves.append(ChangeToMove(r,c,endrow,endcol))
                    elif self.board[endrow][endcol][0] == enemyColour:
                        moves.append(ChangeToMove(r,c,endrow,endcol))
                        break
                    else:
                        break
                else:
                    break

    def GetBishopMoves(self,r,c,moves):
        directions = ((-1,-1),(-1,1),(1,-1),(1,1))
        enemyColour = 'b' if self.whiteToMove else 'w'
        for d in directions:
            for i in range(1,8):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    if self.board[endrow][endcol] == '--':
                        moves.append(ChangeToMove(r,c,endrow,endcol))
                    elif self.board[endrow][endcol][0] == enemyColour:
                        moves.append(ChangeToMove(r,c,endrow,endcol))
                        break
                    else:
                        break
                else:
                    break

    def GetKnightMoves(self,r,c,moves):
        directions = ((1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1))
        allyColour = 'w' if self.whiteToMove else 'b'
        for d in directions:
            endrow = r + d[0]
            endcol = c + d[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                if self.board[endrow][endcol][0] != allyColour:
                    moves.append(ChangeToMove(r,c,endrow,endcol))

    def GetQueenMoves(self,r,c,moves):
        self.GetBishopMoves(r,c,moves)
        self.GetRookMoves(r,c,moves)


    def GetKingMoves(self,r,c,moves):
        directions = ((0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1))
        allyColour = 'w' if self.whiteToMove else 'b'
        for d in directions:
            endrow = r + d[0]
            endcol = c + d[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                if self.board[endrow][endcol][0] != allyColour:
                    moves.append(ChangeToMove(r,c,endrow,endcol))
        if self.whiteToMove and self.castle[0] == True:
            if self.board[7][1] == '--' and self.board[7][2] == '--' and self.board[7][3] == '--':
                  moves.append('e1c1')
            if self.board[7][5] == '--' and self.board[7][6] == '--':
                moves.append('e1g1')
        elif self.castle[1] == True:
            if self.board[0][1] == '--' and self.board[0][2] == '--' and self.board[0][3] == '--':
                moves.append('e8c8')
            if self.board[0][5] == '--' and self.board[0][6] == '--':
                moves.append('e8g8')

    
