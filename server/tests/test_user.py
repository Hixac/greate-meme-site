import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
class TestUserCreate:
    async def test_user_create_201(
        self,
        client: AsyncClient,
        sample_user_data: dict[str, str]
    ) -> None:
        response = await client.post(
            "/api/v1/user/",
            json=sample_user_data
        )
        assert response.status_code == 201

    async def test_user_create_409(
        self,
        client: AsyncClient,
        sample_user_data: dict[str, str]
    ) -> None:
        response = await client.post(
            "/api/v1/user/",
            json=sample_user_data
        )
        assert response.status_code == 201

        response = await client.post(
            "/api/v1/user/",
            json=sample_user_data
        )
        assert response.status_code == 409
