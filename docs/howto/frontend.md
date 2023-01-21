# Frontend

## Using Bulma

Sidewinder comes with a simple workflow that allows you to use CSS framework [Bulma](https://bulma.io/) and customize it with [Saas](https://sass-lang.com/). By default, there is already Bulma CSS file ready to be used in the `static` folder (`static/mybulma/mybulma.css`), so when you are just starting out, there is no need to build it first. In this case, you might just start editing the main Sidewinder CSS file in `static/styles.css`.

### Custom Bulma

The simple asset pipeline is an `npm` project found in the `assets` directory, modeled after the article [Creating a custom Bulma build](https://stribny.name/blog/bulma-build/).

1. Modify `assets/mybulma/mybulma.scss` to your needs
2. Run `npm run build-bulma` in the `assets` folder

The command `build-bulma` will build a new custom Bulma and copy it to `static` folder for consumption in Django.

### Don't want to use Bulma for CSS?

In case Bulma is not your thing, go ahead and delete `assets` and `static/mybulma` folders. Also, you will probably want to remove `django-bulma` package from your Python dependencies with `poetry remove django-bulma`.

You will then need to modify and restyle all the Django templates found in the `templates` directory.