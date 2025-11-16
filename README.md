# S&P 500 One-Year Return Flask App

A simple Flask application that displays the current one-year return for the S&P 500.

## What This App Does

Shows you **one simple number**: the S&P 500's return over the past year.

- If the market is **closed**: Shows the return based on the previous close
- If the market is **open**: Shows the return based on the most current data

**The Calculation:**
It's like asking, "If I bought the S&P 500 exactly one year ago, what would my return be today?"
```
Return = (Current Price - Price 1 Year Ago) / Price 1 Year Ago × 100
```

## Features

- ✅ Displays current 1-year return percentage
- ✅ Shows current price vs. price from 1 year ago
- ✅ Simple, clean interface
- ✅ JSON API endpoint for future React integration

## Files

- `sp500_app.py` - Main Flask application
- `requirements.txt` - Python dependencies

## How to Run Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app:**
   ```bash
   python sp500_app.py
   ```

3. **Open your browser:**
   - Go to `http://localhost:5000`
   - You'll see the 1-year return displayed in large numbers

4. **Test the API directly:**
   ```bash
   curl http://localhost:5000/api/year-return
   ```

**Note:** This requires internet access to fetch data from Yahoo Finance.

## API Endpoint

**GET** `/api/year-return`

Returns JSON with:
```json
{
  "current_price": 5800.50,
  "year_ago_price": 5200.00,
  "year_return": 11.55,
  "date": "2025-11-15",
  "is_sample_data": true
}
```

### Key Functions:

1. **`get_current_year_return()`** - The main calculation
   - Gets the current S&P 500 price (or latest close if market is closed)
   - Gets the S&P 500 price from exactly 1 year ago
   - Calculates: `(current - year_ago) / year_ago × 100`
   - Returns a simple dictionary with the results

2. **`get_year_return()`** - Flask API endpoint
   - Calls `get_current_year_return()`
   - Returns data as JSON for easy consumption by frontends
