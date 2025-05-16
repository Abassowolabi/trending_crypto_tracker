# 🚀 Trending Crypto Tracker

Track the top 30 biggest crypto gainers in the last 24 hours — in real-time, from your terminal.

This Python script pulls live data from the CoinGecko API, filters out the top-performing coins based on 24-hour percentage gains, displays them with colorful output (up/down arrows included!), saves each snapshot to JSON, and generates a clean bar chart showing price changes.

---

## 🔧 Features

- 📈 **Live market scan**: Fetches the top 250 coins by market cap from CoinGecko
- 🚀 **Top gainer detection**: Sorts and selects the top 30 coins with the highest 24h percentage gains
- 🎨 **Colorful CLI**: Displays data in the terminal with green/red arrows for gain/loss
- 💾 **Data snapshots**: Automatically saves results to timestamped JSON files
- 📊 **Chart generation**: Produces bar charts for quick visual comparison
- 🧠 **Smart output**: Skips coins with missing data for cleaner insights
- 🔐 **No API key required**

---

## 📁 Folder Structure

```

trending_crypto_tracker/
├── trending_crypto.py     # Main script
├── data/                  # JSON snapshots (auto-saved)
└── charts/                # PNG bar charts (auto-saved)

````

---

## 🚀 Quick Start

Clone the repo, install dependencies, and run the script:

```shell
git clone https://github.com/Abassowolabi/trending_crypto_tracker.git
cd trending_crypto_tracker
pip install requests matplotlib colorama
python trending_crypto.py
````

---

## 💡 What You’ll See

Each run prints out the top 30 crypto gainers in the past 24 hours with:

* Name and symbol
* Current price (USD)
* Market cap
* 24h change (colored with arrows)

It also:

* Creates a `.json` file in the `data/` folder
* Generates a `.png` chart in the `charts/` folder

You can run this as often as you'd like to monitor crypto trends!

---

## 📌 Notes

* ✅ Requires no API keys or authentication
* 🖼️ Charts are created using `matplotlib`
* 🔁 Easily automatable using GitHub Actions or cron jobs

---

## 📄 License

**MIT** — Feel free to use it, fork it, improve it, and share it!
Attribution is appreciated but not required.

---

Made with 🧠 and ☕ by [Abassowolabi](https://github.com/Abassowolabi)


