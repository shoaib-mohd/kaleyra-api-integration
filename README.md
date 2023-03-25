# Kaleyra API Integration



## About

In this project, you can use Kaleyra API's to send sms to anyone easily.

- APIS
    - http://localhost:8000/kaleyra/status/
    - http://localhost:8000/kaleyra/sms/

## Entities

```json
{
    "to": "Phone number(s) to which you want to send the SMS",
    "sender": "Sender ID assigned to your account",
    "type": "type describe the type of sms",
    "body": "Example SMS Send",
    "template_id": "template_id is the id of the template which you set in the kaleyra account"
}
```
