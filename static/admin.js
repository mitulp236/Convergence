function show_password(id) {
    al
    var pass = document.getElementById('camp_password' + id);
    if (pass.textContent == "********") {

        var valid_password = prompt("Enter the password to see password :");
        if (valid_password == null) {
            alert("Invalid Password!");
        } else {
            $.ajax({
                data: {camp_id: id, validatepassword: valid_password},
                type: 'POST',
                url: '/show_camp_password'
            })
                .done(function (data) {
                    if (data.status == "success") {
                        pass.textContent = data.camppass;
                    } else {
                        alert("Invalid Password!");
                    }
                })
        }


    } else {
        pass.textContent = "********";
    }

}


