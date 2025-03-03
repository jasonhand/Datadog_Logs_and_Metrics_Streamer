# Datadog Logs and Metrics Streamer

![image](https://github.com/user-attachments/assets/337c96d0-0e6b-4e29-847b-edbf78add477)

A demonstration application that streams logs and metrics directly to Datadog's API endpoints. This application showcases how to integrate with Datadog's monitoring platform and visualize the data through Datadog dashboards.

## Dashboard Example

![image](https://github.com/user-attachments/assets/561d941c-a705-4add-9c31-5c0b87c7eced)

## Overview

This application was created with the assistance of Claude Sonnet 3.7 through the agent built into the new Windows version of the Warp terminal. While testing the Warp terminal, I asked it to help me create a simple application that would stream logs and metrics directly to Datadog's API endpoints. This is the result

This application demonstrates how to:

- Stream custom logs directly to Datadog's Log Intake API
- Send custom metrics to Datadog's Metrics API
- Visualize the data in Datadog dashboards

## Setup

1. Create a Datadog account if you don't have one
2. Obtain your Datadog API key and APP key from your account settings
3. Configure the application with your API key and APP key

## Configuration

### Environment Variables

- `DD_API_KEY`: Your Datadog API key
- `DD_APP_KEY`: Your Datadog APP key

## Running the Application

### Prerequisites
- Python 3.8 or higher
- Datadog account and API key (create a .env file and add your API key and APP key)

### Run the application locally

- Create a .env file and add your API key and APP key. Save in the root directory of the project.
- Run the application from your terminal:
   ```bash
   python app.py
   ```

## Relevant Documentation

- [Datadog API Documentation](https://docs.datadoghq.com/api/latest/)
- [Sending Logs to Datadog](https://docs.datadoghq.com/api/latest/logs/)
- [Submitting Metrics](https://docs.datadoghq.com/api/latest/metrics/)
- [Creating Dashboards](https://docs.datadoghq.com/dashboards/)


