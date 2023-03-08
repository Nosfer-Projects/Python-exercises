# all features
import requests
import pytest
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests.structures import CaseInsensitiveDict

@pytest.fixture
def get_url():
    response = requests.get("https://httpbin.org/get")
    return response

@pytest.fixture
def del_url():
    response = requests.delete("https://httpbin.org/delete")
    return response

@pytest.fixture
def patch_url():
    response = requests.patch("https://httpbin.org/patch")
    return response


@pytest.fixture
def post_url():
    response = requests.post("https://httpbin.org/post")
    return response

@pytest.fixture
def put_url():
    response = requests.put("https://httpbin.org/put")
    return response

@pytest.fixture
def auth_url():
    basic = HTTPBasicAuth("user", "password")
    response = requests.get("https://httpbin.org/basic-auth/user/password", auth=basic)
    return response

@pytest.fixture(params=[("user", "passwd"), ("x", "a")])
def auth_url_para(request):
    user, password = request.param
    response = requests.get(f"https://httpbin.org/basic-auth/{user}/{password}", auth=(user, password))
    yield response


@pytest.fixture
def auth_url_bearer():
    headers = {"Authorization": "Bearer token"}
    response = requests.get("https://httpbin.org/bearer", headers=headers)
    return response

@pytest.fixture
def auth_url_digest():
    user = "user1"
    password = "passwd"
    qop = "auth"
    url = f"https://httpbin.org/digest-auth/{qop}/{user}/{password}"
    response = requests.get(url, auth=HTTPDigestAuth(user, password))

    return response

@pytest.fixture
def auth_url_digest_algo():
    user = "user"
    password = "pass"
    qop = "auth"
    algo= "MD5"
    url = f"https://httpbin.org/digest-auth/{qop}/{user}/{password}/{algo}"
    response = requests.get(url, auth=HTTPDigestAuth("user","pass"))
    return response


@pytest.fixture
def auth_url_digest_algo_stale_after():
    user = "user"
    password = "pass"
    qop = "auth"
    algo= "MD5"
    stale_after = "never"
    url = f"https://httpbin.org/digest-auth/{qop}/{user}/{password}/{algo}/{stale_after}"
    response = requests.get(url, auth=HTTPDigestAuth("user", "pass"))
    return response


@pytest.fixture
def auth_url_hidden_basic():
    user = "user"
    password = "pass"
    url = f"https://httpbin.org/hidden-basic-auth/{user}/{password}"
    response = requests.get(url, auth=HTTPBasicAuth("user", "pass"))
    return response

@pytest.fixture
def status_code():
    codes = 500
    url = f"https://httpbin.org/status/{codes}"
    response = requests.delete(url)
    return response


@pytest.fixture
def status_code_wrong_input():
    codes = "kkk"
    url = f"https://httpbin.org/status/{codes}"
    response = requests.delete(url)
    return response

@pytest.fixture
def request_inspection_headers():
    response = requests.get("https://httpbin.org/headers")
    return response

@pytest.fixture
def request_inspection_ip():
    response = requests.get("https://httpbin.org/ip")
    return response


@pytest.fixture
def request_user_agent():
    response = requests.get("https://httpbin.org/user-agent")
    return response

@pytest.fixture
def response_inspection_cache():
    response = requests.get("https://httpbin.org//cache")
    return response


@pytest.fixture
def response_inspection_cache_with_value():
    value = 100
    response = requests.get(f"https://httpbin.org//cache/{value}")
    return response

@pytest.fixture
def response_inspection_cache_with_wrong_value():
    value = "kkk"
    response = requests.get(f"https://httpbin.org//cache/{value}")
    return response

@pytest.fixture
def response_inspection_etag():
    etag = "test"
    response = requests.get(f"https://httpbin.org/etag/{etag}")
    return response

@pytest.fixture
def response_inspection_response_headers():
    response = requests.get(f"https://httpbin.org/response-headers", params="freeform=check")
    return response

@pytest.fixture
def response_inspection_response_headers_type():
    response = requests.get(f"https://httpbin.org/response-headers", params="freeform=check")
    return isinstance(response.headers, CaseInsensitiveDict)

@pytest.fixture
def response_inspection_post_headers():
    response = requests.post(f"https://httpbin.org/response-headers", params="freeform=post_one")
    return response
