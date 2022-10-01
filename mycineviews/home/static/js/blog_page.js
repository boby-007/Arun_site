let blogIndexDivs= document.querySelectorAll(".blog-index-item");
for (let i = 0; i <= blogIndexDivs.length; i++) {
if(i%2==1){
    blogIndexDivs[i].classList.add("row-reverse-class")
}else{
    continue;
}

}