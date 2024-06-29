import allure
import requests

@allure.feature("Test Delete Users")
class TestPytestDeleteUser:

  @allure.story("Test delete single user")
  @allure.title("Verify test delete single user")
  @allure.description("Verify the delete single user API response status code and data")
  @allure.severity("critical")
  def test_delete_user(self, setup_delete_user, env_config, env_request_data, env_response_data):
    host = env_config["host"]
    id = setup_delete_user
    delete_api = f"/users/{id}"
    get_request_data = env_request_data["deleteUser"]
    get_response_data = env_response_data["deleteUser"]
    header=env_config["headers"]
    response = requests.delete(host + delete_api, headers=header, json=get_request_data)
    assert response.status_code == 200
    assert response.json() == get_response_data
