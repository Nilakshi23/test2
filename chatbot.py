from json import dumps
import sys
from httplib2 import Http

JOB_NAME=sys.argv[1]
BUILD_NUMBER=sys.argv[3]
BUILD_USER = sys.argv[2]
BUILD_URL = sys.argv[4]
BUILD_STATUS = sys.argv[5]
SonarQubeQualityGateStatus = sys.argv[6]
Dashboard = sys.argv[7]
CHATBOT = sys.argv[8]

def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'CHATBOT'
    bot_message = {
        'text' : f"Job Name: {JOB_NAME}\nStarted by User: {BUILD_USER} \nBuild Number: {BUILD_NUMBER}\nBuild URL :  {BUILD_URL}\nStatus: {BUILD_STATUS}\nQuality Gate Status: {SonarQubeQualityGateStatus}\nSonar Project URL : {Dashboard}" 
		}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
