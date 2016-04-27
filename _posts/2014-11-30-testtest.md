---
title: "Test post"
tags: [test_tag]
---


### The standard Lorem Ipsum passage, used since the 1500s
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

The standard Lorem Ipsum passage, used since the 1500s

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

![test](http://i.imgur.com/WWCgxX9.jpg)


### Code hightlight examle

{% highlight ruby %}
def index
  @posts = Post.cached_short_listed.paginate(:page => params[:page])
end

def new
  @post = Post.new
end

def create
  @post = Post.new(post_params)
  @post.user = current_user
  respond_to do |format|
    if @post.save
      format.html {redirect_to @post, notice: 'New post created.'}
      format.json{render json: @post, status: :created, location: @post}
    else
      format.html {render action: 'new'}
      format.json {render json: @post.errors, status: :unprocessable_entry}
    end
  end
end
{% endhighlight %}

{% highlight css %}
code {
  font-family: "Lucida Sans", Monaco, Bitstream Vera Sans Mono, Lucida Console, Terminal, monospace;
  font-size: 13px;
  margin: 0 4px;
  padding: 4px 6px;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  -ms-border-radius: 2px;
  -o-border-radius: 2px;
  border-radius: 2px;
    color: #848282;
}
{% endhighlight %}


<a href="https://github.com/railsr/autm-rb" target="_blank" class="btn btn-success"><i class="fa fa-github fa-lg"></i> View on GitHub</a>
