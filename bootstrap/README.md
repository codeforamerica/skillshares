Bootstrap
=========

Twitter's [Bootstrap framework](http://twitter.github.com/bootstrap/) is
an awesome resource to get a MVP-type site up and running.
Unfortunately, many of the sites made with Bootstrap don't capitalize on
the `less` files included in the [Github
project](http://github.com/twitter/bootstrap) for customizing the
default style and colors.

One of the best examples of a customized Bootstrap site I've come across
is [Style Tiles](http://styletil.es). It builds upon the default
Bootstrap CSS, rather than just conforming to the defaults.


Github Pages
------------

Since this is a simple site, let's keep it static and serve it through
Github Pages (Heroku is an awesome alternative, too).

    $ mkdir simple_site && cd simple_site
    $ touch README.md

We can now update the `README.md` file with some information on our
site, and then we can initialize Git.

    $ git init
    $ git add --all
    $ git commit -m "First commit"

Now, it's time to create the project on Github and add it as a remote.
Once you've created the project, you can copy the command that looks
like this:

    $ git remote add origin git@github.com:username/project.git

And we can push our project up to Github.

    $ git push -u origin master

Since this is a Github Pages project, we'll need to create our site in a
`gh-pages` branch.

    $ git checkout -b gh-pages

For the majority of our project, we'll remain in the `gh-pages` branch.


Bootstrapping
-------------

In order to `clone` and `make` Bootstrap, you will need to install
`recess` and `watchr` with [`npm`](http://npmjs.org/) and
[`node.js`](http://nodejs.org/#download):

    $ npm install -g recess watchr

### Bootmaker

I've created the [Bootmaker project](https://github.com/zachwill/bootmaker)
to help you get up and running with Bootstrap as fast as possible. To
install, simply run this from the command line:

    $ curl -L http://git.io/bootmake > Makefile
    $ make
