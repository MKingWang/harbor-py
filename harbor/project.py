from harbor.client import HarborClient


class Project(HarborClient):
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
        req = self._post("projects", data)
        if req.status_code == 201:
            return req.json().get("message")
        else:
            return req.json().get("message")
