import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
  
    EMAIL_ADDRESS = "tanveerkhan.khan144@gmail.com"
    EMAIL_PASSWORD = "snjr fzgc aiwx qads"

    
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")




send_email(
    "Hello from Python",
    "This is a test email sent from Python!",
    "paras.arora@dotsqures.com"
)




