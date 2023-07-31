# Server provisioning

This page explains how to get a virtual private server, configure it, and make your first application deployment.

## Get a VPS

The first step is to get your own virtual private server. You can get one on Digital Ocean which can prepare a VPS with your public SSH key in place, so that you don't have to worry much about SSH configuration besides getting a public/private key pair. As the operating system, choose Fedora.

You can support Sidewinder by signing up with the affiliate link below (you will get $200 credit you can use in 60 days):

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=04e320071eab&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

Sidewinder is prepared to be deployed to a VPS that has a static IP address, but also to a custom domain with https. In that case, you will also need to register a domain and point it your VPS.

Before proceeding, make sure that you have a running private virtual server that you can access with `SSH`.

!!! warning

    Sidewinder is prepared to be run on Fedora operating system. When creating your VPS, make sure you choose Fedora Linux distribution as your OS.

## Install Ansible

The next step is to install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

## Configure hosts.ini

Copy `deployment/ansible/hosts.ini` to  `deployment/ansible/myhosts.ini` and set `ansible_user` to be the name of your server account (like `root`) and set `ansible_host` to the IP address of your server.

Example:

```ini
[all]
host_name ansible_user=root   ansible_host=29.38.208.180
```

## Configure vars.yml

Now it's time to configure your server settings. Copy `deployment/ansible/vars.yml` to `deployment/ansible/myvars.yml`. You might eventually want to configure each property in the file for your production server. 

At the minimum to run a successful test deployment you will need to change:

- `project_name` to be the name of your application, website or app, e.g. `My website`
- `domain_name` to point to the server's IP address or your domain, e.g. `example.com`
- `git_url` to your repository fork of Sidewinder, e.g. `git@github.com:name/mywebsite.git`
- `git_key_file` to point to your private SSH key file on a local system, e.g. `/home/user/.ssh/id_rsa`
- `django_ssl` set to `1` if you are using a domain (`0` otherwise)

You should also change all passwords and secrets:

- `django_secret_key`

And set email server settings:

- `django_default_from_email`, e.g. `hi@example.com`
- `django_server_email`, e.g. `admin@example.com`
- `django_email_host`, e.g. `smtp-relay.example.com`
- `django_email_port`, e.g. `587`
- `django_email_host_user`
- `django_email_host_password`
- `admin_email`, e.g. `admin@example.com`

Other variables like `project_user`, `app_name`, `db_name` will be used to configure user, app and db names on the server. If you don't plan to use the VPS for other purposes (recommended) or you are not familiar with restrictions on these names, it might be better not to set different values.

!!! warning

    It is important to point `git_url` to your repository and to commit and push all application changes you have made to the repository. That's because our deployment Ansible playbook will download and deploy the exact version of the application that will be at the `git_url`.

## Run Ansible playbook

The provided Ansible playbook will download a copy of your Git repository and deploy the last committed version from the `master` branch to the specified server. Everything that you want to deploy needs to be pushed to your remote Git repository.

```bash
cd deployment/ansible 
make provision
```

!!! warning

    You need to be able to run `Makefile` files on your operating system using the `make` command.

Wait until the deployment is finished.

You can verify it by visiting your domain on https or your IP address on http in your browser.

!!! tip

    Consider using [Mitogen for Ansible](https://mitogen.networkgenomics.com/ansible_detailed.html) to make Ansible faster.

## Create a superuser

If the server is up and running we can create our server superuser:

```bash
# inside deployment/ansible 
make createsuperuser
```

## Final steps

There are some final steps to do if you want all features to work:

1. Log in to your Django admin at `ipaddress-or-domain/dj-admin/` and create a flat page for URL `/terms/`.



