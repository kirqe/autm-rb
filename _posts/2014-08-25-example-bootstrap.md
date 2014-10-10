---
title: "Autm-rb some bootstrap"
tags: [read this first, bootstrap, css]
---
###To customize default bootstrap components and variables use <mark>stylesheets/bs.scss</mark>
You can use all the available components of TwitterBootstrap. Here are some of them.

## Buttons and Font Awesome

It imports the latest version of [Font Awesome](http://fortawesome.github.io/Font-Awesome). You can use it with `button`s like so:

<button type="button" class="btn btn-primary"><i class="fa fa-twitter"></i> Tweet</button>
<button type="button" class="btn btn-default"><i class="fa fa-envelope-o"></i> Email</button>

## Text Helpers

Modify text with text helper classes. Documentations [here](http://getbootstrap.com/css/#helper-classes-colors) and [here](http://getbootstrap.com/css/#type-alignment).

<p class="text-muted">Use <code>text-muted</code> to mute text color.</p>

<p class="lead">Use <code>lead</code> to for call-out text.</p>

<p class="text-center">Use <code>text-center</code> to center text.</p>

## Alerts

<div class="alert alert-success" role="alert">Success alert. Customize other alerts in bs.scss</div>

## Responsive Embed

Add `embed-responsive` and either `embed-responsive-16by9` or `embed-responsive-4by3` classes to make embedded objects responsive.

<div class="embed-responsive embed-responsive-16by9">
<iframe width="560" height="315" src="//www.youtube.com/embed/8vJiSSAMNWw" frameborder="0" allowfullscreen></iframe>
</div>

## JavaScript Components

You can use all of the JavaScript components included by Bootstrap. Example: <a data-toggle="modal" data-target="#myModal" href="#">A modal dialog.</a>

<div class="modal fade" id="myModal" tabindex="-1" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Modal Dialog</h4>
      </div>
      <div class="modal-body">
        <p>Hello World!</p>
      </div>
    </div>
  </div>
</div>

## Customizing Bootstrap

Autm-rb uses [bootstrap-sass](https://github.com/twbs/bootstrap-sass), so all of the variables are customizable.
