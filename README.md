# Project: Kibo Blog

Blogs are regularly updated websites that provide insight into a certain topic. Much like social media platforms, blogs allow people to share their thoughts and experiences with others. Given the active comment sections, they enable people to interact with one another and build relationships based on shared interests. Essentially, blogs have become a social platform unto themselves.

In this project, you'll build a Blog Post page. The focus of the project is on post interaction, specifically comment and like.

As in any social network, comments section usually include: content of the comment, post date and user information.

## Your Task

The basic design of a Blog Post page includes Post title, Post content, interaction section (like, comment) and comment section.
Your task is to design an "Add comment" block for a post, and to show all comments on a "Recent comments" page.
You are also supposed to have a counter of comments.

Each post can be liked, so make sure you count the likes too.

Finally, we don't want any spam content in the comments, so, building a funtion that will prevent posting such content is of crucial importance for making a safe and trusted website.

Building these features require you to apply both frontend (HTML, CSS, JavaScript) and backend (Python and Flask) skills.
The design of the blog should be modern, minimalistic, and responsive.

## Starter Code

As you have succesfully completed the Web foundation course, you are expected to have mastered HTML and CSS, and that's is why we wont focus on these technologies that much. In this regard in the strater code you will found:

- home.html with the majority of the code written
- style.css with the majority of the code written
- the 'css' and 'webfonts' folders with fontawesome files that are required in order to use fa-icons for like and comment action.
- spam.json files with the list of spam words
- img folder with all the images you will need

The rest of the files like script.js and app.py are (mostly) empty. Feel free to add other files (such as
recent.html) as you build out the blog.

## Steps

### Wire up all the files

Make sure that all of your html-css-js-img files are linked and connected.
Remember, ,css, .js and images are static files, so it is recommended to use url_for() function to handle them.

### Render the homepage

In the app.py you should write a home() function to render a homepage in route "/"
Take some time and get familiar with the existing code, use inspect element feature to see the already build blocks on page, and understand its layout.
At this point the interactions won't work, but it will have content!

### Hands on Javascript

- To make a comment users have to click on comment icon which will reveal the comment section. Create a function that will display the <section class="addComment"> on click.
- Users can like a post. The post already has 15 likes. By clicking on the heart icon, user increases the number of likes by 1. User can like a post as many time he/she wants. 

### Add comments 
To add a comment user should enter his/her name and the content in the form fields, and click the Add comment button.
  
- Extend the def home() function and write code to request users' input from form.
- Each comment is saved as a item in Python list.
- Don't forget to add a post date to each comment. Post date should be written in format '%Y-%m-%d'

### Show recent comments on homepage
  
For each comment, following information is shown on the page:
  - User profile default icon
  - User name
  - Comment title (first 20 characters of the comment content)
  - Date
  - Comment content 

You should first prepare the HTML tags and then use Jinja2 to pass in the values.  

### Create recent.html
 
You should have everything you need for the recent.html page! Make sure that header, footer and main section are the same as in home.html and then create a table to show: ordinal number, user name, comment content and date.

If the post does not have any comments yet, make sure to print the "No comments to show"


### Handle selecting with JavaScript

The goal of your JS code is to add and remove the `selected` class from different gallery items when clicked, so that a different item is styled as the 'selected' item.

First, add JavaScript to listen for a click on an item. When the item is clicked, run `console.log("clicked")` so that you can tell that the item was clicked. Test this code.

Update the code in your event handler to change which item is selected. It should remove the `selected` class from the currently selected element, and add the `selected` class to the element that was clicked.

Once you have one gallery item selecting on click, you can add the same event listener to the rest of your items.

Test that clicking on an item makes it the selected element, and unselects whichever element was selected before.

**Hints**:

- You can find the currently selected element with `document.querySelector('.selected')`
- You can use `element.classList.remove('selected')` and `element.classList.add('selected')` to add and remove the class
- You can add an listener for click events to an element with `element.addEventListener('click', () => { console.log('clicked')})`

JavaScript is new and tricky! Feel free to ask for help with this part of the project.

## Expected Results

Every content gallery site will look different, but here are some examples that demonstrate the feature in question:

* An [example of an image gallery](https://mdn.github.io/learning-area/javascript/building-blocks/gallery/) from MDN, and [instructions on how to build it](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Image_gallery)
* As linked above, here's [Unsplash's search result page](https://unsplash.com/s/photos/puppy)

You probably have a news blog you read every day or an account on at least one social network like Facebook, Instagram, YouTube or Linkedin, so you are quite familiar with how interaction with content usually works. Just in case you have doubts, take a look at some of the examples here:

- [Facebook](shorturl.at/afBKU)
- [Linkedin](shorturl.at/deEM9)
- [Blog](https://yyj.be/mfbSd) (scroll to bottom to see the comment section)


The design of the blog should be modern, minimalistic, and responsive.

## Bonus Task

There's tons of further ideas you could add to your gallery if you have more time and want to make the project even cooler.

* Add more content. Galleries are more fun when there is more stuff to browse.
* Style the cursor, hover state, and the gallery cards or list items to make the gallery more appealing.
* Add a 'load more' button that shows more content. One way to do this is to have that content hidden at the start, then have the button remove a class that was hiding the content.
* Style the focused item as a modal. See  https://codeshack.io/pure-css3-modal-example/ for a suggestion on how you could style this.
* If you have videos or audio, play them when the item is focused, and stop playing when it gets unfocused.

There's tons more features that you could try to add, if you want. Be creative!
