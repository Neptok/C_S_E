from mailjet_rest import Client
import authDetail  # To retrieving authentication detail
def sendMail():
    api_key = authDetail.getKey()
    api_secret = authDetail.getSecreat()
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "helloworldearth8@gmail.com",
            "Name": "Hello"
        },
        "To": [
            {
            "Email": "reciever mail",
            "Name": "name"
            }
        ],
        "Subject": "mail subject",
        "TextPart": "mail body",
        # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
        "CustomID": "AppGettingStartedTest"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)

    print(result.json())
