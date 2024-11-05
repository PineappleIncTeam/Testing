import json
import allure
import requests
from jsonschema import validate
from base.helper import attach_request, attach_response, get_content_by_type


class BaseResponseModel:
    def __init__(self, status: int, data=None, headers: dict = None, formatted_response: str = None):
        self.status = status
        self.data = data
        self.headers = headers
        self.formatted_response = formatted_response


class BaseClient:
    def __init__(self, base_url: str, **kwargs):
        self.base_url = base_url
        self.kwargs = kwargs

    def custom_request(self, method: str = "POST", rout: str = "", schema: dict = None, **kwargs) -> BaseResponseModel:
        url = f"{self.base_url}{rout}"
        with allure.step(f"{method} {url}"):
            attach_request(method, url, kwargs.get('data', None), kwargs.get('json', None))
            response = requests.request(method, url, verify=False, **kwargs)

            content_type = response.headers.get('Content-Type')
            content_data, attach_type = get_content_by_type(content_type, response)
            formatted_response = json.dumps(content_data, indent=4, ensure_ascii=False)

            attach_response(content_data, response.status_code, response.headers, attach_type)

            if schema:
                validate(instance=content_data, schema=schema)

            return BaseResponseModel(status=response.status_code, data=content_data, headers=response.headers,
                                     formatted_response=formatted_response)

    def post(self, rout: str = "", data: dict = None, json: dict = None, schema: dict = None,
             files: dict = None, cookies: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("POST", rout, schema, data=data, json=json, files=files, cookies=cookies,
                                   **kwargs)

    def get(self, rout: str = "", schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("GET", rout, schema, **kwargs)

    def put(self, rout: str = "", data: dict = None, schema: dict = None, json: dict = None,
            **kwargs) -> BaseResponseModel:
        return self.custom_request("PUT", rout, schema, data=data, json=json, **kwargs)

    def delete(self, rout: str = "", schema: dict = None, json: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("DELETE", rout, schema, json=json, **kwargs)

    def patch(self, rout: str = "", data: dict = None, json: dict = None, schema: dict = None,
              **kwargs) -> BaseResponseModel:
        return self.custom_request("PATCH", rout, schema, data=data, json=json, **kwargs)

    def head(self, rout: str = "", schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("HEAD", rout, schema, **kwargs)
