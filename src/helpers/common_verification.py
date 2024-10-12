# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, " Failed Status Code Match"


def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - Key is grater than zero"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non Empty" + key


def verify_response_delete(response):
    assert "Created" in response
