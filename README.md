# Star-Fitness

## What is Used
- Python 3.10
- Django 
- Django-allauth
- Stripe

## Project Photos

### Landing Page
![Landing Page](./project-photos/landing-page.png)

### Home Page
![Home Page](./project-photos/home.png)

### Logged in Subscribed user
![Subscribed](./project-photos/member-only.png)

### Not logged in
![Membership Page 1](./project-photos/member-page.png)

### Logged in but not subscribed
![Membership Page 2](./project-photos/member-page-2.png)

### Stripe Payment
![Stripe Payment](./project-photos/payment.png)

### Signup Page
![Signup Page](./project-photos/signup.png)

### Login Page
![Login Page](./project-photos/login.png)

### Logout Page
![Logout Page](./project-photos/logout.png)

## how to start

First create virtual environment and install dependency by following:
```bash
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Inside `src/config/`, create `.env` file and create the following environment variable:
```bash
SECRET_KEY
DEBUG
STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY
STRIPE_ENDPOINT_SECRET
DOMAIN_URL
```

For the local development, set `DEBUG` and `DOMAIN_URL` to `True` and `http://localhost:8000/`, repectively

`SECRET_KEY` is a Django secret key

`STRIPE_PUBLISHABLE_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_ENDPOINT_SECRET` must be retrieved from the Stripe (please refer to Stripe Integration section).

While we are creating the Stripe account, make sure to create Product object with Monthly and Yearly Prices. (please refer to Stripe Integration section).

We can `cd` in to `./src`.

Before we can start we need to make migrations and create super user:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

Enter email address and password.

We can start the application with following command:
```bash
$ python manage.py runserver
```

Before we can subscribe though, we must create Membership model object for Monthly and Yearly (id for Monthly must be 1 and 2 for Yearly; If the ids are different, `./src/main/static/js/script.js` must be fixed appropriately)
  - If the ids are different, change the fetch urls appropriately.
  - Each Membership model requires name and priceId.
  - Retrieve the priceId from Stripe Dashboard.

That's it! Have fun!

## Stripe Integration

Stripe integration was based on [this tutorial](https://testdriven.io/blog/django-stripe-subscriptions/)