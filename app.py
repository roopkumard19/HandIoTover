from twilio.rest import Client
import flask
from flask_restful import Resource, Api


app = flask.Flask(__name__)
api = Api(app)

@app.route('/')

def initiate_call():
	account_sid = "AC233559065bfe688e5119167aa22b7e68"
	auth_token = "9aaea5a1e242c18d67a6fb045311bf4f"
	client = Client(account_sid, auth_token)

	call = client.calls\
      		.create(to="+16692547860",  # Any phone number
              		from_="+15005550006")# a valid Twilio number)
              		#url="http://demo.twilio.com/docs/voice.xml"
			

	return str(call.sid)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

