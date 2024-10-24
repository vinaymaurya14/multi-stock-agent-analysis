import openai
import json
import os

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

def analyze_multiple_stock_plots(event, context):
    # Extract plot URLs from the input event
    plot_urls = event['plot_urls']
    
    # Ensure that the number of plot URLs does not exceed 10
    if len(plot_urls) > 10:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'You can only submit up to 10 plot URLs.'
            })
        }
    
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

    # Extract the names of the best performing stocks from the response
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
    Extracts the top performing stocks from the OpenAI response text.
    Adjust this based on the response format from OpenAI.
    """
    if "Top stocks:" in analysis_result:
        stocks = analysis_result.split("Top stocks:")[1].strip()
        return stocks.split(",")[:3]  # Return top 3 stocks
    return []