# https://www.codewars.com//kata/5e28ae347036fa001a504bbe

MOVES = {
    '♜': [[x*m for m in range(1,9)] for x in (-1,-1j,1,1j)],
    '♝': [[x*m for m in range(1,9)] for x in (-1-1j,-1+1j,1-1j,1+1j)],
    '♞': [[x+1j*m] for m in range(-2,3) for x in range(-2,3) if abs(x*m) == 2],
    '♟': [[1-1j], [1+1j]],
}
MOVES['♛'] = MOVES['♜'] + MOVES['♝']

def king_is_in_check(chessboard):
    pieces = {x + 1j * y: piece for x, row in enumerate(chessboard)
              for y, piece in enumerate(row) if piece != ' '}
    for z, piece in pieces.items():
        for it in MOVES.get(piece, ()):
            for dz in it:
                if z+dz in pieces:
                    if pieces.get(z+dz) == '♔':
                        return True
                    break
    return False