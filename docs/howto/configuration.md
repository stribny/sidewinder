# Configuration

Sidewinder is completely configured via environment variables with the help of [django-environ](https://django-environ.readthedocs.io/en/latest/).

Start by creating `.env` file with your local settings in the project's root directory. You can begin by copying `.env-example`.

## .env file config

### Secret key

In production, make sure to set a unique secret key (doesn't matter for development):

```ini
DJANGO_SECRET_KEY=secretkey
```

### Debug mode

```ini
DJANGO_DEBUG=1
DJANGO_DEBUG_TOOLBAR=1
```

Set to `0` to disable debug mode.

### Allowed hosts

```ini
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Add additional hosts as needed in production.

### SSL

```ini
DJANGO_SSL=0
```

Set to `1` in production to configure https.

### Emails

Replace values according to your email server:

```ini
DJANGO_SERVER_EMAIL=sidewinder@example.com
DJANGO_EMAIL_HOST=example.emailprovider.com
DJANGO_EMAIL_PORT=587
DJANGO_EMAIL_HOST_USER=
DJANGO_EMAIL_HOST_PASSWORD=
```

Replace to set default email prefix and origin address:

```ini
DJANGO_DEFAULT_FROM_EMAIL=sidewinder@example.com
ALLAUTH_ACCOUNT_EMAIL_SUBJECT_PREFIX=
```

### Database

Set a connection string to SQLite or PostgreSQL database:

```ini
DJ_DATABASE_CONN_STRING=
```

Alternatively, create a `sidewinder` PostgreSQL database on the port `5432` with `postgres` user and `postgres` password, and make sure that the database is available for connections. Then use this example connection string:

```
DJ_DATABASE_CONN_STRING=postgres://postgres:postgres@localhost:5432/sidewinder
```

### Complete configuration

```ini
DJANGO_SECRET_KEY=secretkey
DJANGO_DEBUG=1
DJANGO_DEBUG_TOOLBAR=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SSL=0
DJANGO_SERVER_EMAIL=sidewinder@example.com
DJANGO_EMAIL_HOST=example.emailprovider.com
DJANGO_EMAIL_PORT=587
DJANGO_EMAIL_HOST_USER=
DJANGO_EMAIL_HOST_PASSWORD=
DJANGO_DEFAULT_FROM_EMAIL=sidewinder@example.com
ALLAUTH_ACCOUNT_EMAIL_SUBJECT_PREFIX=
DJ_DATABASE_CONN_STRING=postgres://postgres:postgres@localhost:5432/sidewinder
```

## Rename app folder

The main application folder is called `appname`. To rename it, you will also need to find and replace references to `appname` in the repository.

## Verify that everything works

You can verify the configuration by [running the project](run.md).

