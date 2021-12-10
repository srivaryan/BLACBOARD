function submit_btn(){
    console.log("hi");
    var mail=document.getElementById("mail");
    if (mail.value==""|| pswrd.value==""){
        alert("Please fill in required field");
        var link=document.createElement('div');
        link.id="link_register";
        link.innerHTML="Not registered yet? Click <a href=\"register.html\"><span style=\"color:blue\">here</span></a>";
        document.getElementById("details_box").appendChild(link);

        
    }
    else{
        
        var btn=document.getElementById("btn_hidden")
        console.log(btn);
        btn.click();
    }
    

}