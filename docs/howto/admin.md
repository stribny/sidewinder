# Administration

Create a super user to administer the Django application:

```bash
# inside project root
poetry shell

# inside virtual environment
./manage.py createsuperuser
```

You can then use Django admin at `<site url>/dj-admin/`, in development at `http://localhost:8000/dj-admin/`.