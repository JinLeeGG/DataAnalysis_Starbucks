# Coffee Franchise Location Strategy Analysis

A data-driven analysis examining the location strategies of coffee franchises in South Korea, specifically investigating the proximity relationship between Starbucks and its competitors.

## 📋 Project Overview

This project investigates the business hypothesis popularized by IDIYA Coffee's strategy of "defend the seat next to Starbucks" - the idea that positioning competitor coffee shops near Starbucks locations can be beneficial for business due to overflow traffic during peak hours and price differentiation.

**Project Duration:** June 30, 2025 - July 2, 2025

## 🎯 Objectives

- Analyze the spatial distribution of Starbucks locations across Seoul, South Korea
- Examine the proximity patterns between Starbucks and other major coffee franchise locations
- Validate the hypothesis that competitor coffee shops strategically locate near Starbucks stores
- Provide data-driven insights for coffee franchise location planning

## 🔍 Problem Statement

IDIYA Coffee's historical strategy was based on the premise that:
1. During peak hours (like lunchtime), Starbucks stores often reach capacity
2. Customers unable to find seats would naturally migrate to nearby alternatives
3. Price-conscious consumers would prefer lower-priced alternatives when available nearby
4. Interestingly, Starbucks locations near competitors often showed higher sales than isolated locations

This project aims to verify whether this proximity strategy is widely adopted across the Korean coffee market.

## 🛠️ Methodology

### Data Collection
- **Web Scraping**: Use Selenium to crawl Starbucks location data from the official website
- **Data Processing**: Convert scraped data to structured DataFrames using pandas
- **External Data**: Download and integrate CSV files containing other major coffee franchise locations in Korea

### Data Analysis
- Distance calculations between competing franchises using the Haversine formula
- Visualization of spatial relationships

## 🔧 Technologies Used

- **Python** - Primary programming language
- **Selenium** - Web scraping automation
- **Pandas** - Data manipulation and analysis
- **CSV** - Data storage and exchange format
- **Jupyter Notebooks** - Analysis and documentation 

## 🚀 Getting Started

### Starbucks Korea Location Web Scraper Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/coffee-location-strategy.git
cd coffee-location-strategy
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the data collection script
```bash
python DataAnalysis_Starbucks\starbucks.py
```

### Starbucks Korea Location Web Scraper Demo

![Starbucks Webscraper Demo](./demo/StarbucksKorea_Webscraper_demo.gif)

## 📊 Expected Outcomes

- Comprehensive dataset of coffee franchise locations in South Korea
- Statistical analysis of proximity patterns between Starbucks and competitors
- Validation or refutation of the "defend the seat next to Starbucks" strategy
- Actionable insights for coffee franchise location planning

## 🔍 Key Research Questions

1. Are competitor coffee shops significantly more likely to be located near Starbucks stores?
2. What is the optimal distance for competitor positioning?
3. Do urban vs. suburban areas show different proximity patterns?
4. Which coffee franchises most commonly employ proximity strategies?

## 📈 Data Sources

- Starbucks Korea official store locator
- Public datasets of major Korean coffee franchises (IDIYA, MagaCoffee, Paik's Coffee, etc.)

## 📄 License

This project is licensed under the MIT License 

## 📞 Contact

For questions or collaboration opportunities, please open an issue or contact the project maintainer.
