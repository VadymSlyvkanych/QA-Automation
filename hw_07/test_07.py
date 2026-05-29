import time

import pytest
import requests


BASE_URL = "http://5.101.50.27:8000"


class EmployeeApi:
    def __init__(self, username, password):
        self.session = requests.Session()
        self.base_url = BASE_URL
        self._login(username, password)

    def _login(self, username, password):
        response = self.session.post(
            f"{self.base_url}/auth/login",
            json={"username": username, "password": password},
        )
        response.raise_for_status()
        data = response.json()
        self.client_token = data["user_token"]

    def create_employee(self, employee_data):
        response = self.session.post(
            f"{self.base_url}/employee/create",
            json=employee_data,
        )
        return response

    def get_employee(self, employee_id):
        response = self.session.get(
            f"{self.base_url}/employee/info/{employee_id}",
        )
        return response

    def update_employee(self, employee_id, data):
        response = self.session.patch(
            f"{self.base_url}/employee/change/{employee_id}",
            params={"client_token": self.client_token},
            json=data,
        )
        return response

    def get_employee_list(self, company_id):
        response = self.session.get(
            f"{self.base_url}/employee/list/{company_id}",
        )
        return response


@pytest.fixture(scope="module")
def api():
    return EmployeeApi("harrypotter", "expelliarmus")


class TestEmployeeApi:
    def test_create_employee(self, api):
        timestamp = str(int(time.time() * 1000))
        data = {
            "first_name": f"John_{timestamp}",
            "last_name": f"Doe_{timestamp}",
            "company_id": 1,
            "phone": "+123456789",
            "is_active": True,
        }
        response = api.create_employee(data)
        assert response.status_code == 200
        result = response.json()
        assert result["first_name"] == data["first_name"]
        assert result["last_name"] == data["last_name"]
        assert result["company_id"] == data["company_id"]
        assert result["is_active"] is True

    def test_get_employee(self, api):
        response = api.get_employee(1)
        assert response.status_code == 200
        result = response.json()
        assert result["company_id"] == 1
        assert "first_name" in result
        assert "last_name" in result

    def test_update_employee(self, api):
        original = api.get_employee(1).json()
        original_email = original.get("email")

        new_email = "updated_ivan@example.com"
        update_response = api.update_employee(1, {"email": new_email})
        assert update_response.status_code == 200
        updated = update_response.json()
        assert updated["email"] == new_email

        api.update_employee(1, {"email": original_email})

    def test_get_employee_list(self, api):
        response = api.get_employee_list(1)
        assert response.status_code == 200
        employees = response.json()
        assert isinstance(employees, list)
        assert len(employees) > 0

    def test_create_employee_full_data(self, api):
        timestamp = str(int(time.time() * 1000))
        data = {
            "first_name": f"Jane_{timestamp}",
            "last_name": f"Smith_{timestamp}",
            "middle_name": "TestMiddle",
            "company_id": 1,
            "email": f"jane_{timestamp}@test.com",
            "phone": "+123456789",
            "birthdate": "1995-05-15",
            "is_active": True,
        }
        response = api.create_employee(data)
        assert response.status_code == 200
        result = response.json()
        assert result["first_name"] == data["first_name"]
        assert result["last_name"] == data["last_name"]
        assert result["middle_name"] == data["middle_name"]
        assert result["email"] == data["email"]
        assert result["phone"] == data["phone"]
        assert result["birthdate"] == data["birthdate"]
        assert result["is_active"] is True

    def test_get_nonexistent_employee(self, api):
        response = api.get_employee(99999)
        assert response.status_code in (404, 500)

    def test_create_employee_missing_required(self, api):
        response = api.create_employee({
            "last_name": "Test",
            "company_id": 1,
        })
        assert response.status_code == 422

    def test_update_employee_invalid_token(self, api):
        response = requests.patch(
            f"{BASE_URL}/employee/change/1",
            params={"client_token": "invalid_token_123"},
            json={"last_name": "ShouldNotWork"},
        )
        assert response.status_code == 401

# uv run pytest hw_07/test_07.py -s --tb=short
