'''
Utility functions for the FreshFarmers application.
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from geopy.distance import geodesic
def send_email(to, subject, body):
    '''
    Sends an email to the specified recipient.
    '''
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, to, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
def send_sms(to, message):
    '''
    Sends an SMS to the specified recipient.
    '''
    # This is a placeholder implementation. You would need to integrate with an SMS gateway API.
    print(f"Sending SMS to {to}: {message}")
def calculate_distance(coord1, coord2):
    '''
    Calculates the distance between two geographical coordinates.
    '''
    return geodesic(coord1, coord2).km