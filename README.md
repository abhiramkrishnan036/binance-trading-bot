# Binance Futures Demo Trading Bot (Python CLI)

A professional command-line trading bot built in Python that connects to Binance Futures Demo API. This bot allows users to place market and limit orders using a clean CLI interface with proper validation, logging, and error handling.

This project demonstrates API integration, modular Python architecture, CLI development, and secure environment variable handling.

---

## Features

- Binance Futures Demo API integration
- Command Line Interface (CLI) support
- Market order execution
- Limit order execution
- Input validation
- Error handling with proper logging
- Secure API key management using .env
- Modular and scalable architecture
- Professional logging system

---

## Project Structure
binance-trading-bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance API client setup
│ ├── orders.py # Order execution logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging configuration
│
├── logs/
│ └── trading_bot.log # Log file
│
├── cli.py # Command line entry point
├── requirements.txt # Dependencies
├── .env # Environment variables (not uploaded)
└── README.md

---

## Technologies Used

- Python 3.12
- Binance Futures Demo API
- python-binance library
- dotenv for environment variables
- logging module
- argparse for CLI interface

---

## Installation

Clone the repository:

Install dependencies:

---

## Environment Setup
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
BASE_URL=https://demo-fapi.binance.com

---

## Usage

Example Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Example Limit Order:
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 60000

---

## Example Output
Order placed successfully!
Order ID: 123456789
Status: NEW
Executed Quantity: 0.000
Average Price: 0.00
logs/trading_bot.log


Logs include:

- Order requests
- API responses
- Errors
- System events

---

## Skills Demonstrated

- API Integration
- Python CLI Development
- Error Handling
- Logging Systems
- Environment Variable Security
- Modular Software Design
- Real-world trading system architecture

---

## Disclaimer

This bot uses Binance Futures Demo environment and does not trade real funds.

---

## Author

Abhiram Krishnan  
GitHub: https://github.com/abhiramkrishnan036
