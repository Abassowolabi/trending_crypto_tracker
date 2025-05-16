import requests
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
import logging

# Initialize colorama for colored terminal output
init(autoreset=True)

# Set up logging to print messages to the terminal only
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fetch market data for top coins from CoinGecko API
def get_market_data(limit=250):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",              # Prices in USD
        "order": "market_cap_desc",        # Sort by market cap descending
        "per_page": limit,                 # Number of coins per page
        "page": 1                         # Page number
    }

    try:
        # Send GET request to API with headers
        response = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()        # Raise exception for HTTP errors
        logging.info(f"Successfully fetched market data for {limit} coins.")
        return response.json()             # Return JSON data as Python list
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch coin data: {e}")
        return []                         # Return empty list on failure

# Format 24h price change with colors and arrows for terminal output
def format_change(change):
    if change is None:
        return "N/A"
    elif change >= 0:
        return f"{Fore.GREEN}🔼 {change:.2f}%{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}🔽 {abs(change):.2f}%{Style.RESET_ALL}"

# Display top gainers in terminal and save their data to JSON
def display_and_save_top_gainers(coins, top_n=30):
    # Filter coins that have valid 24h change values
    gainers = [coin for coin in coins if coin.get('price_change_percentage_24h') is not None]
    # Sort coins by 24h price change descending
    gainers.sort(key=lambda x: x['price_change_percentage_24h'], reverse=True)
    top_gainers = gainers[:top_n]

    print(f"\nTop {top_n} Crypto Gainers in the Last 24 Hours:\n")
    simplified_data = []

    # Loop through top gainers and print their details
    for coin in top_gainers:
        print(f"Name       : {coin['name']}")
        print(f"Symbol     : {coin['symbol'].upper()}")
        print(f"Price      : ${coin['current_price']:,}")
        print(f"24h Change : {format_change(coin['price_change_percentage_24h'])}")
        print(f"Market Cap : ${coin['market_cap']:,}")
        print("-" * 40)

        # Prepare simplified data for JSON saving
        simplified_data.append({
            "name": coin["name"],
            "symbol": coin["symbol"],
            "current_price": coin["current_price"],
            "price_change_percentage_24h": coin["price_change_percentage_24h"],
            "market_cap": coin["market_cap"]
        })

    # Create 'data' folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Create timestamped filename for JSON
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    json_filename = os.path.join("data", f"top_gainers_{timestamp}.json")

    # Write the simplified data to JSON file
    with open(json_filename, "w") as f:
        json.dump(simplified_data, f, indent=4)

    logging.info(f"Saved top {top_n} gainers to {json_filename}")

    # Generate and save the bar chart for top gainers
    generate_chart(simplified_data, timestamp)

# Generate and save a bar chart showing 24h % change for top gainers
def generate_chart(gainers, timestamp):
    try:
        # Extract coin symbols and 24h changes for plotting
        names = [coin["symbol"].upper() for coin in gainers]
        changes = [coin["price_change_percentage_24h"] for coin in gainers]

        # Create figure with size
        plt.figure(figsize=(14, 7))
        bars = plt.bar(names, changes, color='green')

        # Set axis labels and chart title
        plt.xlabel("Coin Symbol")
        plt.ylabel("24h % Change")
        plt.title("Top 30 Crypto Gainers (24h Change)")

        # Add subtitle with timestamp, larger font and dark blue color
        plt.suptitle(f"Data captured on: {timestamp}", y=0.92, fontsize=16, color='#003366')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Adjust layout to make room for subtitle
        plt.tight_layout(rect=[0, 0, 1, 0.9])

        # Annotate each bar with its corresponding change percentage
        for bar, change in zip(bars, changes):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{change:.1f}%", ha='center', va='bottom')

        # Create 'charts' folder if it doesn't exist
        os.makedirs("charts", exist_ok=True)

        # Build full path for chart file
        filename = os.path.join("charts", f"top_gainers_chart_{timestamp}.png")

        # Save the chart to file and close the plot
        plt.savefig(filename)
        plt.close()

        logging.info(f"Saved chart as {filename}")
    except Exception as e:
        logging.error(f"Chart generation failed: {e}")

# Program entry point
def main():
    logging.info("Script started.")
    coins = get_market_data(limit=250)
    if coins:
        display_and_save_top_gainers(coins, top_n=30)
    logging.info("Script finished.\n")

if __name__ == "__main__":
    main()
