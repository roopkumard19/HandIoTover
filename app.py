from twilio.rest import Client
import flask
from flask_restful import Resource, Api
from twilio.twiml.voice_response import VoiceResponse

app = flask.Flask(__name__)
api = Api(app)

@app.route('/')

def initiate_call():
        account_sid = "AC1a9488ee68428a8b4ce01ab2ce376b02"
        auth_token = "6feeef65f6c56367fe7b5817dd14da17"
        client = Client(account_sid, auth_token)

        call = client.calls\
                .create(to="+16692547860",  # Any phone number
                        from_="+13152281086", # a valid Twilio number
                        url="http://demo.twilio.com/docs/voice.xml")


        return "call connected"

@app.route('/disconnect')

def disconnect_call():
        twiml_response = VoiceResponse()
        twiml_response.say('Hello!')
        twiml_response.hangup()
	
	return "call disconnected"	

	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

