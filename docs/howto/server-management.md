# Server management

There are some neat commands in the provided `deployment/ansible/Makefile` that you can run to help you manage your new server:

!!! warning

    Make sure you configured everything first (see [server provisioning](provisioning.md)).

- `make provision` - Provisions a VPS from scratch (use `APP_VERSION` env var for a specific version)
- `make deploy` - Deploys a new application version (use `APP_VERSION` env var for a specific version)
- `make login` - Gives you a remote SSH shell to your server
- `make status` - Gives you status of all important services running (application, database, Redis, queue, webserver)
- `make appservicelog` - Prints the last application service logs
- `make queueservicelog`- Prints the last queue service logs
- `make webserverservicelog`- Prints the last web server service logs
- `make webserveraccesslog` - Prints the last web server access logs
- `make monitor` - Starts a system monitor on the server (to check on system usage like memory, disk, CPU, etc.)
- `make createsuperuser` - Creates a superuser on the server
- `make upgrade` - Updates all operating system packages and restarts the server
