import json

def test_edge_multiple_analysis():
    # Simulate a case where more than 10 plot URLs are provided
    event = {
        "plot_urls": [
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/AAPL.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/GOOGL.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/TSLA.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/AMZN.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/MSFT.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/NVDA.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/F.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/BA.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/KO.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/IBM.png",
            "https://your-bucket-name.s3.amazonaws.com/stock_plots/T.png"
        ]
    }
    response = analyze_multiple_stock_plots(event, None)
    result = json.loads(response['body'])
    
    assert 'message' in result
    assert result['message'] == 'You can only submit up to 10 plot URLs.'