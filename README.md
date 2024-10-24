
# **Stock Price Analysis with LLM**

## **Overview**

This project is an AI-driven solution for analyzing stock price trends based on stock plot images using OpenAI's GPT-4. The solution takes in stock data, generates stock price plots, and then analyzes those plots to identify the top-performing stocks over a three-month period.

The system leverages AWS services such as **Lambda**, **API Gateway**, and **S3** for serverless deployment, and uses OpenAI for the stock analysis.

---

## **Features**
- **Stock Plot Generation**: Generates stock price plots from raw stock data (e.g., CSV files).
- **LLM-Driven Analysis**: Uses OpenAI to analyze stock price trends from plot images.
- **Top-Performing Stock Identification**: Returns the top-performing stocks based on price trends.

---

## **Project Structure**

```
stock-analysis-llm-agent/
│
├── lambda_functions/                      # Lambda functions for stock processing
│   ├── plot_stock_data.py                 # Generates stock price plots
│   ├── analyze_stock_plots.py             # Analyzes stock plots via OpenAI
│   ├── analyze_multiple_stock_plots.py    # Analyzes multiple stock plots via OpenAI
│
├── openai_config/                         # OpenAI configuration
│   └── prompts_config.json                # System prompts for OpenAI
│
├── test_cases/                            # Test cases for validating the system
│   ├── test_normal_analysis.py            
│   ├── test_edge_analysis.py              
│   ├── test_normal_multiple_analysis.py   
│   ├── test_edge_multiple_analysis.py     
│
├── engineering_diagram/                   # AWS architecture diagram
│   └── aws_engineering_diagram.png        
│
├── scripts/                               # Performance and reliability scripts
│   ├── measure_latency.py                 
│   ├── test_reliability.py                
│
├── example_inputs/                        # Example input files for testing
│   ├── example_plot_urls.json             
│   ├── example_multiple_plot_urls.json    
│   ├── example_stock_data.csv             
│
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
├── .gitignore                             # Files to be ignored by Git
└── agent_design.md                        # Agent design document
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/stock-analysis-llm-agent.git
cd stock-analysis-llm-agent
```

### **2. Install Dependencies**
Ensure you have all necessary Python dependencies. You can install them by running:
```bash
pip install -r requirements.txt
```

### **3. Set Up AWS Services**
- **S3 Bucket**: Create an S3 bucket to store stock plot images.
- **Lambda Functions**: Deploy the Lambda functions located in the `lambda_functions/` folder using AWS Lambda.
- **API Gateway**: Configure API Gateway to expose the Lambda functions as RESTful APIs.

### **4. Environment Variables**
Ensure the following environment variables are set in your Lambda functions:
- `BUCKET_NAME`: The name of your S3 bucket.
- `OPENAI_API_KEY`: Your OpenAI API key.

---

## **Usage Instructions**

### **Generating Stock Price Plots**

1. Send a **POST** request to the **API Gateway** endpoint with a CSV file of stock data.
2. The Lambda function will generate stock price plots and store them in an S3 bucket.
3. The response will contain URLs of the generated plot images.

Example **CSV Input**:
```csv
StockName,Date,Price
AAPL,2024-01-01,150
AAPL,2024-01-02,155
GOOGL,2024-01-01,2800
GOOGL,2024-01-02,2850
```

Example **API Request**:
```json
POST https://api-gateway-url/plot-stock
{
    "file": "base64-encoded-csv-data"
}
```

Example **API Response**:
```json
{
    "message": "Stock plots generated successfully.",
    "plot_urls": [
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/AAPL.png",
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/GOOGL.png"
    ]
}
```

---

### **Analyzing Stock Price Trends**

1. After generating the stock price plots, send the URLs of these plots to the **analyze_stock_plots** API.
2. The Lambda function will analyze the plots using OpenAI and return the top-performing stocks.

Example **API Request**:
```json
POST https://api-gateway-url/analyze-plots
{
    "plot_urls": [
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/AAPL.png",
        "https://your-bucket-name.s3.amazonaws.com/stock_plots/GOOGL.png"
    ]
}
```

Example **API Response**:
```json
{
    "message": "Top-performing stocks identified successfully.",
    "top_stocks": [
        "AAPL",
        "GOOGL"
    ]
}
```

---

## **Test Cases**

Test cases are available in the `test_cases/` folder. You can run the tests using `pytest`:
```bash
pytest test_cases/
```

- **test_normal_analysis.py**: Tests normal analysis of a stock plot.
- **test_edge_analysis.py**: Tests edge cases (e.g., invalid URLs).
- **test_normal_multiple_analysis.py**: Tests the analysis of multiple stock plots.
- **test_edge_multiple_analysis.py**: Tests edge cases for multiple plot analysis.

---

## **Performance Testing**

- **Latency Testing**: Use `measure_latency.py` to measure the response time of the API.
- **Reliability Testing**: Use `test_reliability.py` to run multiple requests and measure API reliability.

---

## **Engineering Diagram**

Refer to the AWS engineering diagram (`aws_engineering_diagram.png`) for the architecture showing how the system components (Lambda, API Gateway, S3, OpenAI) interact.

---
