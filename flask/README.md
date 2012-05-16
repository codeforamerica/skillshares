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

### Commit changes

Now that our small app is working, we should make our first commit.

    $ git add -A
    $ git commit -m "First commit"


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

Now, visit the Code for America endpoint:
[`http://localhost:5000/cfa`](http://localhost:5000/cfa).

Also, notice how the `/my/name/is` endpoint isn't static:
[`http://localhost:5000/my/name/is/zach`](http://localhost:5000/my/name/is/zach)

### Variables

Using variables with Flask's routing is pretty awesome -- this is how
the previous `/my/name/is` endpoint worked.

Let's create a route that displays our favorite number.

```python
@app.route('/my/favorite/number/is/<int:number>')
def favorite_number(number):
    return str(number)
```

Note that we specify the number is an integer, and then we return it in
string form using the `str` function. If we didn't convert the number to
a string, then we'd get an error page.

It should also be noted that function names are completely arbitrary.
So, if you don't feel like typing out `favorite_number`, you could type
something as simple as `poop` and it'd still work.

```python
@app.route('/my/favorite/number/is/<int:number>')
def poop(number):
    return str(number)
```

### git

It's important to note that we should be committing code fairly
regularly. This way, in case anything blows up, we can always revert to
a previous state. `git` also allows use to go off on tangents with
branches and just try things out (without messing up the master branch).

So, with that in mind, let's commit what we have so far.

    $ git commit -am "Add routes"

The `a` flag allows you to add all changes to **already tracked files**
and the `m` flag allows you to follow the commit with a message. This is
basically shorthand way to write:

    $ git add -A
    $ git commit -m "Add routes"


Templating
----------

While Flask's routing alone is pretty useful, templating makes it
awesome -- especially since it uses the [Jinja template
engine](http://jinja.pocoo.org/docs/).

To start using templates, let's create a `templates` directory to store
them.

    $ mkdir templates
    $ (cd templates && touch {base,home,cfa}.html)

There should now be three template files in the directory. Also, notice
that by using the `cd` command inside parentheses (it creates a
subshell), we never have to `cd` back a level. And, lastly, the `&&`
inside the command basically executes as "if the last thing worked out,
now do this."

Now, let's start adding content to the `base.html` file.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{% block title %}My Site{% endblock %}</title>
  {% block css %}{% endblock %}
</head>

<body>
  {% block main %}{% endblock %}

  <!-- JavaScript at the bottom for fast page loading -->
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  {% block js %}{% endblock %}
</body>
</html>
```

Notice the `block` statements. These allow us to extend the `base.html`
file with further content in specific areas. Let's add content to the
`home.html` file and then modify our `app.py` file.

```html
{% extends "base.html" %}

{% block css %}
  <style type="text/css">
  h1{
    color: #bada55;
  }
  </style>
{% endblock %}

{% block main %}
  <h1>Hello, World!</h1>
{% endblock %}
```

And we can modify the `app.py` file to now point to our `home.html`
file:

```python
"""
My Flask website.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
```

Go ahead and check out [`http://localhost:5000`](http://localhost:5000)
now, you should see a `#bada55` element.
