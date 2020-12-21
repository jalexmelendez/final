//Global components
//Achievements component
function achievementsTemplate() {
    let achievementsMainContainer = 
    <div class="uk-card uk-card-default">
        <div class="uk-card-header">
            <div class="uk-grid-small uk-flex-middle" uk-grid>
                <div class="uk-width-auto">
                    <img class="uk-border-circle" width="40" height="40" src="https://png.pngtree.com/png-vector/20190819/ourlarge/pngtree-gold-trophy-icon-trophy-icon-winner-icon-png-image_1694365.jpg"></img>
                </div>
                <div class="uk-width-expand">
                    <h3 class="uk-card-title uk-margin-remove-bottom">Unlocked achievements</h3>
                    <p class="uk-text-meta uk-margin-remove-top"><time datetime="2016-04-01T19:00">For this first version we have six achievements.</time></p>
                </div>
            </div>
        </div>
    <div id="componentsTarget" class="uk-card-body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
    </div>
    <div class="uk-card-footer">
        <a class="uk-button uk-button-text">Total achievements to get: 10</a>
    </div>
</div>
const renderTarget = document.getElementById('achievements');
ReactDOM.render(achievementsMainContainer, renderTarget);
}

function achievementComponents() {
    let achievementObject = dataToRender.map(() =>
    <article class="uk-comment uk-comment-primary">
    <header class="uk-comment-header">
        <div class="uk-grid-medium uk-flex-middle" uk-grid>
            <div class="uk-width-auto">
                <img class="uk-comment-avatar" src="images/avatar.jpg" width="80" height="80" alt=""></img>
            </div>
            <div class="uk-width-expand">
                <h4 class="uk-comment-title uk-margin-remove"><a class="uk-link-reset" href="#">Author</a></h4>
                <ul class="uk-comment-meta uk-subnav uk-subnav-divider uk-margin-remove-top">
                    <li><a href="#">12 days ago</a></li>
                    <li><a href="#">Reply</a></li>
                </ul>
            </div>
        </div>
    </header>
    <div class="uk-comment-body">
        <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
    </div>
    </article>
    );
    const compTarget = document.getElementById('componentsTarget');
    ReactDOM.render(achievementObject, compTarget);
}