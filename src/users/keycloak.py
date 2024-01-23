from base.settings import (
    KEYCLOAK_REALM,
    KEYCLOAK_SERVER_URL,
    KEYCLOAK_ADMIN_USERNAME,
    KEYCLOAK_ADMIN_PASSWORD,
    KEYCLOAK_CLIENT_ID,
    KEYCLOAK_CLIENT_SECRET,
)
from keycloak import KeycloakAdmin  # type: ignore
from keycloak.exceptions import KeycloakPostError  # type: ignore
from uuid import UUID


def get_keycloak_admin() -> KeycloakAdmin:
    """
    Return a KeycloakAdmin instance.
    """
    return KeycloakAdmin(
        server_url=KEYCLOAK_SERVER_URL,
        username=KEYCLOAK_ADMIN_USERNAME,
        password=KEYCLOAK_ADMIN_PASSWORD,
        realm_name=KEYCLOAK_REALM,
        client_id=KEYCLOAK_CLIENT_ID,
        client_secret_key=KEYCLOAK_CLIENT_SECRET,
    )


def create_keycloak_user(email: str, password: str) -> UUID:
    """
    Create a user in Keycloak and return the UUID of the user.
    Raises ValueError if uuid is not a valid UUID.
    """
    try:
        keycloak_admin = get_keycloak_admin()
        uuid = keycloak_admin.create_user(
            {
                "email": email,
                "username": email,
                "enabled": True,
                "credentials": [{"type": "password", "value": password}],
            }
        )
    except KeycloakPostError:
        uuid = keycloak_admin.get_user_id(email)

    return UUID(uuid)
