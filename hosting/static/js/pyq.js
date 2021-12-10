// var inp_search=document.getElementById("search_bar");
// inp_search.addEventListener("onclick",function(e){
//     console.log(e);
// })
function search(){
    var key=document.getElementById("search_bar");
    var book=document.createElement("div");
    
    let year="2021";
    let link="http://www.frymybheja.thankyou.com";
    book.className="item";
    book.innerHTML="<p>Course: "+key.value+"</p><p>Year: "+year+"</p>";
    book.innerHTML+="<p>To view/donload the question paper, click <a href=\""+link+"\" style=\"font-weight:bold; text-decoration: none; color: white\">here</a></p>";
    document.getElementById("result").appendChild(book);
}

