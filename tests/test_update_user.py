import allure
import requests

@allure.feature("Test Update Users")
class TestPytestUpdateUser:

  @allure.story("Test update single user")
  @allure.title("Verify test update single user")
  @allure.description("Verify the update single user API response status code and data")
  @allure.severity("critical")
  def test_update_user(self, env_config, env_request_data, env_response_data, cleanup_update_user):
    host = env_config["host"]
    update_api = env_config["updateUser"]
    get_request_data = env_request_data["updateUser"]
    get_response_data = env_response_data["updateUser"]
    header=env_config["headers"]
    response = requests.put(host + update_api, headers=header, json=get_request_data)
    assert response.status_code == 200
    assert get_response_data == response.json()
