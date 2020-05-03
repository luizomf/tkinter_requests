import requests
import json
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes


class RequestsAdapter:
    def __init__(self, url, data, method, content_type, headers, paths):
        self.url = url.strip()
        self.method = method.lower().strip()
        self.content_type = content_type.strip()
        self.headers = headers.strip()
        self.paths = paths
        self.data = data.strip()

        self.response = None
        self._ajust_data()

    def _ajust_data(self):
        if self.data:
            self.data = json.loads(self.data)

        if self.headers:
            self.headers = json.loads(self.headers)

        if not self.url:
            raise ValueError('URL not sent')

        if not self.method:
            raise ValueError('Method not sent')

        if not self.content_type:
            raise ValueError('Select content type')

        if self.content_type == 'multipart/form-data':
            return self._ajust_data_multipart()
        return self._ajust_data_json()

    def _get_request_function(self):
        return getattr(requests, self.method)

    def _ajust_data_multipart(self):
        fields = {**self.data} if self.data else{}
        headers = self.headers if self.headers else {}

        mime = MimeTypes()

        for file_field_name, file_path in self.paths:
            if not file_field_name or not file_path:
                continue

            file_mime, _ = mime.guess_type(file_path)
            fields[file_field_name] = (file_field_name, file_path, file_mime)

        multipart = MultipartEncoder(fields=fields)
        self.headers['Content-Type'] = multipart.content_type
        request_function = self._get_request_function()
        self.response = request_function(
            url=self.url, data=multipart, headers=headers
        )

    def _ajust_data_json(self):
        fields = {**self.data} if self.data else{}
        headers = self.headers if self.headers else {}

        request_function = self._get_request_function()
        self.response = request_function(
            url=self.url, json=fields, headers=headers
        )
