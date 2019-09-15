function login() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('passw').value;

    let data = {
        username: username,
        password: password
    };

    $.ajax({
        url: "http://127.0.0.1:5000/login",
        type: "post",
        contentType: "application/json",
        context: document.body,
        success: function (res) {
            if (res['result']){
                window.location.replace('http://127.0.0.1:5000/home');
            }
        },
        data: JSON.stringify(data)
    });
}


