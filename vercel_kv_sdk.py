import os,json
from typing import Optional

import requests
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class KVConfig(BaseModel):
    url: str
    rest_api_url: str
    rest_api_token: str
    rest_api_read_only_token:str

class Header(BaseModel):
    Authorization:str


options_key_list = ['ex','px',"exat","pxat","keepTtl"]

class KV:
    """
    api document: https://vercel.com/docs/storage/vercel-kv/rest-ap
    """

    def __init__(self, kv_config: Optional[KVConfig] = None):
        if kv_config is None:
            self.kv_config = KVConfig(
                url=os.getenv("KV_URL"),
                rest_api_url=os.getenv("KV_REST_API_URL"),
                rest_api_token=os.getenv("KV_REST_API_TOKEN"),
                rest_api_read_only_token=os.getenv(
                    "KV_REST_API_READ_ONLY_TOKEN"
                ),
            )
        else:
            self.kv_config = kv_config

    def get_kv_conf(self) -> KVConfig:
        return self.kv_config

    def get_header(self) -> Header:
        return {
            'Authorization': f'Bearer {self.kv_config.rest_api_token}',
        }

    def has_auth(self) -> bool:
        resp = requests.get(self.kv_config.rest_api_url, headers=self.get_header())
        return resp.json()['error'] != 'Unauthorized'


    def set(self, key, value,**args) -> bool:
        url = f'{self.kv_config.rest_api_url}'
        data = ['SET',key,value]
        args = {key:args[key] for key in args if key in options_key_list}
        for key in args:
            data.append(key)
            data.append(args[key])
        resp = requests.post(url,data=json.dumps(data), headers=self.get_header())
        return resp.json()['result']

    def get(self, key) -> bool:
        resp = requests.get(f'{self.kv_config.rest_api_url}/get/{key}', headers=self.get_header())
        return resp.json()['result']


    


