function register(){
    let username = document.getElementById("username").value;
    let password = document.getElementById("passw").value;
    let second_password = document.getElementById("check_passw").value;

    if (password != second_password){
        {{ flash('Senhas não são iguais') }}
    }

    let data = {
        username: username,
        password: password
    };

     $.ajax({
        url: "http://127.0.0.1:5000/register",
        type: "post",
        contentType: "application/json",
        context: document.body,
        success: function (res) {
            if (res['status']){
                window.location.replace('http://127.0.0.1:5000/home');
            }
        },
        data: JSON.stringify(data)
    });


}

function back(){
    window.location.replace('http://127.0.0.1:50000/login');
}