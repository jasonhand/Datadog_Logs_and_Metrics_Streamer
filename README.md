# Datadog Logs and Metrics Streamer

A demonstration application that streams logs and metrics directly to Datadog's API endpoints. This application showcases how to integrate with Datadog's monitoring platform and visualize the data through Datadog dashboards.

## Overview

This application demonstrates how to:

- Stream custom logs directly to Datadog's Log Intake API
- Send custom metrics to Datadog's Metrics API
- Visualize the data in Datadog dashboards

## Setup

1. Create a Datadog account if you don't have one
2. Obtain your Datadog API key from your account settings
3. Configure the application with your API key

## Configuration

### Environment Variables

- `DD_API_KEY`: Your Datadog API key
- `DD_APP_KEY`: Your Datadog APP key

## Running the Application

### Prerequisites
- Python 3.8 or higher
- Datadog account and API key

### Local Development
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables
4. Run the application:
   ```bash
   python app.py
   ```

## Relevant Documentation

- [Datadog API Documentation](https://docs.datadoghq.com/api/latest/)
- [Sending Logs to Datadog](https://docs.datadoghq.com/api/latest/logs/)
- [Submitting Metrics](https://docs.datadoghq.com/api/latest/metrics/)
- [Creating Dashboards](https://docs.datadoghq.com/dashboards/)


