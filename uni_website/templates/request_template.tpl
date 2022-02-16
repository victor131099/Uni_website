% include templates/header.tpl

<div style="margin-top:120px; padding:2%">
<h1 class = "javascript-title">Templates </h1>
<p>Bottle comes with a fast and powerful built-in template engine called SimpleTemplate Engine. To render a template you can use the template() function or the view() decorator. All you have to do is to provide the name of the template and the variables you want to pass to the template as keyword arguments. Here’s a simple example of how to render a template:</p>
<pre>
    <code>
    @route('/hello')
    @route('/hello/<name>')
    def hello(name='World'):
        return template('hello_template', name=name)
    </code>
</pre>
<p>This will load the template file hello_template.tpl and render it with the name variable set. Bottle will look for templates in the ./views/ folder or any folder specified in the bottle.TEMPLATE_PATH list.</p>
<h2><b>Syntax</b></h2>
<p>The template syntax is a very thin layer around the Python language. Its main purpose is to ensure correct indentation of blocks, so you can format your template without worrying about indentation. Follow the link for a full syntax description: SimpleTemplate Engine

Here is an example template:</p>
<pre>
    <code>
    if name == 'World':
        &lt;h1&gt;Hello {name}!&lt;/h1&gt;
        &lt;p&gt;This is a test.&lt;/p&gt;
    else:
        &lt;h1&gt;Hello {name.title()}!&lt;/h1&gt;
        &lt;p&gt;How are you?&lt;/p&gt;
    end
    </code>
</pre>
</div>

% include templates/tailer.tpl