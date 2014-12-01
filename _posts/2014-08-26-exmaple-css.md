---
title: "Autm-rb essential stuff"
tags: [read this first, bootstrap, css]
---

This theme uses [Bootstrap](http://getbootstrap.com/) for styling. Here're some stuff you should know before using it. To learn more, check out Bootstrap's [documentation](http://getbootstrap.com/css/).

## Headings

`h1` tags are reserved for the post title. Don't use them. Use `h2` tags mostly, and use `h3` if you need subheadings.
Or just  edit <mark>stylesheets/style.css</mark>

## Paragraphs

**This is a regular paragraph.** Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's <mark>standard</mark> dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

Links look like [this](#). *Emphasis*. <mark>Marked</mark>. <del>Deleted</del>. <code>Code</code>. <kbd>user-input</kbd>.

## Blockquotes

> **This is a blockquote**. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

## Lists

* Unordered List
* Unordered List
* Unordered List

1. Ordered List
1. Ordered List
1. Ordered List

## Tables

You don't need to add the Bootstrap `.table` class to `table`. This is how it works.

<table>
  <thead>
    <tr>
      <th>name</th>
      <th>type</th>
      <th>link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Jekyll</td>
      <td>BlogEngine</td>
      <td><a href="http://jekyllrb.com/">jekyllrb.com</a></td>
    </tr>
  </tbody>
</table>

## Code

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('jekyll')
#=> prints 'Hi, jekyll' to STDOUT.
{% endhighlight %}

## Images

Images are responsive.
![]({{site.baseurl}}/images/local/colorsp.png)

## That's it!

Here're some more examples [{{ page.previous.title }}]({{ page.previous.url | prepend:site.baseurl }}) to learn more.
