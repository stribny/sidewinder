# Application deployment

If you haven't, make sure to [provision the server](provisioning.md) first.

The server provisioning from the previous step already deployed our first version of the application. However, for future deployments we don't want to run the whole provisioning playbook  (although it should be safe to do so with a small time window when the server won't be available to serve requests). For this purpose there is a separate Make target called `deploy`.

## Deploy command

To deploy a master branch when application has been updated:

```bash
cd deployment/ansible
make deploy
```

!!! warning

    Any content you want to be deployed has to be pushed to the remote Git repository.

### Deploying a specific version

We can identify a specific application version using a git branch (like `master`), git tag (like `v1.0`), commit hash, or any other valid identifier. To deploy such specific application version we can set an environment variable called `APP_VERSION` to such identifier:

```bash
# inside deployment/ansible 
APP_VERSION="v1.0" make deploy
```

### Considerations

Our Ansible playbook will push all new code to the server, run database migrations, and reloads or restarts services (see `deployment/ansible/provision.yml` for details). It is important that the new version of the application is compatible in the database schema and migration files with what is already in the database on the server. That means you shoudn't try to go back to previous versions and only move forward in your migrations.
