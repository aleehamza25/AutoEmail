# 📊 Auto Email Report Sender

This Python script reads a CSV sales report, summarizes the data using `pandas`, and automatically sends a formatted email to a recipient using SMTP or Gmail API.

## 🚀 Features
- Reads `.csv` files
- Summarizes revenue by product
- Sends a custom email with the report
- Can be scheduled for daily reports

## 🛠 Tech Stack
- Python
- pandas
- smtplib / Gmail API

## 📦 How to Run
1. Update `sales_data.csv` with your data
2. Set your Gmail & App Password in the script
3. Run:
```bash
python email_report.py
