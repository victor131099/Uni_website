% include templates/header.tpl

<div class="section" id="top">
    <h1>Admin control panel</h1>
    <p>This page allows you to mute or remove members and manage the discussion forum. Click on the links below to jump straight into a section.</p>
    <br>
    <a href="#AddMembers" class="button">Add Members</a>
    <a href="#RemoveMembers" class="button">Remove Members</a>
    <a href="#MuteMembers" class="button">Mute Members</a>

</div>
<div class="section" id="AddMembers">
    <h2>Add Members</h2>
    <div class="underline"></div>
    <div class="article-container">
        <article>
                <div class ="search">
                    <form action="/admin" method="post">
                        <input type="hidden" name="requestType" value="add">
                        <input type = "text" name="fname" placeholder="First Name" />
                        <input type = "text" name="lname" placeholder="Last Name" />
                        <input type = "text" name="email" placeholder="Email" />
                        <input type = "text" name="username" placeholder="Username" />
                        <input type = "password" name="password" placeholder="Password" />
                        <input type= "submit" value = "Submit"/>
                    </form>
                </div>
        </article>
    </div>
</div>

<div class="section" id="RemoveMembers">
    <h2>Remove Members</h2>
    <div class="underline"></div>
    <div class="article-container">
        <article>
            <table class = "adminTable">
                <tbody>
                    <tr>
                        <th><h2>Member Name</h2></th>
                        <th><h2>Remove</h2></th>
                    </tr>
                    % for i in rows:
                        <tr>
                            <th><a>{{i[0]}}</a></th>
                            <td><form action="/admin" method="post">
                                <input type="hidden" name="requestType" value="remove">
                                <input type="hidden" name="username" value={{i[0]}}>
                                <input type= "submit" value = "Remove"/>
                            </form></td>
                        </tr>
                    % end
                </tbody>
            </table>
        </article>
    </div>
</div>

<div class="section" id="MuteMembers">
    <h2>Mute Members</h2>
    <div class="underline"></div>
    <div class="article-container">
        <article>
            <table class = "adminTable">
                <tbody>
                    <tr>
                        <th><h2>Member Name</h2></th>
                        <th><h2>Is Muted?</h2></th>
                        <th><h2>Toggle Mute</h2></th>
                        <!--<th><h2>Date</h2></th> -->
                    </tr>
                    % for i in rows:
                        <tr>
                            <th><a>{{i[0]}}</a></th>
                            <td>{{i[1]}}</td>
                            <td><form action="/admin" method="post">
                                <input type="hidden" name="requestType" value="mute">
                                <input type="hidden" name="username" value={{i[0]}}>
                                <input type="hidden" name="isMuted" value={{i[1]}}>
                                <input type= "submit" value = "Toggle Mute"/>
                            </form></td>
                        </tr>
                    % end
                </tbody>
            </table>
        </article>
    </div>
</div>

% include templates/tailer.tpl
