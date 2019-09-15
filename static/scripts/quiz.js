
function load_quiz(quiz_title){
    let url = "http://127.0.0.1:5000/quiz/" + quiz_title.replace(' ', '_');
    window.location.replace(url);
}