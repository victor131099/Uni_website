 % include templates/header.tpl

 <div style="margin-top:120px; padding:2%">
 <div class = "questioncontent">
    % if isMuted:
        <p style="color:red; text-align:center">YOU ARE CURRENTLY MUTED</p>
    % end
    <h1 class = "title"> {{question_info[4]}}</h1>
    <div class= "main-creator">
        <span class = "author" id = "main-author"> {{question_info[7]}} </span>
        <span class = "time" id= "main-time"> - {{time_str}}</span>
        <div>
            <p> {{question_info[3]}}</p>
        </div>
    </div>
    <ul class = "comments">
        <form action= "/comment" method = "POST">
            <input type="text" name = "comment" placeholder="Add Comment">
            <input class = "button-reply" type="submit" value="Reply">
        </form>
        % if comments == None:
            <h1> 0 responses</h1>
        % else:
            <h1> {{len(comments)}} responses</h1>
            % for comment in comments:
                <li class = "comment-component">
                    <div class = "comment-body">
                        <div class= "publisher">
                            <span class = "author"> {{comment[6]}}</span>
                            <span class = "time"> - {{comment[3]}}</span>
                        </div>
                        <div class = "content"> {{comment[4]}}</div>
                    </div>
                </li>
            %end
        % end

    </ul>
</div>
</div>

% include templates/tailer.tpl