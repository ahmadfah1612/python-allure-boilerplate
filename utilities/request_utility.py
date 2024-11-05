import json
import requests
import allure
from config.config import Config


class RequestUtility:
    @staticmethod
    def make_request(method, endpoint, payload=None):
        url = f"{Config.BASE_URL}{endpoint}"

        with allure.step(f"Making {method} request to {url}"):
            allure.attach(
                json.dumps(payload, indent=2) if payload else "No payload",
                name="Request Payload",
                attachment_type=allure.attachment_type.JSON
            )

            response = requests.request(
                method=method,
                url=url,
                json=payload,
                headers=Config.HEADERS
            )

            allure.attach(
                json.dumps(response.json(), indent=2),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON
            )

            return response

