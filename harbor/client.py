import requests
import json


class HarborClient():
    def __init__(self, username, password, url):
        self.url = url
        self.http = requests.session()
        self.http.headers = {"accept": "application/json", "Content-Type": "application/json"}
        self.http.auth = (username, password)

    def _format_params(self, **kwargs):
        params = {}
        if len(kwargs) != 0:
            for k in kwargs:
                params.update(k=kwargs[k])
        return params

    def _get(self, path, **kwargs):
        params = self._format_params(**kwargs)
        url = "{}/api/{}".format(self.url, path)
        req = self.http.get(url, params=params)
        if req.status_code == 200:
            return req.json(), req.status_code
        else:
            req_msg = req.json()
            return None, req.status_code

    def _post(self, path, data=None):
        # params = self._format_params(**kwargs)
        url = "{}/api/{}".format(self.url, path)
        d = json.dumps(data)
        req = self.http.post(url, data=d)
        return req

    def health(self):
        req, status = self._get("health")
        return req, status

    def search(self, project):
        req, status = self._get("search", q=project)
        return req, status


