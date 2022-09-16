from twilio.rest import Client


# Sending text message
# Get SID and auth_token to create a client object
account_SID = input("Enter SID: ")
auth_token = input("Enter auth token: ")
twilio_cli = Client(account_SID, auth_token)

# Get twilio and user's number
twilio_number = input("Enter twilio number: ")
self_number = input("Enter your number: ")

# Get message body and send
message_body = input("Enter message body: ")
user_message = twilio_cli.messages.create(
    body=message_body, from_=twilio_number, to=self_number)
