import openai
import json
import os

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

def analyze_stock_plots(event, context):
    # Extract plot URLs from the input event
    plot_urls = event['plot_urls']
    
    # Prepare the prompt to send to OpenAI API
    prompt = "Analyze the stock price trends from the following plot URLs: "
    for url in plot_urls:
        prompt += f"{url} "

    # Make a request to OpenAI API to analyze the plots
    response = openai.Completion.create(
        model="gpt-4",  # Use GPT-4 for enhanced analysis
        prompt=prompt,
        max_tokens=100,
        temperature=0.5
    )

    # Extract the names of the top 3 performing stocks from the response
    analysis_result = response['choices'][0]['text']
    top_stocks = extract_top_stocks(analysis_result)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Top-performing stocks identified successfully.',
            'top_stocks': top_stocks
        })
    }

def extract_top_stocks(analysis_result):
    """
    Extracts the top 3 performing stocks from the OpenAI response text.
    This is a simplified example and may require adjustments based on the response format.
    """
    # Example: Assuming the response contains stock names in the format "Top stocks: AAPL, GOOGL, TSLA"
    if "Top stocks:" in analysis_result:
        stocks = analysis_result.split("Top stocks:")[1].strip()
        return stocks.split(",")[:3]  # Return top 3 stocks
    return []