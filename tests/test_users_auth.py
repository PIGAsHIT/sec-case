import os
import importlib

def setup_module(module):
    # 測試時設定環境變數，確保 app 讀得到
    os.environ["API_TOKEN"] = "test-token"
    # 重新載入 app 模組以套用新環境變數
    global app_module
    app_module = importlib.import_module("app")

def test_users_unauthorized_no_header():
    client = app_module.app.test_client()
    resp = client.get("/users")
    assert resp.status_code == 401

def test_users_unauthorized_wrong_token():
    client = app_module.app.test_client()
    resp = client.get("/users", headers={"Authorization": "Bearer wrong"})
    assert resp.status_code == 401

def test_users_authorized_ok():
    client = app_module.app.test_client()
    resp = client.get("/users", headers={"Authorization": "Bearer test-token"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert data and {"id", "name", "role"}.issubset(data[0].keys())
