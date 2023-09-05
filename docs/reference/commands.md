# Commands

## Django

You can display all available commands from all Django apps using `./manage.py`. Refer
to Django and each Django app documentation for more information. 

All commands here should be run inside the Poetry's virtual environment.

Some useful commands:

* `./manage.py runserver` - Starts Django development server
* `./manage.py fresh` - Resets the database and creates a superuser (see `fresh.py`)
* `./manage.py makemigrations` - Generates migrations based on model changes
* `./manage.py migrate` - Runs unapplied migrations (syncs the database schema after generating new migration files)
* `./manage.py sqlmigrate <appname> <migrationfilename>` - Examines a migration file by showing what the generated SQL looks like
* `./manage.py sh` - Starts enhanced Python shell with auto-imported models and Django context (IPython is default in Sidewinder)
* `./manage.py dbshell` - Starts db shell (like PostgreSQL's psql)
* `./manage.py run_huey` - Starts Huey consumers (this way you can test huey consumers using Redis locally)
* `./manage.py print_settings` - Prints all Django settings
* `./manage.py diffsettings` - See all Django settings that differ from Django's defaults
* `./manage.py show_urls` - Shows all urlpatterns
* `./manage.py show_template_tags` - Displays template tags and filters available in the current project
* `./manage.py list_signals` - Prints all defined Django signals
* `./manage.py list_model_info` - Prints all models, their attributes and methods
* `./manage.py notes` - Shows all annotations like TODO, FIXME, BUG, HACK, WARNING, NOTE or XXX in the py and HTML files
* `./manage.py inspectdb` - Generates Django models from the database
* `./manage.py spectacular` - Prints generated OpenAPI schema
* `./manage.py startapp <name> <projectname>/<name>` - Creates a new Django app inside "projectname" folder (what you chose for renaming the project)
* `./manage.py createsuperuser` - Creates a new super user
* `./manage.py changepassword <username>` - Changes a password for a given user
* `./manage.py generate_secret_key` - Generates Django secret key (useful when needing one for production)
* `./manage.py admin_generator <appname>` - Generates the contents of admin.py for a given Django app
* `./manage.py describe_form <appname.ModelName>` - Generates Django form based on a model
* `./manage.py drf_create_token <username>` - Generates an API token for a given user
* `./manage.py makemessages --locale=<locale>` (or `--all`) - Creates or updates messages files for translations
* `./manage.py compilemessages` - Compiles .po files created by makemessages to .mo files
* `./manage.py clear_cache` - Clears Django cache
* `./manage.py clean_pyc` - Removes .pyc files from the project 
* `./manage.py check` - Runs Django check list
* `./manage.py validate_templates` - Validates Django templates
* `./manage.py unreferenced_files` - Lists media files that are not referenced anymore by file fields
* `./manage.py sendtestemail <email@address>` - Sends a test email to the provided email address
* `./manage.py raise_test_exception` - Raises a test exception. Useful for testing error reporters such as Sentry

## Documentation

Feel free to modify Sidewinder's documentation site in the `docs` folder for your needs.

* `mkdocs serve` - Start the live-reloading docs server
* `mkdocs build` - Build the documentation site