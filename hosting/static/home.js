
function toggle_sidebar(){
    var side_bar=document.getElementById("side_navigation");
    if(side_bar.style.display=="none"){
        side_bar.style.display="block";
    }
    else{
        side_bar.style.display="none";
    }
    
    console.log(side_bar.style.vosibility);
}

    // side_bar.style.visibility="no"