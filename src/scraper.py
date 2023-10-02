from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

URL = "https://www.nhl.com/stats/skaters?reportType=season&seasonFrom=20222023&seasonTo=20222023&gameType=2&playerPlayedFor=franchise.17&filter=gamesPlayed,gte,1&sort=points,goals,assists&page=0&pageSize=50"


def scrape_nhl_stats():
    # Configure the webdriver
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # Ensure you're using the Chromium-based version of Edge
    options.headless = True  # This will run Edge in headless mode (no GUI)

    # Initialize the webdriver
    with webdriver.Edge(options=options) as driver:
        driver.get(URL)

        try:
            table_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#root > main > div.ReactTable.-striped"))
            )

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.select_one("#root > main > div.ReactTable.-striped")

            players = []

            for row in table.select('.rt-tr-group'):
                player = {}
                try:
                    player['name'] = row.select_one('a[href*="player"]').text.strip()
                except Exception as e:
                    print("Error processing player name in a row:", e)
                    print("Row content:", row.prettify())

                try:
                    player['gp'] = int(row.select_one('div[role="cell"]:nth-child(7)').text.strip())
                except Exception as e:
                    print("Error processing games played in a row:", e)
                    print("Row content:", row.prettify())

                cells = row.select('.rt-td')
                if len(cells) > 12:  # Ensuring we have enough columns before extracting P/GP
                    try:
                        player['ppg'] = cells[12].text.strip()
                    except Exception as e:
                        print("Error processing points per game in a row:", e)
                        print("Row content:", row.prettify())

                # Extracting goals
                try:
                    player['goals'] = int(row.select_one('div:nth-child(8)').text.strip())
                except Exception as e:
                    print("Error processing goals in a row:", e)
                    print("Row content:", row.prettify())

                # Extracting assists
                try:
                    player['assists'] = int(row.select_one('div:nth-child(9)').text.strip())
                except Exception as e:
                    print("Error processing assists in a row:", e)
                    print("Row content:", row.prettify())

                # Extracting penalty minutes
                try:
                    player['pims'] = int(row.select_one('div:nth-child(12)').text.strip())
                except Exception as e:
                    print("Error processing penalty minutes in a row:", e)
                    print("Row content:", row.prettify())

                # Extracting shots
                try:
                    player['shots'] = int(row.select_one('div:nth-child(22)').text.strip())
                except Exception as e:
                    print("Error processing shots in a row:", e)
                    print("Row content:", row.prettify())

                if 'name' in player and 'gp' in player and 'ppg' in player and 'goals' in player and 'assists' in player and 'pims' in player:
                    players.append(player)

            return players

        except Exception as e:
            print(f"Error encountered: {e}")
            return None
