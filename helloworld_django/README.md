helloworld_django
=================

A helloworld HTTP endpoint app made in Python and Django 1.9.4

#### setup
Please make sure to run the following to install dependencies
    $ sudo pip install -r requirements.txt

After which, the following should be run for Django purposes

    $ python manage.py migrate

To start the server, please run

    $ python manage.py runserver

The HTTP endpoint can be accessed at the following address

 - http://127.0.0.1:8000/

#### test
To test the GET response with no Accept headers, run
```bash
curl -X GET "http://127.0.0.1:8000/"
```
To test the GET response with an application/json Accept header, run
```bash
curl -X GET -H "Accept: application/json" "http://127.0.0.1:8000/"
```

The unittests utilize the `Httpretty` and `requests` packages for mocking http requests. To run them from the project root directory, call
```bash
python helloworld/test.py
```
