% include templates/header.tpl

<div class="section" id="top">
    <h1>Web Frameworks</h1>
    <img src="img/frameworks_webapps.png"> <br>
    <i>Imaged sourced from <a href="https://www.scnsoft.com/blog/web-application-framework">ScienceSoft</a></i>
</div>
<div class="frameworks" id="content">
    <h2>What is a Web Application Framework?</h2>
    <p>A web application framework is a software framework that aids in the process of developing web apps, web APIs and other web services.</p>
    <h2>Why you need a Web Application Framework</h2>
    <p>A web application framework provide a fast and easy method to develop web applications. Many of them provide libraries which promote reusable code to get your projects running quickly.</p>
    <h2>Types of Web Application Frameworks</h2>
    <h3>Client-Side Frameworks</h3>
    <img src="img/frameworks_react_v_angular.png"> <br>
    <i>Image sourced from <a href="https://blog.cloudboost.io/fast-introduction-to-react-for-angular-2-4-developers-4465e1621cf7">Vladimir Tolstikov</a></i>
    <p>Client-side frameworks are used to develop the "front-end" of a web application, most often used in the display through JavaScript, which is run on the browser to ensure that the web application is usable on different platforms, browsers and devices. Popular client-side frameworks include <b>Angular</b>, designed by Google and <b>React</b>, developed by Facebook.</p>
    <h3>Server-Side Frameworks</h3>
    <p>Server-side frameworks (a.k.a. the "back-end" of a web application) make it easier to develop, maintain and scale web applications. They can provide libraries which make communication with the HTTP protocol simpler.
This website uses Bottle for Python as the back-end framework. However, more commonly used and popular frameworks include <b>Django</b> (Python), <b>Flask</b> (Python), <b>Ruby on Rails</b> (Ruby) and <b>Express</b> (Node.js/JavaScript)</p>
    <h2>Single-page applications and Multi-page applications</h2>
    <img src="img/frameworks_spa-vs-mpa.png"> <br>
    <i>Image sourced from <a href="https://yalantis.com/blog/single-page-apps-vs-multiple-page-apps/">Daryna Pukha</a></i>
    <p>A single-page application is a web application that dynamically rewriting the page so that new information can be displayed and changed without reloading the page, this results in a web application that behaves like a native application. Examples of this are Facebook, YouTube, Gmail, GitHub and Netflix. On the other hand, multi-page applications are the more traditional websites where users must interact with the website to load a new page and display new information. Multi-page applications are perfect for read-only websites which purely present information to users.</p>
    <h2>Web Application Framework Architectures</h2>
    <h2>Model View Controller (MVC) Architecture</h2>
    <p>MVC in web development is a software design pattern which divides an application into three components: Model, View and Controller. The result of three components is a clear model to separate front-end development from back-end development while also being easily scalable.</p>
    <img src="img/frameworks_mvc.svg"> <br>
    <i>Image sourced from <a href="https://commons.wikimedia.org/wiki/File:MVC-Process.svg">Wikimedia Commons</a></i>
    <h3>Model</h3>
    <p>The model component controls the data flow, rules and logic of the application.</p>
    <h3>View</h3>
    <p>The view component is the presentation of the data to users i.e. the graphical user interface (GUI).</p>
    <h3>Controller</h3>
    <p>The controller handles user input and interaction with the view. User inputs are sent to the model and processed by the model, sent back to the controller, and finally the end result is sent to the view.</p>
</div>

% include templates/tailer.tpl