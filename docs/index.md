# Sidewinder

<figure markdown>
  ![Sidewinder](sidewinder.png){ width="200" }
  <figcaption></figcaption>
</figure>

**Sidewinder** is an open-source [Django](https://www.djangoproject.com/) starter kit that focuses on good defaults, developer experience, and deployment. Also, [a snake](https://en.wikipedia.org/wiki/Crotalus_cerastes).

You can start a new Django project without worrying about the correct project structure, or what development and testing tools to install and how to configure them. You can also deploy your new project right away with provided Ansible playbook in a few minutes.

## Philosophy

Sidewinder is opinionated to provide smooth experience from starting a new project to deploying it on a single Virtual Private Server (VPS). It is ideal for indie hackers, educators, students and the like.

## Main features

### Configuration

- Good default project structure
- Dependency management with [Poetry](https://python-poetry.org/) that makes it straightforward to manage virtual environments
- Project configuration via environment variables thanks to [django-environ](https://django-environ.readthedocs.io/en/latest/)

### Authentication

- Custom `User` model to allow future extensibility
- Configured [django-allauth](https://github.com/pennersr/django-allauth) for email login and 3rd party authentication
- Stronger password hashing with [argon2-cffi](https://github.com/hynek/argon2-cffi)

### Frontend

- It is expected that you bring your own CSS/CSS framework
- Basic one-file CSS is included to style authentication-related and example pages
- Configured [htmx](https://htmx.org/) for smoother frontend interactions

### HTTP APIs

- [Django REST Framework](https://www.django-rest-framework.org/) for writing REST APIs with configured token authentication
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) for HTTP API documentation
- [drf-standardized-errors](https://drf-standardized-errors.readthedocs.io) for standardized API responses, including configuration for drf-spectacular
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) to allow cross-origin requests (restricted to HTTP API endpoints)

### Task queue

- [huey](https://github.com/coleifer/huey) for executing background and periodic tasks
- [django-huey-monitor](https://github.com/boxine/django-huey-monitor) for monitoring huey task queue in Django admin

### Development Tools

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) for additional Django commands like `shell_plus`
- [django-browser-reload](https://github.com/adamchainz/django-browser-reload) and [pywatchman](https://github.com/facebook/watchman) for auto reloading
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) for debugging
- [django-silk](https://github.com/jazzband/django-silk) for profiling requests and db queries
- [snoop](https://pypi.org/project/snoop/) for ad-hoc debugging
- [Black](https://github.com/psf/black) for automatic code formatting
- [flake8](https://flake8.pycqa.org/en/latest/) linter
- [isort](https://pycqa.github.io/isort/) for sorting imports
- [pre-commit](https://pre-commit.com/) hook configured with Black, Flake8, and isort
- [bandit](https://github.com/PyCQA/bandit) for finding security issues
- Logging with [structlog](https://www.structlog.org/en/stable/) via [django-structlog](https://django-structlog.readthedocs.io/en/latest/)

### Testing

- [pytest](https://docs.pytest.org) test runner via [pytest-django](https://github.com/pytest-dev/pytest-django)
- Useful pytest plugins like `pytest-sugar`, `pytest-icdiff`, `pytest-randomly`, `pytest-xdist`, `pytest-cov`
- [factoryboy](https://factoryboy.readthedocs.io/en/stable/) for defining fixtures
- [Faker](https://faker.readthedocs.io/en/master/) for generating fake data
- [Playwright](https://playwright.dev/) for end-to-end UI testing
- [openapi-spec-validator](https://github.com/p1c2u/openapi-spec-validator) for validating the generated API specs

### Deployment

- Prepared deployment to a single Virtual Private Server (VPS) with reverse proxy and PostgreSQL database
  - [Ansible](https://www.ansible.com/resources/get-started) playbook that deploys the project in one go
  - [Fedora](https://getfedora.org/) as the compatible operating system
  - [PostgreSQL](https://www.postgresql.org/) as the database
  - [Caddy](https://caddyserver.com/) as the reverse proxy server
  - [gunicorn](https://gunicorn.org/) as the WSGI HTTP Server 
  - `systemd` service
