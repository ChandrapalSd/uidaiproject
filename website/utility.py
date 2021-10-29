from .config import twilio_account_sid, twilio_auth_token, twilio_number
from twilio.rest import Client as twilioClient

def sendSMS(mob:str, msg:str):
    mob = '+91'+mob
    client = twilioClient(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        body=msg,
        from_ = twilio_number,
        to = mob
    )
