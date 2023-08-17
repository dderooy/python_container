import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import sys
import traceback


class CustomHTTPAdapter(HTTPAdapter):
    """
        Class is used to set timeouts and retry conditions for all requests
    """
    def __init__(self, *args, **kwargs):
        self.timeout = 15 #timeout in seconds
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)
        retry_strategy = Retry(
            total=2, #retry amount
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504, 409, 408],
            allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "POST"]
        )
        self.max_retries = Retry.from_int(retry_strategy)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)
    
session = requests.Session()
adapter = CustomHTTPAdapter()
assert_status_hook = lambda response, *args, **kwargs: response.raise_for_status()
session.mount("https://", adapter)
session.hooks["response"] = [assert_status_hook]
session.headers = {"Accept": "application/json", "Content-Type": "application/json"}

def main():

    try:

        print("hello world!")
        #TODO: script here 

    except Exception as e:
        traceback.print_exc()
        exc_type, exc_obj, exc_tb = sys.exc_info()
        msg = f"ERROR! type: {exc_type}, line: {exc_tb.tb_lineno}, msg: {e}"
        print(msg)
    

if __name__ == "__main__":
    main()
