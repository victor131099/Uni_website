% include templates/header.tpl

<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" href="css/styles.css" >
    <title>HTML Content</title>

    </head>

    <body style="background-color: rgb(184, 184, 184);">
        <br>
        <div class="section" style="margin-top:80px">
            <h1>HTML</h1>
            <div class="module">
                <p>Welcome to a beginners guide to coding with HTML. Through the following steps you will be able to create webpages with buttons, links, images and many other features. Have fun learning!</p>
            </div>
        </div>

        <div class="module">
            <a id="Introduction">
                <h1>1.0 Introduction</h1>
                <p>Hyper Text Markup Language (HTML) is a widely used language for creating webpages. It dictates the layout, presentation and content that is displayed on a webpage.
                <br>Fundamentally, HTML is created through a series of Tags, Elements and Attributes. These three interlinked properties work together to dictate the content of a webpage.</p>
            </a>

            <p> Already know some HTML? Jump to a topic with the links below: </p>

            <a href="#Syntax">1.1 Syntax</a>
            <br>
            <a href="#Layout">1.2 Layout</a>
            <br>
            <a href="#Images">2.0 Images</a>
            <br>
            <a href="#Absolute & Relative Images">2.1 Absolute & Relative Images</a>
            <br>
            <a href="#Image Formatting">2.2 Image Formatting</a>
            <br>
            <a href="#Buttons">3.0 Buttons</a>
            <br>
            <a href="#URL Tags">3.1 URL Tags</a>
            <br>
            <a href="#Graphical Buttons">3.2 Graphical Buttons</a>
            <br>
            <a href="#User Input">4.0 User Input</a>
            <br>
            <a href="#Website Styling">5.0 Website Styling</a>
        </div>

        <div class="module">
            <a id="Syntax">
                <h2>1.1 Syntax</h2>
                <h3>Tags and Elements</h3>
                <p><strong>Tags</strong> are a series of set notation in HTML that are used to determine the function of blocks of code. HTML has a vast assortment of tags that perform multiple different functions.</p>
                <br>
                <img class="htmlcontent" src="/img/html_content/Example1.png" alt="Example1: <!DOCTYPE html> <html>">
                <p>In the above example, all code surrounded in angle brackets e.g. &lt;code&gt; contain tags.</p>
                <br>
                <p>The function of each tag is explained below:</p>
                <p><strong>&lt;!DOCTYPE html&gt; --&gt;</strong> Defines the document as a html readable</p>
                <p><strong>&lt;html&gt; --&gt;</strong> Defines a section that contains html content</p>
                <p><strong>&lt;head&gt; --&gt;</strong> Defines data for the document. Note: the data is not displayed on the webpage. It is used to determine metadata of the page.</p>
                <p><strong>&lt;title&gt; --&gt;</strong> The name of the page. Notice the title is within the &lt;head&gt; section. Thus it is not displayed on the page.</p>
                <p><strong>&lt;body&gt; --&gt;</strong> Defines a section containing the main display of the webpage.</p>
                <p><strong>&lt;h1&gt; --&gt;</strong> Defines a header as displayed on the right “Webpage Header”.</p>
                <p><strong>&lt;p&gt; --&gt;</strong> Creates a paragraph containing text.</p>
                <br>
                <p>An element refers to the content that is displayed within the tag. For example, the “Webpage Title” is an element of the &lt;title&gt; tag.
                <br><br>All the tags above excluding the &lt;!DOCTYPE&gt; must be closed. This is achieved by adding a forward slash tag <strong>&lt;/tag&gt;</strong>, at the conclusion of the tags content.</p>
                <br>
                <img class="htmlcontent" src="/img/html_content/Example2.png" alt="Example2: Closing a tag with a forward slash at its conclusion">

                <br>
                <h3>Attributes</h3>
                <p><strong>Attributes</strong> allow access to parameters that can be used to alter a tag’s functionality. For example.</p>
                <br>
                <img class="htmlcontent" src="/img/html_content/Example3.png" alt="Example3: Using the style attribute to modify the function of a paragraph tag.">
                <p>Notice above: multiple parameters can be accessed in a single attribute, separated by a semi-colon. As such the final text is now styled in green and aligned to the center.
                <br>
                <strong>Task 1: Create your first page!</strong>
                Using the above information and examples you have learned, create the following webpage with html:
                </p>
                <br>
                <img class="htmlcontent" src="/img/html_content/Example4.png" alt="Task 1: Create a rainbow text webpage with each paragraph aligning in diffferent horizontal positions.">
                <p>Tip: Remember to align your header, not just the paragraphs!</p>
            </a>
        </div>

        <div class="module">
            <a id="Layout">
                <h2>1.2 HTML Layout</h2>
                <p>There are two ways to layout HTML elements. These can either be sorted on a new-line (Block elements), and same-line (in-line or span elements).</p>
                <h3>Div</h3>
                <p><strong>&lt;div&gt; --&gt;</strong> Creates a block element (an element on a new line)</p>
                <p><strong>&lt;span&gt; --&gt;</strong> Creates an in-line element (content on the same line)</p>
                <br>
                <p>Example of Div and Span:</p>
                <img class="htmlcontent" src="/img/html_content/Example5.png" alt="Example4: Div new line elements and Span inline elements.">
            </a>
        </div>

        <div class="module">
            <a id="Images">
                <h1>2.0 Layout</h1>
                <p>In HTML images are created using the &lt;img&gt; tag.</p>
                <br>
                <p>There are two primary attributes for the img tag, including: scr and alt.
                <br><strong>SCR:</strong> contains the URL path to the image. This path is a webpage on the webserver that contains solely the image that is to be presented.
                <br><strong>ALT:</strong> contains text that describes the image if it is not available for viewing. This occurs when the path provided in the SRC is not valid.
                </p>
            </a>
        </div>

        <div class="module">
            <a id="Absolute & Relative Images">
                <h2>2.1 Absolute & Relative Images</h2>
                <p>When providing a URL reference to an image, the pathway can be considered absolute or relative.</p>
                <br>
                <p><strong>Absolute</strong> pathways are used when sourcing an image from an external webserver (I.e a different website). An absolute pathway is the full URL that would be displayed in a search browser, for example: https://www.examplewebsite.com/image/example_image.png
                <br>Conversely, <strong>relative</strong> pathways refer to images that are from the internal webserver, these pathways exclude the web address, and just contain the path within the site. For example: /image/example_image.png
                </p>
            </a>
        </div>

        <div class="module">
            <a id="Image Formatting">
                <h2>2.2 Image Formatting</h2>
                <p>The style attribute that we have previously used for text elements is also available for images.</p>
                <br>
                <p>Most commonly, the <strong>width:</strong> and <strong>height:</strong> parameters are used to determine the scale of the image in pixels. </p>
                <br>
                <p>Image with styling code example</p>
                <img class="htmlcontent" src="/img/html_content/Example6.png" alt="Example5: Example of an image that has been set with width=1024 and height=1024 using tag attributes.">
            </a>
        </div>

        <div class="module">
            <a id="Buttons">
                <h1>3.0 Buttons</h1>
                <p>Buttons are exceptionally important in web development, as they allowed navigation across a website. There are two primary ways to achieve this in HTML, through URL links, and graphical buttons.</p>
            </a>
        </div>

        <div class="module">
            <a id="URL Tags">
                <h2>3.1 URL Tags</h2>
                <p>The tag &lt;a&gt; defines any content within it as a hyperlink.</p>
                <br>
                <p>The attribute <strong>href</strong> within &lt;a&gt; refers to the returned link that will be presented when the link is pressed.</p>
                <br>
                <p>By placing a paragraph tag &lt;p&gt; within a link tag &lt;a&gt;, we can define a text that can be clicked to return a new webpage. This is beneficial, as the link can be described as any text – not just the URL itself.</p>
                <p>For example:</p>
                <img class="htmlcontent" src="/img/html_content/Example7.png" alt="Example6: Example of a URL link with a alternate description <link description>">

            </a>
        </div>

        <div class="module">
            <a id="Graphical Buttons">
                <h2>3.2 Graphical Buttons</h2>
                <p>As demonstrated above, by encapsulating the <a> tag within <p> allows us to link a paragraph element. You may have intuitively realised that the same could be possible for an image element as well.</p>
                <br>
                <p>Task 2: Create an image and make it link to an external webpage through an absolute URL. Hint: Place an &lt;img&gt; inside the &lt;a&gt; tag.</p>
            </a>
        </div>

        <div class="module">
            <a id="User Input">
                <h1>4.0 User Input</h1>
                <p>HTML contains an assortment of many different user inputs. These range from text, to dates, to checkboxes and file uploads. In this lesson we will explore how users can input forms, and how to save the output at the conclusion of the entry.</p>
                <br>
                <h3>Creating an Input field</h3>
                <p><strong>&lt;input type=”text” id="inputid" name="inputid"&gt;&lt;br&gt;</strong><br>Creates a single line textbox element that a user can enter values into.</p>
                <br>
                <p>With this single tag, we can create an input field. However, we can also assign a label to the field, to give user’s a description of what to enter such as their name, password, address etc. This is achieved through the following.</p>

                <p><strong>&lt;label for=" inputid"&gt;Input ID Field:&lt;/label&gt;&lt;br&gt;</strong><br>This line of code will label the input box as “Input ID Field:”.</p>
                <br>
                <p>This line of code will label the input box as “Input ID Field:”.</p>

                <br>
                <h3>Creating a Submission Button</h3>
                <p><strong>&lt;input type="submit" value="Submit">&gt;</strong><br>The input type submit creates a button that will save data to a form handler. For the submission to work, it requires the following:</p>
                <br>
                <p>Firstly, all input data must be encapsulated within a &lt;form&gt; tag. Moreover, this form must have the attribute "action" which provides a script that processes the data. JavaScript can be used to create this handling script, to learn a basic understanding of JavaScript, see our lesson here: <strong>Insert Link Here</strong></p>
                <br>
                <p>Thus, we can create a submission form with the following:</p>
                <img class="htmlcontent" src="/img/html_content/Example8.png" alt="Example7: Example of a first and last name submission input fields, with a submit button.">

            </a>
        </div>

        <div class="module">
            <a id="Website Styling">
                <h1>5.0 Website Styling</h1>
                <p>HTML has many purposes when developing the aesthetic of the website. However, Cascading Style Sheets (CSS) is a vastly more robust and powerful tool for designing the layout and look of a website. To learn CSS, you can find out lesson here: <strong><a href="/css">CSS Lesson</a></strong></p>
            </a>
        </div>
<body>

% include templates/tailer.tpl