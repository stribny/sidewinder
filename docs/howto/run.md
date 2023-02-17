# Start Sidewinder

You can run the development server inside the Poetry's virtual environment. If this is the first time, don't forget to run Django's `migrate` management command before that.

```bash
# inside project root
poetry shell

# inside virtual environment
./manage.py migrate # first time
./manage.py runserver
```
