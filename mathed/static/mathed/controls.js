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

// Functions profile
function renderProfile() {
    //alert(userInSession);
}

// Functions achievements
function renderAchievements() {
    achievementsTemplate();
    apiEngine('achievements');
}

// Functions leaderboard
function topusers() {
    //alert('top');
}

// Functions practice
function testUi() {
    //alert('ui');
}