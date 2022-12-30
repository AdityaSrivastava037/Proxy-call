from twilio.rest import Client
import key

Client = Client(key.account_sid, key.auth_token)

message = Client.messages.create(
    body="this is a new message from Code Palace!",
    from_=key.twillio_number,
    to=key.my_phone_number
)

print(message.body)