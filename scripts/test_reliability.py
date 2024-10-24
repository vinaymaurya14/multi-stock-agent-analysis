import requests

def test_reliability(api_url, payload, runs=10):
    failures = 0
    for i in range(runs):
        response = requests.post(api_url, json=payload)
        if response.status_code != 200:
            failures += 1
        print(f"Run {i+1}/{runs}: {response.status_code}")
    
    print(f"Number of failures: {failures}/{runs}")
    return failures

# Example usage
api_url = "https://your-api-gateway-endpoint"
payload = {
    "plot_urls": [
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/AAPL.png",
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/GOOGL.png"
    ]
}
test_reliability(api_url, payload, runs=20)