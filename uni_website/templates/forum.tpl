% include templates/header.tpl

<div class = "forumcontent" style="margin-top:120px">

    <h1 class = "title"  > Discussion Forum </h1>
    % if isMuted:
        <p style="color:red; text-align:center">YOU ARE CURRENTLY MUTED</p>
    % end
    <div class = "create-post">
        <form action= "/post" method = "GET" >
            <input class = "create-button"  type = "submit" value = "Create Post"/>
        </form>
    </div>
    <div class = "search-post">
        <div class ="search">
            <form action = "/search" method = "POST">
                <input class = "search-text" name = "search" type = "text" placeholder="Search" />
                <input class= "search-button" type= "submit" value = "Submit"/>
            </form>
        </div>

    </div>

    <table class = "discussionTable">
        <tbody>
            <tr>
                <th><h2>Question</h2></th>
                <th class = "response"><h2>Number of response</h2></th>
                <th><h2>Date</h2></th>
            </tr>
            % for i in rows:
                <tr>
                    <th><a href = "/question?id={{i[0]}}"> {{i[4]}}</a></th>
                    <td>{{i[5]}}</td>
                    <td> {{i[2]}}</td>
                </tr>
            % end



        </tbody>
    </table>
<div style="margin-top:260px">
</div>

% include templates/tailer.tpl
