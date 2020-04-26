from harbor.client import HarborClient


class Project(HarborClient):
    def __init__(self):
        pass

    def create(self, name, public=True, **kwargs):
        # 待优话部分  处理所有的post json数据
        # data = {
        #     "count_limit": 0,
        #     "project_name": "string",
        #     "cve_whitelist": {
        #         "items": [
        #             {
        #                 "cve_id": "string"
        #             }
        #         ],
        #         "project_id": 0,
        #         "id": 0,
        #         "expires_at": 0
        #     },
        #     "storage_limit": 0,
        #     "metadata": {
        #         "enable_content_trust": "string",
        #         "auto_scan": "string",
        #         "severity": "string",
        #         "reuse_sys_cve_whitelist": "string",
        #         "public": "string",
        #         "prevent_vul": "string"
        #     }
        # }
        data = {
            "project_name": name,
            "metadata": {
                "public": str(public)
            }
        }
        resp = self._post("projects", data)
        if resp.status_code == 201:
            return resp.json().get("message")
        else:
            return resp.json().get("message")

    def search(self, name):
        resp = self._search(name)
        projects = resp[0].get("project")
        for project in projects:
            if project.get("name") == name:
                return project

    def isExits(self, name):
        path = "projects?project_name={}".format(name)
        resp = self._head(path)
        if resp.status_code == 200:
            return True
        elif resp.status_code == 404:
            return False
        else:
            return None

    def delete(self, id):
        path = "projects/{}".format(id)
        resp = self._delete(path)
        if resp.status_code == 200:
            return "delete successfully", 200
        else:
            return "delete failed", resp.status_code

    def modify(self, id, name, **kwargs):
        # 这个修改功能有问题，可能是不能修改名称支持能修改其中的配置
        data = {
            "project_name": name,
        }
        path = "projects/{}".format(id)
        resp = self._put(path,data)
        return resp.status_code