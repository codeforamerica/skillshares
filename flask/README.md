Flask
=====

[Flask](http://flask.pocoo.org/) is a small Python web framework. It's
best for creating simple sites that aren't database heavy, and it's
partially inspired by the Ruby [Sinatra
framework](http://www.sinatrarb.com/).

This Skillshare hopes to provide both a simple overview and functional
prototype.


Installation
------------

Installing Python libraries is somewhat tricky for beginners -- it's not
nearly as user-friendly as Ruby's `gem install`. There is a Python
installer called `pip` that is most used by the Python community, so
let's get that setup if you don't already have it.

To check to see if you have `pip` installed, run the following from your
command line.

    $ pip -h

If you get an error, you'll need to run the following:

    $ sudo easy_install pip

Once that runs, just double check that you have `pip` running:

    $ pip -h


### Flask

We now need to install Flask. It's as simple as running:

    $ pip install flask

You might get an error -- even though you have `pip` installed. This
probably means you don't have the correct permissions set up, so we'll
use `sudo` to install it:

    $ sudo pip install flask

We could talk more about permissions, but that's not nearly as fun as
building a simple site.


Creating a directory
--------------------

Let's create a directory and hit the ground running. From the command
line, we'll create a directory, initialize a new `git` repo, and start
coding. If you already have a directory for simple projects, feel free
to use that instead.

    $ mkdir flask_site
    $ cd flask_site

And initalize `git`:

    $ git init

Now, let's go ahead and create two blank files.

    $ touch {README.md,app.py}

The bracket syntax on the command line is awesome for repeating
commands. It's basically doing this:

    $ touch README.md
    $ touch app.py

Whenever I'm creating new projects, I always like to use the `touch`
command to create blank files so they show up in my text editor.


Hello World
-----------

Let's create a basic Flask site so everyone can see why they'd use a
framework versus just static pages.

In `app.py`, write the following:

```python
"""
My Flask website.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
```

While Flask is not as pretty as Sinatra (at least, in my opinion), this
should give us a simple site. From the command line, you should now be
able to run the following command and then visit
[`http://localhost:5000`](http://localhost:5000) in your browser to see
your "Hello, World!" message:

    $ python app.py

### Restarting the app

Everytime you make changes to the `app.py` file, it should reload since
the app is being run with `debug` keyword. If it doesn't, you can
shut down the app by hitting `Control-C` and then running `python
app.py` again.


Routing
-------

One of Flask's strengths is the ability to create beautiful URLs, so
let's go ahead and create a few routes for our site.

```python
"""
My Flask website.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/cfa')
def cfa():
    return "Code for America"


@app.route('/my/name/is/<name>')
def my_name(name):
    return name.title()


if __name__ == '__main__':
    app.run(debug=True)
```

Now, run `python app.py` again and visit the Code for America endpoint:
[`http://localhost:5000/cfa`](http://localhost:5000/cfa).

Also, notice how the `/my/name/is` endpoint isn't static:
[`http://localhost:5000/my/name/is/zach`](http://localhost:5000/my/name/is/zach)
