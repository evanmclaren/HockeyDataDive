# NHL Player Statistics Analysis: The Stevens Index

While navigating the job application process, I felt I was lacking a tangible example of my coding abilities, especially in the area of data extraction, processing, and visualization. I decided to spend some time learning data scraping techniques, which I'd never used before, and chose to focus on statistics from professional ice hockey, involving a personal interest in analytics that I would like to develop in more depth in the future.

Over a span of two days, with ChatGPT serving as my private tutor, this project gradually took shape. On the way I was inspired to formulate a novel statistical index. Named the **Stevens Index**, it measures a player's performance in relation to Kevin Stevens' remarkable 1991-92 NHL season — a season that stands out as arguably the greatest power forward performance in league history. Stevens, playing on the left wing with Mario Lemieux at center and Rick Tocchet on the right side, was able to net 54 goals and 69 assists, all the while racking up an astounding 254 penalty minutes.

Thanks for checking out this little coding journey of mine. Go check out some of number 25's highlight goals on YouTube!

## Overview

The Stevens Index takes into account four critical metrics: Goals per Game, Assists per Game, Points per Game, and Penalty Minutes per Game. The closer a player's season mirrors Kevin Stevens' 1991-1992 season in these areas, the better their Stevens Index.

This repository includes:
- A web scraper to gather player statistics from the NHL's official website.
- Calculations for various metrics, including the Stevens Index.
- Visualizations for analyzing these metrics.

## Dependencies

- [Python](https://www.python.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)
- [matplotlib](https://matplotlib.org/)

## Quick Start

1. Clone this repository.
```
git clone [repository_link]
```

2. Navigate to the project directory.
```
cd [project_directory_name]
```

3. Install the required dependencies.
```
pip install -r requirements.txt
```

4. Run the main script to start the analysis.
```
python main.py
```

This will scrape the data, calculate metrics, and provide visualizations including the Stevens Index.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)