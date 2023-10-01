# Import the necessary module from Twilio to send SMS
from twilio.rest import Client

# Twilio Account SID and Authentication Token (replace with your own values)
account_sid = 'ACb2905aed1c7160f472d34979e5bc7cf2'
auth_token = 'b0b477f498d555626b9b03e76869fccc'

# Create a Twilio client object for sending SMS
client = Client(account_sid, auth_token)

# Define a function to send an SMS
def sendSms():
    # Create an SMS message with the given body and recipient numbers
    message = client.messages.create(
        from_='+17697597450',  # Twilio phone number (replace with your own)
        body='Alert',  # SMS message body
        to='+919101801683'  # Recipient's phone number (replace with the desired recipient)
    )

    # Print the SID of the sent message for reference
    print(message.sid)
