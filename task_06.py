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
    if (
            (player1 == 'R' and player2 == 'S') or
            (player1 == 'S' and player2 == 'P') or
            (player1 == 'P' and player2 == 'R')
    ):
        return str(player1[0]) + ' ' + str(player1[1])
    if player1[1] == player2[1]:
        return str(player1[0]) + ' ' + str(player1[1])
    else:
        return str(player2[0]) + ' ' + str(player2[1])


# print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
