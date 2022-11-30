# https://www.codewars.com//kata/58a3b28b2f949e21b3000001

PIECES_MOVES = {1: [(1,0), (-1,0),  (0,1),  (0,-1)],
               -1: [(1,1), (-1,-1), (-1,1), (1,-1)]}

def bishops_and_rooks(chessboard):

    def theRootOfAllEvil(r, c):
        evilIsHere.add( (r,c) )
        for dr,dc in PIECES_MOVES[chessboard[r][c]]:
            for i in range(1,8):
                x,y = r + dr*i, c + dc*i
                if not( 0 <= x < 8 and 0 <= y < 8 ) or chessboard[x][y] != 0: break
                evilIsHere.add( (x,y) )

    evilIsHere = set()
    for r in range(8):
        for c in range(8):
            if chessboard[r][c] != 0: theRootOfAllEvil(r,c)
    
    return 64 - len(evilIsHere)