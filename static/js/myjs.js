var userRegistered = Number($('#hidden2').text());
if(userRegistered) $("#btn1").prop('value', 'Deregister');


$(document).ready(function(){
    var userRegistered = Number($('#hidden2').text());
    if(userRegistered) $("#btn1").prop('value', 'Deregister');
    else $("#btn1").prop('value', 'Register');
    
    $("#btn1").show();

    console.log(userRegistered);
    $("#btn1").click(function () {
        console.log("Aman");
        var x = $('#hidden').text();
        console.log(userRegistered);
        data_passed = {pk: x};
        if(userRegistered == 0){
            console.log("In");
            $("#btn1").prop('value', 'Deregister');
            userRegistered = 1;
            alert("Successfully Registered.");
            $.get('/registeration/user_register/', data_passed, function () {
                        console.log("Received Response");
                });


        }
        else{
            console.log("Out");
            $("#btn1").prop('value', 'Register');
            userRegistered = 0;
            alert("Successfully Deregistered.");
            $.get('/registeration/user_deregister/', data_passed, function () {
                    console.log("Derigiser Received Response");
            });

        }

        // data_passed = {pk: x};
        // $.get('/registeration/user_register/', data_passed, function () {
        //             alert("Successfully Registered.");
        //         });

        // $("#btn1").val("");
        // $("#btn1").attr("id", "btn2");


        // $("#btn2").unbind("click").click(function () {
        //     var x = $('#hidden').text();
        //     console.log(x);

        //     data_passed = {
        //             pk: x
        //         };
                // $.get('/registeration/user_deregister/', data_passed, function () {
                //     alert("Successfully Deregistered.");
                // });

        //     $("#btn2").val("hey hey");
        //     $("#btn2").attr("id", "btn1");    

    // }
    // );

    
});

});

