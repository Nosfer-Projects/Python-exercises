import json


def test_get_method_on_site(get_url):
    assert get_url.status_code == 200

def test_delete_method_on_site(del_url):
    assert del_url.status_code == 200

def test_patch_method_on_site(patch_url):
    assert patch_url.status_code == 200

def test_post_method_on_site(post_url):
    assert post_url.status_code == 200

def test_put_method_on_site(put_url):
    assert put_url.status_code == 200

def test_auth_method_on_site(auth_url):
    assert auth_url.status_code == 200

def test_auth_method_on_site_text(auth_url):
    res_text = auth_url.text
    data_json = json.loads(res_text)
    assert data_json["authenticated"] == True

def test_auth_method_on_site_para(auth_url_para):
    expected_status = [200,401]
    assert auth_url_para.status_code in expected_status

def test_auth_method_on_site_bearer(auth_url_bearer):
    assert auth_url_bearer.status_code == 200

def test_auth_method_on_site_digest(auth_url_digest):
    assert auth_url_digest.status_code == 200

def test_auth_method_on_site_digest_algo(auth_url_digest_algo):
    assert auth_url_digest_algo.status_code == 200

def test_auth_method_on_site_digest_algo_stale_after(auth_url_digest_algo_stale_after):
    assert auth_url_digest_algo_stale_after.status_code == 200

def test_auth_method_on_site_hidden_basic_auth(auth_url_hidden_basic):
    assert auth_url_hidden_basic.status_code == 200

def test_status_code(status_code):
    assert status_code.status_code == 500

def test_status_code_wrong_input(status_code_wrong_input):
    assert status_code_wrong_input.status_code == 400

def test_request_inspection_headers_status_code(request_inspection_headers):
    assert request_inspection_headers.status_code == 200

def test_request_inspection_headers(request_inspection_headers):
    data = json.loads(request_inspection_headers.text)
    assert data["headers"]["Host"]== "httpbin.org"

def test_request_inspection_ip_status_code(request_inspection_ip):
    assert request_inspection_ip.status_code == 200

def test_request_inspection_ip(request_inspection_ip):
    data = json.loads(request_inspection_ip.text)
    assert data["origin"] == "31.183.193.42"


def test_request_inspection_ip_headers(request_inspection_ip):
    assert request_inspection_ip.headers["Content-Length"] == "32"

def test_request_user_agent_status_code(request_user_agent):
    assert request_user_agent.status_code == 200

def test_request_user_agent(request_user_agent):
    data = json.loads(request_user_agent.text)
    assert "python-requests" in data["user-agent"], "User-Agent does not contain 'python-requests'"


def test_response_inspection_cache_status_code(response_inspection_cache):
    assert response_inspection_cache.status_code == 200

def test_response_inspection_cache_with_value(response_inspection_cache_with_value):
    assert response_inspection_cache_with_value.status_code == 200

def test_response_inspection_cache_with_wrong_value(response_inspection_cache_with_wrong_value):
    assert response_inspection_cache_with_wrong_value.status_code == 404

def test_response_inspection_etag(response_inspection_etag):
    assert response_inspection_etag.status_code == 200

def test_response_inspection_response_headers_status_code(response_inspection_response_headers):
    assert response_inspection_response_headers.status_code == 200

def test_response_inspection_response_headers_url(response_inspection_response_headers):
    assert response_inspection_response_headers.url == "https://httpbin.org/response-headers?freeform=check"


def test_response_inspection_response_headers_header_content_length(response_inspection_response_headers):
    assert response_inspection_response_headers.headers["Content-Length"] == "92"

def test_response_inspection_response_headers_header_type(response_inspection_response_headers_type):
    assert response_inspection_response_headers_type

def test_response_inspection_post_headers_url(response_inspection_post_headers):
    assert response_inspection_post_headers.url == "https://httpbin.org/response-headers?freeform=post_one"

def test_response_inspection_post_headers(response_inspection_post_headers):
    assert response_inspection_post_headers.headers["freeform"] == "post_one"














