import requests
import json


class HarborClient:
    url = ""
    http = None

    def __init__(self, username, password, url):
        HarborClient.url = url
        HarborClient.http = requests.session()
        HarborClient.http.headers = {"accept": "application/json", "Content-Type": "application/json"}
        HarborClient.http.auth = (username, password)

    def _format_params(self, **kwargs):
        params = {}
        if len(kwargs) != 0:
            for k in kwargs:
                params.update(k=kwargs[k])
        return params

    def _get(self, path, **kwargs):
        params = self._format_params(**kwargs)
        url = "{}/api/{}".format(HarborClient.url, path)
        resp = HarborClient.http.get(url, params=params)
        if resp.status_code == 200:
            return resp.json(), resp.status_code
        else:
            return None, resp.status_code

    def _post(self, path, data=None):
        url = "{}/api/{}".format(HarborClient.url, path)
        d = json.dumps(data)
        resp = HarborClient.http.post(url, data=d)
        return resp

    def _head(self, path):
        url = "{}/api/{}".format(self.url, path)
        resp = HarborClient.http.head(url)
        return resp

    def _delete(self, path):
        url = "{}/api/{}".format(self.url, path)
        HarborClient.http.cookies.clear()
        resp = HarborClient.http.delete(url)
        return resp

    def _put(self, path, data):
        url = "{}/api/{}".format(self.url, path)
        HarborClient.http.cookies.clear()
        d = json.dumps(data)
        resp = HarborClient.http.put(url, data=d)
        return resp

    def _search(self, name):
        path = "search?q={}".format(name)
        return self._get(path)
