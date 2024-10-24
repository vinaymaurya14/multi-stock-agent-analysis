# Agent Design: Stock Price Analysis with LLM

## Overview

This agent is designed to analyze stock price trends from plot images using OpenAI's GPT-4 API. It accepts stock plot images, processes them, and returns the top-performing stocks based on trends over the last three months.

## Agent Task Flow

1. **Stock Data Input**:
   - Input data is provided via plot URLs (either a single or multiple images).
   - The agent accepts up to 10 stock plot images as input.

2. **System Prompt and LLM Integration**:
   - The agent uses OpenAI’s GPT-4 model for analyzing stock price trends.
   - A system prompt is used to guide the analysis based on stock plot trends.
   - The LLM identifies the top-performing stocks based on percentage price change.

3. **Interaction with APIs**:
   - **S3**: The stock plot images are stored in an S3 bucket, and URLs are passed to the agent.
   - **API Gateway & Lambda**: API Gateway serves as the interface for user requests, invoking Lambda functions that interact with the LLM.

## Detailed Workflow

1. **Input Handling**:
   - Input: Plot URLs (max 10 URLs).
   - The agent ensures that only up to 10 URLs are processed. Any more than this will result in an error response.

2. **Data Processing and Analysis**:
   - The agent prepares a system prompt and sends it to the LLM.
   - OpenAI analyzes the plot URLs and returns the top 3 performing stocks.

3. **Output**:
   - The output is the names of the top-performing stocks, which is sent back via API response.