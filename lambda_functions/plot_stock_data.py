import pandas as pd
import matplotlib.pyplot as plt
import boto3
import os
from io import BytesIO

s3_client = boto3.client('s3')

def plot_stock_data(event, context):
    # Parse the incoming file data (assuming the file is uploaded as base64-encoded)
    file_data = event['body']  # Assume the file is passed as base64-encoded CSV
    stock_file = pd.read_csv(BytesIO(file_data))
    
    bucket_name = os.environ['BUCKET_NAME']  # S3 bucket name to store plots
    plot_urls = []
    
    for stock in stock_file['StockName'].unique():
        stock_data = stock_file[stock_file['StockName'] == stock]
        
        # Plot stock prices
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Date'], stock_data['Price'], label=stock)
        plt.title(f'{stock} Stock Price Over 3 Months')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        
        # Save plot to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        
        # Upload plot to S3
        s3_key = f'stock_plots/{stock}.png'
        s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=buffer, ContentType='image/png')
        
        # Generate URL to the plot
        plot_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
        plot_urls.append(plot_url)
        
        # Clear the plot
        plt.close()
    
    return {
        'statusCode': 200,
        'body': {
            'message': 'Stock plots generated successfully.',
            'plot_urls': plot_urls
        }
    }