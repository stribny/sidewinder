# Creating a new Django app

[Django apps](https://docs.djangoproject.com/en/4.2/ref/applications/) make it possible to separate a Django project
into multiple apps where each app can be dedicated to a different domain or other concern. Sidewinder comes with the `core` 
Django application housing all the basic functionality in the kit but you are not limited to add more apps if you want to.

!!! note

    This step is optional. Feel free to just use the `core` app if you don't want to separate the project into more apps.

## Use Django's startapp command

If you want to add a new app to house your new application domain separated from core, start by creating the app's folder and invoking the standard Django command `startapp`:

```
# inside virtual env in the project's root folder

mkdir <appsfolder>/<newappname>
./manage.py startapp <newappname> <appsfolder>/<newappname>
```

`<appsfolder>` will be either `appname` if you didn't rename anything yet or your new name if you have already renamed the project. It should be the parent directory of the `core` folder (your new app will be a sibling to `core`). 

`<newappname>` is how you want to name the new app.

For example, if you followed the previous instructions to rename the `appname` to `school` and want to create a new app `administration` you would run `./manage.py startapp administration school/administration`.

## Configuration

Additionaly we will need to make some adjustments to make the new app available.

1. In the newly generated `<appsfolder>/<newappname>/apps.py` file change the value of `name` from `<newappname>` to `<appsfolder>.<newappname>`. For example from `administration` to `school.administration`.
2. Include `"<appsfolder>.<newappname>"` in the `INSTALLED_APPS` list in the `<appsfolder>/settings.py`.

Now you should be able to apply the new migrations as usual and use the new app.



