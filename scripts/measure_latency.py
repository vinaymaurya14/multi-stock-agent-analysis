import time
import requests

# Measure latency for API response
def measure_latency(api_url, payload):
    start_time = time.time()  # Record start time
    response = requests.post(api_url, json=payload)  # Make API request
    end_time = time.time()  # Record end time
    
    latency = end_time - start_time  # Calculate latency in seconds
    return latency, response.json()

# Example usage
api_url = "https://your-api-gateway-endpoint"
payload = {
    "plot_urls": [
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/AAPL.png",
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/GOOGL.png"
    ]
}
latency, result = measure_latency(api_url, payload)
print(f"Latency: {latency:.2f} seconds")
print(f"Result: {result}")