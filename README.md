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

## Current Setup (Demo Mode)

The app currently uses **sample data** (S&P 500 at ~$5,800 with an 11.55% return) so you can test it anywhere.

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

## Switching to Real Data

To use real Yahoo Finance data instead of simulated data:

1. Open `sp500_app.py`
2. Find line 85: `data = get_current_year_return(use_sample=True)`
3. Change it to: `data = get_current_year_return(use_sample=False)`
4. Restart the Flask app

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

## Next Steps: Adding React

Once you're happy with the Flask backend, you can:

1. **Create a React app:** `npx create-react-app sp500-frontend`
2. **Fetch data from the API:** Use `fetch()` or `axios` to call `/api/rolling-returns`
3. **Add visualizations:** Use libraries like:
   - **Recharts** (simple, React-friendly charts)
   - **Chart.js** (powerful charting library)
   - **D3.js** (for advanced custom visualizations)

## Understanding the Code

### Key Functions:

1. **`get_current_year_return()`** - The main calculation
   - Gets the current S&P 500 price (or latest close if market is closed)
   - Gets the S&P 500 price from exactly 1 year ago
   - Calculates: `(current - year_ago) / year_ago × 100`
   - Returns a simple dictionary with the results

2. **`get_year_return()`** - Flask API endpoint
   - Calls `get_current_year_return()`
   - Returns data as JSON for easy consumption by frontends

That's it! Just ~80 lines of straightforward code.

## Questions?

The Flask app is ready to go! When you're ready, we can:
- Add the React frontend to make it look nice
- Add a chart showing the year's price movement
- Add comparisons to other time periods
- Display additional market info

Just let me know what you'd like to tackle next!
