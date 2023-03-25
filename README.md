# Kaleyra API Integration


## About

In this project, you can use Kaleyra API's to send sms to anyone easily.

- APIS
    - http://localhost:5000/kaleyra/status/
    - http://localhost:5000/kaleyra/sms/

## Paylod

```json
{
    "to": "Phone number(s) to which you want to send the SMS",
    "sender": "Sender ID assigned to your account",
    "type": "type describe the type of sms",
    "body": "Example SMS Send",
    "template_id": "template_id is the id of the template which you set in the kaleyra account"
}
```

### Project Start Guide:

- First of all, clone the project
- Install the dependencies by using ""pip install -r requirements.txt" command
- "python project/app.py" command to start the project
- Then you can use the project api's and integrate in your project as well.
