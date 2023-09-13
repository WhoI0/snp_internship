class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    options = ['R', 'P', 'S']
    if len(players) != 2:
        raise WrongNumberOfPlayersError()
    for player in players:
        if player[1] not in options:
            raise NoSuchStrategyError()
    player1, player2 = players
    if (player1 == 'R' and player2 == 'S') or (player1 == 'S' and player2 == 'P') or (player1 == 'P' and player2 == 'R'):
        return player1
    if player1[1] == player2[1]:
        return player1
    else:
        return player2


print(rps_game_winner([ ["player1", "P"], ["player2", "P"]]))