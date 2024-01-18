from base.settings import (
    KEYCLOAK_REALM,
    KEYCLOAK_SERVER_URL,
    KEYCLOAK_ADMIN_USERNAME,
    KEYCLOAK_ADMIN_PASSWORD,
)
from keycloak import KeycloakAdmin  # type: ignore
from keycloak.exceptions import KeycloakPostError  # type: ignore
from uuid import UUID


KEYCLOAK_ADMIN = KeycloakAdmin(
    server_url=KEYCLOAK_SERVER_URL,
    username=KEYCLOAK_ADMIN_USERNAME,
    password=KEYCLOAK_ADMIN_PASSWORD,
    realm_name=KEYCLOAK_REALM,
)


def create_keycloak_user(email: str, password: str) -> UUID:
    """
    Create a user in Keycloak and return the UUID of the user.
    Raises ValueError if uuid is not a valid UUID.
    """
    try:
        uuid = KEYCLOAK_ADMIN.create_user(
            {
                "email": email,
                "username": email,
                "enabled": True,
                "credentials": [{"type": "password", "value": password}],
            }
        )
    except KeycloakPostError:
        uuid = KEYCLOAK_ADMIN.get_user_id(email)

    return UUID(uuid)
