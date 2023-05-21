# Frontend

## Basic stylesheets and templates

By default, there is a basic CSS file (`static/css/base.css`) that styles a few existing pages, mainly the `django-allauth` authentication pages.

You can build upon this CSS file or replace it. There is no CSS framework included in Sidewinder.

`django-allauth` templates are provided in the `templates` folder for customization, together with a custom form rendering templates (`templates/forms` via `CustomFormRenderer`) so that checkboxes are rendered with labels displayed after them.

## HTMX

HTMX is loaded in the `_base.html` template together with configured CSRF token (`<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>`).
