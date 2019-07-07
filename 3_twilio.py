# you must this external package : sudo pip install twilio

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8395430cc35c7d7b49d36c285898a25a'
auth_token = '966812f29ee99bdcad11e5b6857b9655'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="The breakfast is wonderfull, thanks.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)