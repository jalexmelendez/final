//Global components
//Achievements component

//DEPRECIATED FUNCTION
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
            <p><a onClick={achievementComponents()} class="uk-button">Fetch achievements</a></p>
        </div>
        <div class="uk-card-footer">
            <a class="uk-button uk-button-text">Total achievements to get: 10</a>
        </div>
    </div>
const renderTarget = document.getElementById('achievements');
ReactDOM.render(achievementsMainContainer, renderTarget);
}

function achievementComponents() {
    console.log('executed');
    let achievementObject = dataToRender.map((data) =>
    <div class="uk-card uk-card-default uk-card-hover">
        <div class="uk-card-header">
            <div class="uk-grid-small uk-flex-middle" uk-grid>
                <div class="uk-width-auto">
                    <img class="uk-border-circle" width="40" height="40" src="https://png.pngtree.com/png-vector/20190819/ourlarge/pngtree-gold-trophy-icon-trophy-icon-winner-icon-png-image_1694365.jpg"></img>
                </div>
                <div class="uk-width-expand">
                    <h3 class="uk-card-title uk-margin-remove-bottom">Achievement</h3>
                    <p class="uk-text-meta uk-margin-remove-top"><time key={data.toString()} datetime="2016-04-01T19:00">{data}</time></p>
                </div>
            </div>
        </div>
    </div>
    );
    const compTarget = document.getElementById('componentsTarget');
    ReactDOM.render(achievementObject, compTarget);
}

function topuserComponents() {
    console.log('executed');
    let achievementObject = dataToRender.map((data) =>
    <div class="uk-card uk-card-default uk-card-hover">
        <div class="uk-card-header">
            <div class="uk-grid-small uk-flex-middle" uk-grid>
                <div class="uk-width-auto">
                    <img key={data.profile_pic.toString()} class="uk-border-circle" width="40" height="40" src={data.profile_pic}></img>
                </div>
                <div class="uk-width-expand">
                    <h3 key={data.score.toString()} class="uk-card-title uk-margin-remove-bottom">Score: {data.score} </h3>
                    <p key={data.username.toString()} class="uk-text-meta uk-margin-remove-top"><time datetime="2016-04-01T19:00">Username: {data.username}</time></p>
                </div>
            </div>
        </div>
    </div>
    );
    const compTarget = document.getElementById('usercomponentsTarget');
    ReactDOM.render(achievementObject, compTarget);
}

function renderQuestions() {
    let questionObj = dataToRender.map((data, index) => 
    <div class="uk-margin">
        <span>
            <p key={operator.toString()}>
                <strong> {index +1}.- </strong>
                <span key={data['1'].toString()}>{data['1']}</span>
                <span> {operator} </span>
                <span key={data['2'].toString()}>{data['2']}</span>
                <span> = </span>
                <input key={data.ans.toString()} data-set={data.ans} class="uk-input uk-form-width-small test-answer" type="text" placeholder="Your answer"></input>
            </p>
        </span>
    </div>
    );
    const questionTarget = document.getElementById('questionTarget');
    ReactDOM.render(questionObj, questionTarget);
}

function renderAnswers() {
    let answerstable = 
    <table class="uk-table">
    <caption>Test results</caption>
    <thead>
        <tr>
            <th>Your answer</th>
            <th>Correct answer</th>
            <th>Points</th>
        </tr>
    </thead>
    <tbody>
        <Results />
    </tbody>
</table>;
const compTarget = document.getElementById('questionTarget');
ReactDOM.render(answerstable, compTarget);
}

function Results() {
        let answers = dataToRender.map((data) =>
        <tr>
            <td key={data.user.toString()}>{data.user}</td>
            <td key={data.correct.toString()}>{data.correct}</td>
            <td key={data.evaluation.toString()}>{data.evaluation == true ? '+1' : '0'}</td>
        </tr>);
        return answers;
}