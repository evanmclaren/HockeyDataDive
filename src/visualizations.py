import matplotlib.pyplot as plt


def plot_ppg(player_names, ppg_values):
    plt.figure(figsize=(14, 8))

    # Bar chart for PPG
    plt.barh(player_names, ppg_values, color='skyblue')

    # Title and labels
    plt.title("Points per Game (P/GP) for Players")
    plt.xlabel("P/GP")
    plt.ylabel("Player Names")

    # Display the plot
    plt.gca().invert_yaxis()  # Invert y-axis to have the player with the highest P/GP at the top
    plt.tight_layout()


def plot_gps(player_names, goals, shots):
    # Calculate GPS values
    gps_values = [g/s if s != 0 else 0 for g, s in zip(goals, shots)]

    plt.figure(figsize=(14, 8))

    # Scatter plot for GPS
    plt.scatter(gps_values, player_names, color='coral', s=100)  # s sets the size of each dot

    # Title and labels
    plt.title("Goals Per Shot (GPS) for Players")
    plt.xlabel("GPS")
    plt.ylabel("Player Names")

    # Display the plot
    plt.gca().invert_yaxis()  # Invert y-axis to have the player with the highest GPS at the top
    plt.tight_layout()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

def plot_stevens_index(player_names, stevens_indices):
    plt.figure(figsize=(14, 8))

    # Bar chart for Stevens Index
    colors = ['red' if name == "Kevin Stevens '91-'92" else 'lightgreen' for name in player_names]
    plt.barh(player_names, stevens_indices, color=colors)

    # Title and labels
    plt.title("Stevens Index for Players")
    plt.xlabel("Stevens Index")
    plt.ylabel("Player Names")

    # Display the plot
    plt.gca().invert_yaxis()  # Invert y-axis to have the player with the lowest Stevens Index (closest to ideal) at the top
    plt.tight_layout()
