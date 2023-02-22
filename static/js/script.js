
var likesIcon = document.querySelector(".noLikes");
var noLikes = document.querySelector(".noLikes b");
var commentIcon = document.querySelector(".noComments")

count = 0;
likesIcon.addEventListener('click', function(){
  count = parseInt(noLikes.textContent) + 1;
  noLikes.textContent = count;
});

commentIcon.addEventListener('click', function(){
   document.querySelector(".addComment").style.display = "block";
  });

  
