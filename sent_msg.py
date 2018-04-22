#Using Twilio API

from twilio.rest import Client

# MY Account SID from twililo
account_sid = "AC1ef0626a958aa2fde91d95fd493f8f62"
# MY Auth Token from twilio
auth_token  = "aab0cc15f54f3653a59033df5bec3932"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919970919048", 
    from_="+12512208054",
    body="Your Messag eGoes Here")

print(message.sid)
