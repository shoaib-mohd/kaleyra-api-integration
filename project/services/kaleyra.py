# -*- coding: utf-8 -*-
import json

import requests
from settings.logging import logger


class kaleyra:

    def send(self, req):
        '''
        {
            "to": 91XXXXXXXXXX,
            "sender": "SHOW",
            "type": "TXN",
            "body": "Example SMS Send",
            "template_id": " "

            # find template: https://messaging.kaleyra.com/support/solutions/articles/3000092892-how-do-i-create-a-template-
        }
        '''

        data = json.loads(req)

        if not data.get("to") or len(str(data.get("to"))) != 12:
            return {"message": "Mobile Number is not available or invalid"}, 400
        if not data.get("sender"):
            return {"message": "sender is not available"}, 400
        if not data.get("type"):
            return {"message": "type is not available"}, 400
        if not data.get("body"):
            return {"message": "email body is not available"}, 400
        if not data.get("template_id"):
            return {"message": "template_id is not available"}, 400

        sid = " "
        api_key = " "

        # For more information:- https://developers.kaleyra.io/docs/view-api-key-and-sid

        headers = {
            "api-key": api_key,
            "Content-Type": "application/json",
        }
        url = f"https://api.in.kaleyra.io/v1/{sid}/messages"
        response = requests.post(
            url=url, json=data, headers=headers, timeout=30)

        logger.info(
            "SMS Send by Kaleyra url: %s headers: %s payload: %s status code: %s response: %s",
            url,
            headers,
            data,
            response.status_code,
            response.text,
        )

        if response.status_code == 202:
            res = json.loads(response.text)
            return {
                "message_id": res.get("data")[0].get("message_id"),
                "status_code": response.status_code,
            }
        return {"message": response.text, "status_code": response.status_code}
