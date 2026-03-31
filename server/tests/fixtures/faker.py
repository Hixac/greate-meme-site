import pytest
from faker import Faker


faker = Faker()


@pytest.fixture
def sample_user_data() -> dict[str, str]:
    return {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password()
    }
