% include templates/header.tpl

<div style="margin-top:120px">
<h1 class = "textTitle" style = "padding-left: 500px;">Javascript Syntax</h1>
<p>Syntax refers to the way in which code is structured. This is essential in order to create
functional code with the ability to control flow, create conditions and develop functions.</p>
<h2><b>1.0 Variables</b></h2>
<p>Refer to objects that store a value. The most common forms of variables include the
following:</p>
<ul>
    <li>Booleans: Store true or false values. </li>
    <li>String: Store a series of characters (symbols, letters or numbers) as text</li>
    <li>Number: Stores an integer or decimal value.</li>
    <li>Array: Stores multiple values of the same or different objects.</li>
    <li>Object: A custom data form for storing anything else in a variable.</li>
</ul>
<p>
To initialise a variable in Javascript, the following format is used.
</p>
<pre>
<code>
    let variableName = ‘variableContent’;

    let myNumber = 1;

    let myBoolean = true;

    let myArray = [1, 2, ‘a’, ‘b’, true, false];
</code>
</pre>
<h2><b>2.0 Basic Operations</b></h2>
Operations allow the comparison of multiple variables, and the alteration of those variables.
These include basic arithmetic and assignment operations as follows:
<table class = "discussionTable">
    <tbody>
        <tr>
            <th>Addition Oeration</th>
            <th >+</th>
            <th>Add 2 variables together</th>
        </tr>

        <tr>
            <th>Subtraction Oeration</th>
            <th >-</th>
            <th>Subtract 2 variables together</th>
        </tr>

        <tr>
            <th>Multplication Oeration</th>
            <th >*</th>
            <th>Mutiply 2 variables together</th>
        </tr>

        <tr>
            <th>Division Oeration</th>
            <th >/</th>
            <th>divide 2 variables together</th>
        </tr>

        <tr>
            <th>Equality  Oeration</th>
            <th >===</th>
            <th>return true if the values of 2 variable is equal</th>
        </tr>




    </tbody>
</table>
<h2><b>3.0 Control flow</b></h2>
<p>
Control flow refers to the way in which code is execute and how to make changes to this
sequence. In order to control flow in JavaScript, we use conditional statements in the
following format:
</p>
<span>
Condition
</span>
<pre>
<code>
if(condition) {
    alert(‘condition has been met’);
} else {
    alert(‘condition failed’);
}
</code>
</pre>
<p>
Loops:When working with arrays, a scenario often arises when a condition needs to be checked
against all elements of the array. As such, a for loop can be used in the following format:
</p>
<pre>
<code>
let i = 0;
for(i = 0; i < myArray.length; i++) {
    functionForEachObject();
}
</code>
</pre>

<h2><b>4.0 Functions</b> </h2>
<p>Functions allow the coder to create generalised code that can return a specified output
from given inputs.</p>
<pre>
<code>
function(name){
    return name
}
</code>
</pre>
<div style="margin-bottom:120px; padding:2%">

% include templates/tailer.tpl