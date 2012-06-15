Bootstrap
=========

Twitter's [Bootstrap framework](http://twitter.github.com/bootstrap/) is
an awesome resource to get a MVP-type site up and running.
Unfortunately, many of the sites made with Bootstrap don't capitalize on
the `less` files included in the [Github
project](http://github.com/twitter/bootstrap) for customizing the
default style and colors.

Obviously, the best way to learn all about the niceties and proper usage
of Bootstrap is either [the documentation](http://twitter.github.com/bootstrap)
(which is a living example of best practices -- it's built with
Bootstrap) or the [code on Github](http://github.com/twitter/bootstrap).
This skillshare doesn't aim to replace either of those. This is just a
handy guide of heuristics and tips for how I go about building quick
websites.

I do want to pass off one piece of advice before moving on to other
things, though -- the best way to learn Bootstrap, in my opinion, is to
**make a ton of crappy sites**. Normally once you've made three or four
crappy sites, Bootstrap will fit in pretty nicely with your workflow.
Also, those first three or four might not be the best-looking sites --
hence the emphasis on crappy.

### Alternatives

As with anything in front-end development, there are tons of
alternatives to the things mentioned here.
[Foundation](http://foundation.zurb.com) is one of the most well-known
alternatives to Bootstrap, and both [Sass](http://sass-lang.com/) and
[Stylus](http://learnboost.github.com/stylus/) are alternatives to
[Less](http://lesscss.org).

However, none of those will be covered. This skillshare is less about
the possibilities of creating quick websites and will be more about the
particular workflow I use.


Installation
------------

Boring things first. The easiest way to get started with Bootstrap for
those who don't like the command line and/or Git is by [downloading
Bootstrap from the official documentation](http://twitter.github.com/bootstrap).
If, however, you like the command line and want to use an awesome
`Makefile`, I've set up a [project to do just
that](http://github.com/zachwill/bootmaker) (it does have a few
dependencies, however).

If you do opt for downloading Bootstrap, you're going to want to grab
the `mixins.less` file -- in my opinion, this is the single greatest
part of using Bootstrap. In addition, you're going to need to get `Less`
in order to take advantage of the mixins.

From the command line (in your current project) you can run:

```
curl -L git.io/mixins > mixins.less
curl -L git.io/less-1.3.0 > less.js
```

### Structure

I normally set up my directories to look like the following:

```
├── js
├── img
└── css
    └── less
```

Then, depending on whether you're making a quick static site or setting
up something like a [small Jekyll project](http://github.com/zachwill/doc),
your project can also contain `README.md`, `index.html`, and `CNAME` files.


Heuristics
----------

While I can't really walk you through the documentation (it's best you
look through it on your own), I can help put you in the right mindset
for using Bootstrap in your projects.

### Rectangles

The easiest way to approach building your website in Bootstrap is to
think in **rectangles**. This might sound a little weird (and you might
be asking yourself why we're covering this rather than code right now),
but it pays off in the end.

If you think of cutting your design into rectangles -- both in row and
column form -- you can hit the ground running pretty fast.

### Responsive

It's also a best practice, in my opinion, to go the responsive route
with Bootstrap. By just adding one CSS file, your markup expands and
shrinks based on the size of the browser/screen. Also, this can help
lead you away from trying to get pixel perfect layouts and instead
design similar to [Style Tiles](http://styletil.es). Plus, I just think
it looks cool.

### Less CSS

If you're really going to take advantage of Bootstrap, you're also going
to need to use [Less CSS](http://lesscss.org) in your project. As I
stated before, the best part of Bootstrap, in my opinion, is the
`mixins.less` file.

But, what if you've already been developing your site with plain, old
CSS? No worries. Valid CSS is valid Less -- so you're not in any
trouble.

Also, once you see the beauty of variables, mixins, color functions, and
inheritance, you'll understand why Less is pretty awesome.

### Divitis

More of a warning than anything, you're going to suffer from
[divitis](http://www.google.com/search?q=divitis) when using Bootstrap.
It's going to seem like overkill with the amount of `div` elements we'll
be using, but you'll end up with a responsive website that adapts and
works with anything from an iPhone to IE7 -- so you'll just more or less
have to get used to it.

There might also be alternative ways to achieve the same effects that
we'll be going for, but, as of right now, don't be suprised to see HTML
that looks like this:

```html
<section class="background">
  <div class="container">

    <div class="row">
      <div class="span6">
        <!-- A column half the width of the row -->
      </div>
      <div class="span6">
        <!-- Another column half the width of the row -->
      </div>
    </div>

  </div>
</section>
```


Code
----

The best way to go from here is probably by writing some code. I've
included a boilerplate `index.html` file that marks where your content
should go. We can also create a simple server for our project with the
following command:

```
python -m SimpleHTTPServer 5555
```

You should then be able to visit [`http://localhost:5555/`](http://localhost:5555/)
in your browser.

### First Site

The first site we'll make should look like the following.

![](https://github.com/codeforamerica/skillshares/raw/master/bootstrap/site.png)

Notice how it naturally is divided into three sections (red, green, blue),
with distinct columns in each? That should make it pretty easy to
code in Bootstrap (notice it does look rectangular).

At a meta level, our markup should look something like this.

```
├── red
    └── column
        └── text
    └── column
        └── image

├── green
    └── column
        └── image + text
    └── column
        └── image + text
    └── column
        └── image + text

└── blue
    └── column
        └── image
    └── column
        └── text
```

It's easy to begin to turn this into HTML. Each of those top levels will
become a `<section>`. But, what about the columns?

Well, looking at the picture again, each of the sections does have
different column layouts (or intends to), but the columns in each
section are in a single `row` (just trust me if you're skeptical). So,
our updated meta level for red should actually look like this:

```
├── red
    └── row
        └── column
            └── text
        └── column
            └── image
```

Now, I'm going to introduce a simple rule: each `row` has a width of 12
units, and those columns need to total up to (or be less than) 12.

So, our meta level will need to be updated once more:

```
├── red
    └── row
        └── column6
            └── text
        └── column6
            └── image
```

Lastly, I'm going to add another rule: a `row` has to be held in a
`container`. Not every `row` has to have its own `container`, but there
does need to be at least one.

There are now two ways to go forward: **fluid** and **regular**.

### Fluid

Making our web page fluid can help reduce the amount of `div` elements
we'll have to use in order to achieve the desired effect of having
full-screen backgrounds.

### Regular

Couldn't that `container` just be the `section`? **Nope**. Notice how the
color covers the entire page width in the picture? `Containers` aren't
allowed to be the full width of the page -- in fact, they help constrain
the content when it comes to our page being responsive.

So, the updated meta level should look like:

```
├── red
    └── container
        └── row
            └── column
                └── text
            └── column
                └── image
```

It's pretty easy to turn that into the correct Bootstrap markup:

```html
<section class="red">
  <div class="container">

    <div class="row">
      <div class="span6">
        <p>Lorem ipsum text.</p>
      </div>
      <div class="span6">
        <img src="http://placehold.it/600x400" />
      </div>
    </div>

  </div>
</section>
```

Try writing the `blue` and `green` ones on your own.
