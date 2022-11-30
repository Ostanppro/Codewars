# https://www.codewars.com//kata/5bebcbf2832c3acc870000f6

def score(hand):
    score = sum( int(c) if c.isdigit() else 11 if c == "A" else 10 for c in hand )
    aces = hand.count("A")
    
    for _ in range(aces):
        if score > 21:
            score -= 10
    
    return "BJ" if score == 21 and len(hand) == 2 else score if score <= 21 else 0


def winners(player1, player2, player3, dealer, deck):
    p1, p2, p3, house = map(score, (player1, player2, player3, dealer))
    
    if house == "BJ":
        return []
    
    deck = deck[::-1]
    
    while 0 < house < 17 and deck:
        dealer.append(deck.pop())
        house = score(dealer)
    
    return ( ["Player 1"] * (p1 == "BJ" or p1 > house) +
             ["Player 2"] * (p2 == "BJ" or p2 > house) + 
             ["Player 3"] * (p3 == "BJ" or p3 > house) + 
             [] )