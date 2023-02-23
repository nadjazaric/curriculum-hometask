function countLikes() {
  var likesIcon = document.querySelector(".noLikes");
  var noLikes = document.querySelector(".noLikes b");
  count = 0;
  likesIcon.addEventListener('click', function () {
    count = parseInt(noLikes.textContent) + 1;
    noLikes.textContent = count;
  });
}

function revealComments() {
  var commentIcon = document.querySelector(".noComments")

  commentIcon.addEventListener('click', function () {
    document.querySelector(".addComment").style.display = "block";
  });
}



fetch('/static/data/comments.json')
  .then(response => response.json())
  .then(data => {
    const postsBody = document.getElementById('posts-tbody');
    counter = 0;
    for (let i = 0; i < data.length; i++) {
      const currPost = data[i];
      counter++

      let idElement = document.createElement('td');
      idElement.innerText = counter;

      let userName = document.createElement('td');
      userName.innerText = currPost[0];

      let date = document.createElement('td');
      date.innerText = currPost[1];

      let comment = document.createElement('td');
      comment.innerText = currPost[2];

      let rowElement = document.createElement('tr');
      rowElement.append(idElement, userName, date, comment);

      postsBody.append(rowElement);

    }
  })
