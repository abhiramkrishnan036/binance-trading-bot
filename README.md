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
