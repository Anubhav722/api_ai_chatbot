import json
import apiai
CLIENT_ACCESS_TOKEN = 'e7a52c6d3df0440fa55fb9e0768056c3'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
print("To end the conversation enter 'q' or 'Q'")
def main():
    while True:

	request = ai.text_request()
	request.lang = 'en'
	request.query = raw_input('Chat with me: ')
	if not request.query is 'q' and not request.query is 'Q':
	    response = request.getresponse()
	    responsestr = response.read().decode('utf-8')
	    response_obj = json.loads(responsestr)

	    print(response_obj["result"]["fulfillment"]["speech"])

	if request.query is 'q' or request.query is 'Q':
	    print("Have a nice day.!")
	    break

if __name__ == '__main__':
    main()
