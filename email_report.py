import pandas as pd
import smtplib
from email.message import EmailMessage

# Load CSV
df = pd.read_csv("sales_data.csv")
summary = df.groupby("Product")["Revenue"].sum()

# Email setup
msg = EmailMessage()
msg["Subject"] = "Daily Sales Report"
msg["From"] = "you@gmail.com"
msg["To"] = "manager@example.com"
msg.set_content(f"Here’s your report:\n\n{summary.to_string()}")

# Send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("you@gmail.com", "app-password")
    smtp.send_message(msg)
