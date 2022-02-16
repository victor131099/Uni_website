% include templates/header.tpl

<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" href="../static/css/styles.css" >
    <title>CSS Content</title>

    </head>

    <body style="background-color: rgb(234, 234, 234)">
        <h1 style="font-size:52px"></h1>
        <div class="section">
            <h1 style="font-size:52px">CSS</h1>
            <div class="module">
                <p>Welcome to a beginners guide to coding with CSS.</p>
                <p>By using CSS we can greatly improve the productivity of web development! In our CSS tutorial, you'll learn how to use CSS to control the style and layout of multiple Web pages at once.</p>

            </div>
        </div>

        <div class="module">
            <a id="What Is CSS?">
                <h1>What is CSS?</h1>
                <p>CSS stands for Cascading Style Sheets</p>
                <p>CSS describes how HTML elements are to be displayed on screen, paper, or in other media</p>
                <p>CSS saves a lot of work. It can control the layout of multiple web pages all at once</p>
                <p>External stylesheets are stored in CSS files</p>
                <p>External stylesheets can greatly improve productivity</p>
                <p>Multiple style definitions can be stacked into one</p>
            </a>

            <a id="Why Use CSS?">
                <h2>Why Use CSS?</h2>
                <p>CSS is used to define styles for your web pages, including the design, layout and variations in display for different devices and screen sizes.</p>
            </a>

            <p> Already know some HTML? Jump to a topic with the links below: </p>

            <a href="#CSS Syntax">1.0 CSS Syntax</a>
            <br>
            <a href="#How to add CSS?">2.0 How to add CSS?</a>
            <br>
            <a href="#CSS Selectors">3.0 CSS Selectors</a>
            <br>
            <a href="#CSS Colours">4.0 CSS Colours</a>
            <br>

        </div>

        <div class="module">
           <a id="CSS Sytnax">
               <h2>CSS Sytnax</h2>
               <br>
               <img src="img/css syntax.png" alt="Example1: <!DOCTYPE html> <html>" style="height:190px">
               <br>
               <br>
               <p align="left"><strong>--&gt;</strong> A selector is usually an HTML element that you need to change the style of.</p>
               <p align="left"><strong>--&gt;</strong> The declaration block contains one or more declarations separated by semicolons.</p>
               <p align="left"><strong>--&gt;</strong> Each declaration includes a CSS property name and a value, separated by a colon.</p>
               <p align="left"><strong>--&gt;</strong> Multiple CSS declarations are separated with semicolons, and declaration blocks are surrounded by curly braces.</p>

               <br>
           </a>
        </div>
        <div class="module">
           <a id="How to add CSS?">
               <h2>How to add CSS?</h2>

               <p> There are three ways of inserting a style sheet:</p>
               <p><a href="#External CSS">2.1 External CSS</a></p>
               <p><a href="#Internal CSS">2.2 Internal CSS</a></p>
               <p><a href="#Inline CSS">2.3 Inline CSS</a></p>

               <br>
           </a>

           <a id="External CSS">
               <h3>2.1 External CSS</h3>

               <p align="left">With an external style sheet, we can change the look of an entire website by changing just one file.
                 Each HTML page must include a reference to the external style sheet file inside the element, inside the head section.</p>
              <br>
              <p align="left"><strong>--&gt;</strong> Example: </p>
              <img src="img/externalcss1.png" width="400" height="350"> <img src="img/externalcss2.png" width="350" height="350">
              <br><br>

           </a>

           <a id="Internal CSS">
              <h3>2.2 Internal CSS</h3>

              <p align="left">An internal style sheet may be used if one single HTML page has a unique style. The internal style is defined inside the <strong>&lt;</strong> style <strong>&gt;</strong> element, inside the head section.</p>
              <br>
              <p align="left"><strong>--&gt;</strong> Example: </p>
              <img src="img/internalcss.png" width="400" height="450">
              <br><br>
           </a>

           <a id="Inline CSS">
              <h3>2.3 Inline CSS</h3>

              <p align="left">An inline style may be used to apply a unique style for a single element. To use inline styles, add the style attribute to the relevant element. The style attribute can contain any CSS property.</p>
              <br>
              <p align="left"><strong>--&gt;</strong> Example: </p>
              <img src="img/inlinecss.png" width="600" height="200">
              <br><br>
           </a>

           <h3>Cascading Order</h3>

           <p align="left"> All the styles in a page will "cascade" into a new "virtual" style sheet by the following rules, where number one has the highest priority:</p>
           <p align="left"><strong>&#183;</strong> Inline style (inside an HTML element)</p>
           <p align="left"><strong>&#183;</strong> External and internal style sheets (in the head section)</p>
           <p align="left"><strong>&#183;</strong> Browser default</p>
           <p align="left">So, an inline style has the highest priority, and will override external and internal styles and browser defaults.</p>
        </div>

        <div class="module">
           <a id="CSS Selectors">
               <h2>CSS Selectors</h2>

               <p align="left"> We can divide CSS selectors into five categories:</p>
               <p align="left"><strong>&#183;</strong> Simple selectors (select elements based on name, id, class)</p>
               <p align="left"><strong>&#183;</strong> Combinator selectors (select elements based on a specific relationship between them)</p>
               <p align="left"><strong>&#183;</strong> Pseudo-class selectors (select elements based on a certain state)</p>
               <p align="left"><strong>&#183;</strong> Pseudo-elements selectors (select and style a part of an element)</p>
               <p align="left"><strong>&#183;</strong> Attribute selectors (select elements based on an attribute or attribute value)</p>
               <br>

               <h3>Most basic selectors</h3>
               <h4>3.1 The CSS element Selector</h4>
               <p>The element selector selects HTML elements based on the element name.</p>
               <br>
               <img src="img/csselement1.png" width="1000" height="300">
               <br><br>

              <h4>3.2 The CSS id Selector</h4>
              <p align="left">The id selector uses the id attribute of an HTML element to select a specific element. The id of an element is unique within a page, so the id selector is used to select one unique element. To select an element with a specific id, write a hash (#) character, followed by the id of the element.</p>
              <br>
              <img src="img/cssidselector.png" width="1000" height="300">
              <br><br>

             <h4>3.3 The CSS class Selector</h4>
             <p align="left">The class selector selects HTML elements with a specific class attribute. To select elements with a specific class, write a period (.) character, followed by the class name.</p>
             <br>
             <img src="img/cssClassSelector.png" width="1000" height="300">
             <br><br>

             <p>You can also specify that only specific HTML elements should be affected by a class.</p>
             <br>
             <img src="img/cssClassSelector2.png" width="1000" height="300">
             <br><br>

             <h3>All CSS Simple Selectors</h3>
             <img src="img/allSelectors.png" width="800" height="300">
             <br><br>

           </a>
        </div>

        <div class="module">
           <a id="CSS Colors">
              <h2>CSS Colors</h2>
              <p align="left">Colors are specified using predefined color names, or RGB, HEX, HSL, RGBA, HSLA values. CSS/HTML support 140 standard color names.</p>
              <br>
              <h4>1. defined the color by name</h4>
              <img src="img/cssColor1.png" width="900" height="130">
              <br><br>

              <h4>2. defined color by using RGB values, HEX values, HSL values, RGBA values, and HSLA values:</h4>
              <img src="img/cssColor2.png" width="800" height="200">
              <br><br>
           </a>
        </div>
    <body>
</html>


% include templates/tailer.tpl