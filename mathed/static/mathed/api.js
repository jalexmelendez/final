//Data to fetch

//API 
function apiEngine(option) {
    let csrftoken = getCookie('csrftoken');
    fetch(`/api`, {
        method: 'POST',
        headers: { "X-CSRFToken": csrftoken },
        body: JSON.stringify({'option':option, 'user': userInSession}),
        credentials: "same-origin"
    })
    .then(function(response) {
        return response.json();
    })
    .then(response => {
        dataToRender.splice(0, dataToRender.length);
        console.log(response);
        pushData(response);
    })
}

function pushData(response) {
    for (i=0;i<Object.keys(response).length;i++) {
        if (filterApiData(response[i]) != false) {
            dataToRender.push(response[i]);
        }
    }
}

function filterApiData(response) {
    switch(response) {
        case "": return false; break;
        case "None": return false; break;
        case "none": return false; break;
        case false: return false; break;
        case undefined: return false; break;
        default: return true;
    } 
}

//Test API
function testApiEngine(answers) {
    let csrftoken = getCookie('csrftoken');
    fetch(`/submit`, {
        method: 'POST',
        headers: { "X-CSRFToken": csrftoken },
        body: JSON.stringify({'data':answers, 'user': userInSession}),
        credentials: "same-origin"
    })
    .then(function(response) {
        return response.json();
    })
    .then(response => {
        dataToRender.splice(0, dataToRender.length);
        console.log(response);
        pushData(response);
        renderAnswers();
    })
}

//CSRF TOKEN GENERATOR
// https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}