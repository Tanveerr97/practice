
import smtplib
from email.message import EmailMessage
import psycopg2

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

def fetch_data_directly():
    try:
        # Establish connection to the database
        connection = psycopg2.connect(
            host="localhost",
            database="tanveer",
            user="root",
            password="12345"
        )
        cursor = connection.cursor()
        
        # Query to fetch all data from the table
        cursor.execute("SELECT * FROM Daily_updates")
        rows = cursor.fetchall()

        # Check if there are rows and format the output
        if rows:
            body = "📋 All Daily Updates:\n\n"
            body += f"{'S.No':<6} {'Date':<12} {'Task':<45} {'Status'}\n"
            body += "-" * 80 + "\n"

            # Format each row as a line of text
            for row in rows:
                sno, date, task, status = row
                date_str = str(date)  # Convert date to string
                body += f"{sno:<6} {date_str:<12} {task:<45} {status}\n"
        else:
            body = "No updates found in the Daily_updates table."

        connection.close()
        return body  # Return the formatted body to be used in the email

    except Exception as e:
        print(f"❌ Error: {e}")
        return "Error fetching data from the database."


if __name__ == "__main__":
    updates_body = fetch_data_directly()  # Fetch the data
    send_email(
        subject="📧 All Daily Updates",
        body=updates_body,  # Send the fetched data as the email body
        to_email="tanveerkkhan146@gmail.com"  # Recipient's email
    )
