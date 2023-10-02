from matplotlib import pyplot as plt
from src.scraper import scrape_nhl_stats
from src.visualizations import plot_ppg, plot_gps, plot_stevens_index
from src.stevens_index import calculate_stevens_index

def main():
    # Scrape data
    players_data = scrape_nhl_stats()
    if not players_data:
        print("Failed to retrieve player data.")
        return

    # Prepare data for Points per Game visualization
    player_names_ppg = [player['name'] for player in players_data]
    ppg_values = [float(player['ppg']) for player in players_data]

    # Plot Points per Game visualization
    plot_ppg(player_names_ppg, ppg_values)

    # Prepare data for Goals per Shot visualization
    player_names_gps = [player['name'] for player in players_data if player.get('shots') and player['shots'] > 0]
    goals = [player['goals'] for player in players_data if player.get('shots') and player['shots'] > 0]
    shots = [player['shots'] for player in players_data if player.get('shots') and player['shots'] > 0]

    # Plot Goals per Shot visualization
    plot_gps(player_names_gps, goals, shots)

    # Calculate Stevens Index
    sorted_players = calculate_stevens_index(players_data)
    stevens_indices = [player['stevens_index'] for player in sorted_players]
    player_names_for_stevens = [player['name'] for player in sorted_players]
    player_names_for_stevens.append("Kevin Stevens '91-'92")
    stevens_indices.append(1)

    # Visualize Stevens Index
    plot_stevens_index(player_names_for_stevens, stevens_indices)

if __name__ == '__main__':
    main()
    plt.show()
