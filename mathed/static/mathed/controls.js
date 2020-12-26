// Global variables
const userInSession = globalDir['user'];
let dataToRender = []
// System storage
// Controller
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('gotoProfile').addEventListener('click', function() {
        profileCont.style.display = 'block';
        achievementsCont.style.display = 'none';
        topUsersCont.style.display = 'none';
        practiceCont.style.display = 'none';
        renderProfile();
    })
    document.getElementById('render_ach').addEventListener('click', function() {
        profileCont.style.display = 'none';
        achievementsCont.style.display = 'block';
        topUsersCont.style.display = 'none';
        practiceCont.style.display = 'none';
        renderAchievements();
    })
    document.getElementById('renderTop_users').addEventListener('click', function() {
        profileCont.style.display = 'none';
        achievementsCont.style.display = 'none';
        topUsersCont.style.display = 'block';
        practiceCont.style.display = 'none';
        topusers();
    })
    document.getElementById('render_test_ui').addEventListener('click', function() {
        profileCont.style.display = 'none';
        achievementsCont.style.display = 'none';
        topUsersCont.style.display = 'none';
        practiceCont.style.display = 'block';
        testUi();
    })
})
// Switcher

function asyncSwitcher(option) {
    console.log('option');
}

// Functions profile
function renderProfile() {
    //alert(userInSession);
}

// Functions achievements
function renderAchievements() {
    apiEngine('achievements');
    //achievementComponents();
}


// Functions leaderboard
function topusers() {
    apiEngine('top_by_score');
}


// Function start test
function startSum() {
    apiEngine('sum');
    operator = '+';
}

function startSub() {
    apiEngine('sub');
    operator = '-';
}

function startMult() {
    apiEngine('multi');
    operator = '*';
}

// Init test
function initExam() {
    document.getElementById('questionTarget').innerHTML = '';
    document.getElementById('testControls').style.display = 'block';
    renderQuestions();
}

// Functions submit test
function testSubmit() {
    let dataSet = document.getElementsByClassName('test-answer');
    let answers = [];
    for(i=0;i<dataSet.length;i++) {
        let correct = dataSet[i].getAttribute('data-set');
        let usrAnswer = dataSet[i].value;
        if (usrAnswer.length == 0) {
            let format = {'user': 0, 'correct': correct}
            answers.push(format);
        }
        else {
            let format = {'user': parseInt(usrAnswer), 'correct': correct}
            answers.push(format);
        }
    }
    testApiEngine(answers);
    console.log(answers);
    document.getElementById('testControls').innerHTML = '';
    document.getElementById('finishRevision').style.display = 'block';
    return 0 ;
}