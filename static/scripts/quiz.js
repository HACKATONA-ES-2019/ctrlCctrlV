
function load_quiz(quiz_title){
    let url = "http://127.0.0.1:5000/quiz/" + quiz_title.replace(' ', '_');
    window.location.replace(url);
}

function change_color(button){
    let value = button.getAttribute('data-correct');

    if (value == 0){
        button.style.background = "#e70000";
    }
    else{
        button.style.background = "#89fe96";
    }

}