# gcp-cloud-function-python-base
Template to build small Python applications with Cloud Functions.

## Why use this?
The purpose for this template is to deploy a Python application to be run as a Cloud Function with all the basics
included like a proper folder structure, a set of application defaults or some basic unit tests. Add your own classes 
and/or functions to the mix and there you have... a working application ready to be deployed in (hopefully) no time.

**TL; DR** oh... you don't have to, but if you do you'll save time (and, probably, money too!) every time you need a 
quick solution running as a Cloud Function.

## How can I use this template?
Using this template is as straightforward as cloning this repository, setting up the virtual environment for it and 
you're on the go. However, I made some assumptions that may not be valid for you so you need to take them into account
before using it.

### Assumptions
These are the assumptions made with this template:

1. We are going to use Python 3.x so the setup commands will read like `python` and `pip` (in contrast with `python3` 
and `pip3` on systems where both Python 2.x and 3.x are installed)
2. We are going to deploy the application as a .zip file rather than using the inline code editor (that's why there are 
some support scripts, like `pack`, to deal with that)
3. The main function name is (*ahem...*) **cloud_function** (*creativity at its best!*)
4. I work with every major operating system out there on a daily basis but my operating system of choice is Linux at 
work and macOS at home so the support scripts may not work for you if you're on a Windows machine (or, at least, I 
haven't tested them)
5. The response from the application will be REST-like, JSON-encoded with up to three fields in the response: `data` 
(you can provide a dictionary or a list as a payload), `message` (if you want an explicit message) and `status` (`OK`
if the status code is `200 OK`, `ERROR` otherwise). An example of a successful response would be `{"status":"OK"}`
along with a `200 OK` status code, whereas an example of an unsuccessful response would be `{"status":"ERROR"}` along 
with its appropriate status code

### Steps
1. Clone the repository
2. Initialize the virtual environment (PyCharm does this for me in an almost automatically but if 
you're using the console or some IDEs like Visual Studio Code, `python -m venv venv/`, `source venv/bin/activate` 
and `pip install -r requirements.txt` will produce the same result)

After this you'll have a working template with three core files: `src/application.py` (where the application class 
is defined along with its `run()` method, which is the one getting called), `main.py` (the main application script 
and the one that gets executed as a Cloud Function) and `app.py` (the 
[Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) equivalent of the main application script, so you can 
debug your projects locally before deploying them onto Cloud Functions like this (from the terminal): 
`flask --debug run`).

The real magic happens in `src/application.py` (within the `run()` method) so, unless you have very specific needs, you 
don't need to touch neither `app.py` nor `main.py`.

## I wrote and tested my application. Now what?
The only thing left to do, before uploading to Cloud Functions, is to pack your application contents into a .zip file.

### Packing your application
This template includes a set of directories: `build/` (where all application files are copied and/or installed before 
zipping them) and `dist/` (where the resulting .zip files are stored). It also includes a set of support scripts: 
`clear-all` (which clears both `build/` and `dist/` directories), `clear-build` (which clears the `build/` directory), 
`clear-dist` (which clears the `dist/` directory) and `pack` (which installs the Python modules your application needs 
(along with some other libraries), copy your application files and compresses the contents of the `build/` folder and 
write the resulting .zip file onto the `dist/` folder with the current date and version number encoded in its name). 

In order to pack your application, you just need to execute this on the terminal: `./pack`. Once finished, you will find
your application packed in the `dist/` folder. An example of a packed application file would be 
`gcp-cloud-function-python-base-2023-08-17-v1.zip`. The only thing left for you is to drop that file onto your Cloud
Function to create (or update) it and that's all :)

### Version numbering
Hey, it happens all the time. Your application is deployed and running and, then, you discover a bug or a new feature is
requested, and you know what that means: back to the workbench!

Once finished, it's about time to pack your application again and update your Cloud Function. In order for you to be 
able to update your Cloud Function as many times as you need (or want) the current date and version number are encoded 
onto the filename, so the first time you pack your application it may end with a name like 
this: `gcp-cloud-function-python-base-2023-08-17-v1.zip`.

If you happen to pack your application more than once in a day the packing script will account for your previous
versions, so you can keep control of the exact version you send to Cloud Functions for update. An example of this would
be (if we pack our application a second time): `gcp-cloud-function-python-base-2023-08-17-v2.zip`. Need to pack it a
third time? `gcp-cloud-function-python-base-2023-08-17-v3.zip`. A fourth? 
`gcp-cloud-function-python-base-2023-08-17-v4.zip`. And the version count goes on... :)

## And that's about it!
If you find a bug or something for improvement file the appropriate request and I will gladly take a look at it.

Happy coding!
