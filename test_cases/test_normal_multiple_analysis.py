import json

def test_normal_multiple_analysis():
    event = {
        "plot_urls": [
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/AAPL.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/GOOGL.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/TSLA.png"
        ]
    }
    response = analyze_multiple_stock_plots(event, None)
    result = json.loads(response['body'])
    
    assert 'top_stocks' in result
    assert len(result['top_stocks']) > 0