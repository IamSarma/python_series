from twilio.rest import Client


# Sending text message
# Get SID and auth_token to create a client object
account_SID = input("Enter SID: ")
auth_token = input("Enter auth token: ")
twilio_cli = Client(account_SID, auth_token)

# Get twilio and user's number
twilio_number = input("Enter twilio number: ")
self_number = input("Enter your number: ")
