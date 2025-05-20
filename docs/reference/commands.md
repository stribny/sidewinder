# Commands

## Django

You can display all available commands from all Django apps using `uv run -- manage.py`. Refer
to Django and each Django app documentation for more information.

Some useful commands:

* `uv run -- manage.py runserver` - Starts Django development server
* `uv run -- manage.py fresh` - Resets the database and creates a superuser (see `fresh.py`)
* `uv run -- manage.py makemigrations` - Generates migrations based on model changes
* `uv run -- manage.py migrate` - Runs unapplied migrations (syncs the database schema after generating new migration files)
* `uv run -- manage.py sqlmigrate <appname> <migrationfilename>` - Examines a migration file by showing what the generated SQL looks like
* `uv run -- manage.py sh` - Starts enhanced Python shell with auto-imported models and Django context (IPython is default in Sidewinder)
* `uv run -- manage.py dbshell` - Starts db shell (like PostgreSQL's psql)
* `uv run -- manage.py run_huey` - Starts Huey consumers (this way you can test huey consumers using Redis locally)
* `uv run -- manage.py print_settings` - Prints all Django settings
* `uv run -- manage.py diffsettings` - See all Django settings that differ from Django's defaults
* `uv run -- manage.py show_urls` - Shows all urlpatterns
* `uv run -- manage.py show_template_tags` - Displays template tags and filters available in the current project
* `uv run -- manage.py list_signals` - Prints all defined Django signals
* `uv run -- manage.py list_model_info` - Prints all models, their attributes and methods
* `uv run -- manage.py notes` - Shows all annotations like TODO, FIXME, BUG, HACK, WARNING, NOTE or XXX in the py and HTML files
* `uv run -- manage.py inspectdb` - Generates Django models from the database
* `uv run -- manage.py spectacular` - Prints generated OpenAPI schema
* `uv run -- manage.py startapp <name> <projectname>/<name>` - Creates a new Django app inside "projectname" folder (what you chose for renaming the project)
* `uv run -- manage.py createsuperuser` - Creates a new super user
* `uv run -- manage.py changepassword <username>` - Changes a password for a given user
* `uv run -- manage.py generate_secret_key` - Generates Django secret key (useful when needing one for production)
* `uv run -- manage.py admin_generator <appname>` - Generates the contents of admin.py for a given Django app
* `uv run -- manage.py describe_form <appname.ModelName>` - Generates Django form based on a model
* `uv run -- manage.py drf_create_token <username>` - Generates an API token for a given user
* `uv run -- manage.py makemessages --locale=<locale>` (or `--all`) - Creates or updates messages files for translations
* `uv run -- manage.py compilemessages` - Compiles .po files created by makemessages to .mo files
* `uv run -- manage.py clear_cache` - Clears Django cache
* `uv run -- manage.py clean_pyc` - Removes .pyc files from the project
* `uv run -- manage.py check` - Runs Django check list
* `uv run -- manage.py validate_templates` - Validates Django templates
* `uv run -- manage.py unreferenced_files` - Lists media files that are not referenced anymore by file fields
* `uv run -- manage.py sendtestemail <email@address>` - Sends a test email to the provided email address
* `uv run -- manage.py raise_test_exception` - Raises a test exception. Useful for testing error reporters such as Sentry

## Documentation

Feel free to modify Sidewinder's documentation site in the `docs` folder for your needs.

* `uv run -- mkdocs serve` - Start the live-reloading docs server
* `uv run -- mkdocs build` - Build the documentation site
