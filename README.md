# Testing Django with Keycloak

This is a simple Django REST API that uses Keycloak for authentication.

### Launching Keycloak

I'm running the Keycloak server with the following command
(from [the Keycloak docs](https://www.keycloak.org/getting-started/getting-started-docker)):

```
docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:23.0.4 start-dev
```

This launches Keycloak at http://localhost:8080, with the admin user being `admin` and the password being `admin`.

### Configuring the Keycloak Client

Here's how I configured the `admin-cli` client. Should work as well with new clients.

- In the "Settings" tab:
    - Activate "Client Authentication" (in previous versions, set "Access Type" to "confidential")
    - Activate "Service Accounts Roles" (in previous versions, "Service Accounts Enabled")
    - Activate "Standard Flow" (in previous versions, "Standard Flow Enabled")
- In the "Credentials" tab:
    - Make sure "Client Authenticator" is set to "Client Id and Secret"
    - Copy the "Secret" value to a `.env` file in the root of this project, as `KEYCLOAK_CLIENT_SECRET=<secret>`
- In the "Service account roles" tab:
    - Click "Assign role" and select the "admin" role
- In the "Advanced" tab:
    - Set "User Info Signed Response Algorithm" to "RS256"

### Running the Django REST API

**Requirements**:

- Python 3.12 installed via Pyenv
- Poetry installed via Pipx
- For a detailed guide, you can follow [this article](https://blog.marcosalonso.dev/perfect-python-environment/)

Follow the provided `.env.example` file to define (at least) the following environment variables
in a `.env` file in the root of this project:

```
DJANGO_SUPERUSER_EMAIL=<email>
DJANGO_SUPERUSER_PASSWORD=<password>

KEYCLOAK_CLIENT_SECRET=<secret>
```

You can now then use the provided Makefile to run the app:

```
make install   # configure Poetry and install dependencies
make reset     # reset the database and create a new admin user
make run       # run the app
```
