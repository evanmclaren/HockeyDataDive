# src/stevens_index.py

def calculate_stevens_index(players_data):
    # Kevin Stevens' per-game metrics from the 1991-1992 season
    STEVENS_METRICS = {
        'goals_per_game': 54 / 80,
        'assists_per_game': 69 / 80,
        'points_per_game': (54 + 69) / 80,
        'pims_per_game': 254 / 80
    }

    for player in players_data:
        # Calculate per-game metrics for the current player
        player_goals_per_game = player['goals'] / player['gp']
        player_assists_per_game = player['assists'] / player['gp']
        player_points_per_game = (player['goals'] + player['assists']) / player['gp']
        player_pims_per_game = player['pims'] / player['gp']

        # Store the per-game metrics in a temporary dictionary for easier comparison
        player_metrics = {
            'goals_per_game': player_goals_per_game,
            'assists_per_game': player_assists_per_game,
            'points_per_game': player_points_per_game,
            'pims_per_game': player_pims_per_game
        }

        total_difference = 0

        # Calculate the Stevens Index by comparing each metric
        for key, value in STEVENS_METRICS.items():
            total_difference += abs(player_metrics[key] - value)

        player['stevens_index'] = 1 / (1 + total_difference)

    # Sort the players based on their Stevens Index
    sorted_players = sorted(players_data, key=lambda x: x['stevens_index'])

    return sorted_players

