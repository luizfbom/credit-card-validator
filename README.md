# Azure Credit Card Document Validator

## Overview
This project is a Streamlit web application that validates credit card images using Azure Document Intelligence service. The application allows users to upload images of credit cards, check if its a valid credit card image and processes them to extract credit card information, and displays the validation results.

## Features
- Image upload functionality (supports PNG, JPG, JPEG)
- Azure Blob Storage integration for file storage
- Credit card information detection and validation
- Real-time feedback on credit card validity
- Display of extracted credit card details including:
  - Card holder name
  - Card number
  - Expiration date
  - Issuing bank
  - Payment network

## Prerequisites
- Python 3.x
- Azure account with:
  - Blob Storage service
  - Document Intelligence API
- Required Python packages:
  ```
  streamlit
  azure-storage-blob
  azure-ai-documentintelligence
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Azure credentials:
   - Set up your Azure storage account
   - Configure your Azure Document Intelligence service
   - Update environment variables or configuration files with your Azure credentials

## Usage
1. Start the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Use the file uploader to select and upload a credit card image

4. View the validation results and extracted information

## Project Structure 