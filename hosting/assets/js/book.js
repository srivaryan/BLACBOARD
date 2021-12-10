function search(){
    var key=document.getElementById("search_bar");
    var book=document.createElement("div");
    
    let author="John J D";
    book.className="item";
    book.innerHTML="<p>Book: "+key.value+"</p><p>Author: "+author+"</p><p>Lent By: "+"abcd"+"</p>";
    book.innerHTML+="<p>To borrow the book, click <span onclick=\"book()\" style=\"font-weight:bold; cursor:pointer;\">here</span></p>"
    document.getElementById("result").appendChild(book);
}

function book(){
    if(document.querySelector(".alert")==null){
        var alert=document.createElement("div");
    alert.className="alert";
    alert.innerHTML="<p>Do you want to borrow the book?</p>";
    var yes=document.createElement("button");
    yes.setAttribute("type","button");
    yes.setAttribute("onclick","close_box()");
    
    console.log(yes);
    yes.innerHTML="Yes";
    
    var no=document.createElement("button");
    no.innerHTML="No";
    no.setAttribute("type","button");
    no.setAttribute("onclick","close_box()");
    
    alert.appendChild(yes);
    alert.appendChild(no);
    document.body.appendChild(alert);

    }
    else{
        var box=document.querySelector(".alert");
        box.style.display="block";
    }
    
    
    // confirmation();

}

function close_box(){
    
    var box=document.querySelector(".alert");
    box.style.display="none";
}
// function confirmation(){
//     var yes=document.querySelector(".button yes");
//     yes.addEventListener('click',function(){
//         var box=document.querySelector(".alert");
//         box.style.display="none";
//     })
// }

