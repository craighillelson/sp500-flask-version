from flask import Flask, jsonify, render_template_string
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)

def get_current_year_return(use_sample=True):
    """
    Get the 1-year return for the S&P 500.
    Returns the most recent price and the return from exactly 1 year ago.
    
    Think of this like: "If I bought the S&P 500 exactly one year ago, 
    what would my return be today?"
    """
    if use_sample:
        # Generate sample data for demo
        np.random.seed(42)
        current_price = 5800.50  # Sample current price
        year_ago_price = 5200.00  # Sample price from 1 year ago
        year_return = ((current_price - year_ago_price) / year_ago_price) * 100
        
        return {
            'current_price': current_price,
            'year_ago_price': year_ago_price,
            'year_return': year_return,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'is_sample': True
        }
    else:
        # Use real data from Yahoo Finance
        try:
            import yfinance as yf
            
            # Get S&P 500 data
            sp500 = yf.Ticker('^GSPC')
            
            # Get current data (last available close or intraday if market is open)
            current_data = sp500.history(period='1d')
            if current_data.empty:
                return None
            current_price = float(current_data['Close'].iloc[-1])
            
            # Get price from 1 year ago (approximately 252 trading days)
            historical_data = sp500.history(period='1y')
            if len(historical_data) < 2:
                return None
            year_ago_price = float(historical_data['Close'].iloc[0])
            
            # Calculate 1-year return
            year_return = ((current_price - year_ago_price) / year_ago_price) * 100
            
            return {
                'current_price': current_price,
                'year_ago_price': year_ago_price,
                'year_return': year_return,
                'date': current_data.index[-1].strftime('%Y-%m-%d'),
                'is_sample': False
            }
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

@app.route('/')
def index():
    """Simple HTML page to display the current 1-year return"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>S&P 500 Year Return</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                text-align: center;
            }
            h1 { color: #333; }
            .return-box {
                background: #f5f5f5;
                padding: 40px;
                border-radius: 10px;
                margin: 30px 0;
            }
            .big-number {
                font-size: 72px;
                font-weight: bold;
                margin: 20px 0;
            }
            .positive { color: #4CAF50; }
            .negative { color: #f44336; }
            .details {
                color: #666;
                margin-top: 20px;
            }
            .info-box {
                background: #e3f2fd;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
                border-left: 4px solid #2196F3;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <h1>S&P 500 One-Year Return</h1>
        
        <div class="return-box" id="returnBox">
            <p>Loading...</p>
        </div>
        
        <script>
            fetch('/api/year-return')
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('returnBox').innerHTML = 
                            '<p>Error: ' + data.error + '</p>';
                        return;
                    }
                    
                    const returnValue = data.year_return;
                    const colorClass = returnValue >= 0 ? 'positive' : 'negative';
                    const sign = returnValue >= 0 ? '+' : '';
                    
                    document.getElementById('returnBox').innerHTML = `
                        <div class="big-number ${colorClass}">${sign}${returnValue.toFixed(2)}%</div>
                        <div class="details">
                            <p><strong>Current Price:</strong> $${data.current_price.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</p>
                            <p><strong>Price 1 Year Ago:</strong> $${data.year_ago_price.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</p>
                            <p><strong>As of:</strong> ${data.date}</p>
                        </div>
                    `;
                })
                .catch(error => {
                    document.getElementById('returnBox').innerHTML = 
                        '<p>Error loading data: ' + error + '</p>';
                });
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/api/year-return')
def get_year_return():
    """API endpoint that returns the current 1-year return as JSON"""
    try:
        # Set to True for demo/testing, False for real Yahoo Finance data
        data = get_current_year_return(use_sample=False)
        
        if data is None:
            return jsonify({'error': 'Unable to fetch data'}), 404
        
        return jsonify({
            'current_price': data['current_price'],
            'year_ago_price': data['year_ago_price'],
            'year_return': data['year_return'],
            'date': data['date'],
            'is_sample_data': data['is_sample']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
