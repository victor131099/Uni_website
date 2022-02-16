% include templates/header.tpl

<div style="margin-top:120px; padding:2%">
<div class="post-container">
    <form action="/post" method = "POST">
        % if isMuted:
            <p style="color:red; text-align:center">YOU ARE CURRENTLY MUTED</p>
        % end
        <input type="text" class= "question-title" name="title" placeholder="Title">

        <textarea id="description" name="description" placeholder="Description" style="height:200px"></textarea>

        <input type="submit" value="Submit">
    </form>
</div>
</div>

% include templates/tailer.tpl