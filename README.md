# Project: Kibo Blog

Blogs are regularly updated websites that provide insight into a certain topic. Much like social media platforms, blogs allow people to share their thoughts and experiences with others. Given the active comment sections, they enable people to interact with one another and build relationships based on shared interests. Essentially, blogs have become a social platform for themselves.

In this project, you'll build a Blog Post page. The focus of the project is on post-interaction, specifically comments and like.

As in any social network, the comments section usually includes the content of the comment, the post date, and user information.

## Your Task

The basic design of a Blog Post page includes the Post title, Post content, interaction section (like, comment), and comment section.
Your task is to design an "Add comment" block for a post and to show all comments on a "Recent comments" page.
You are also supposed to have a counter of comments.

Each post can be liked, so make sure you count the likes too.

Finally, you should protect your blog from spam and detect spam triggers. Spam trigger words are keywords or phrases that web providers see as red flags. You’ll often find these words in emails that people mark as spam. You will need to create a spam filter that will catch suspicious words and phrases associated with scams, gimmicks, promises, gifts, and similar. Building a function that will prevent posting such content is of crucial importance for making a safe and trusted website.

Building these features requires you to apply both frontend (HTML, CSS, JavaScript) and backend (Python and Flask) skills.
The design of the blog should be modern, minimalistic, and responsive.

## Starter Code

As you have completed the Web foundation course, you are expected to have mastered HTML and CSS, and that's why we won't focus on these technologies that much. In this regard in the starter code you will find:

- home.html with the majority of the code written
- style.css with the majority of the code written
- the 'CSS' and 'webfonts' folders with font awesome files that are required to use fa-icons for like and comment action.
- spam.json files with the list of spam words
- img folder with all the images you will need

The rest of the files like script.js and app.py are (mostly) empty. Feel free to add other files (such as recent.html) as you build out the blog.

## Steps

### Wire up all the files

Make sure that all of your html, css, js and img files are linked and connected.
Handle them as a static files.
Remember, .css, .js and images are static files, so it is recommended to use url_for() function to handle them.

### Render the homepage

In the app.py you should write a home() function to render a homepage in route "/"
Take some time and get familiar with the existing code, use inspect element feature to see the already build blocks on the page, and understand its layout.
At this point, the interactions won't work, but it will have content!

### Hands on Javascript

- To comment users have to click on the comment icon which will reveal the comment section. Create a function that will display the <section class="addComment"> on click.
- Users can like a post. The post already has 15 likes. By clicking on the heart icon, the user increases the number of likes by 1. User can like a post as many time he/she wants. 

### Add comments 
To add a comment user should enter his/her name and the content in the form fields, and click the Add comment button.
  
- Extend the def home() function and write code to request users' input from a form.
- Each comment is saved as an item in the Python list.
- Don't forget to add a post date to each comment. Post date should be written in the format '%Y-%m-%d'

### Show recent comments on homepage
  
For each comment, the following information is shown on the page:
  - User profile default icon
  - User name
  - Comment Title (first 20 characters of the comment content)
  - Date
  - Comment content 

You should first prepare the HTML tags and then use Jinja2 to pass in the values.
Make sure the comment list is given in render_template() function.

### Count comments

Total number of comments should be shown next to the comment icon.

### Create recent.html
 
You should have everything you need for the recent.html page! Make sure that header, footer, and main section are the same as in home.html, and then create a table to show: the ordinal number, user's name, comment content, and date.

If the post does not have any comments yet, print the "No comments to show" message.

You should also add some css style to make your table look modern.

### Write the spam checker
  
The list of potential spam words is saved in the spam.json file.
  
Your job is to open the file, list the phrases, and check if the comment content contains any of these words.
If it does, the comment is rejected.
The program should also print the response in a form of <p> "Message looks like spam. Please rephrase it" </p>.
Help the user understand what he did wrong by listing all the suspicious words that should not show up in a comment. (list the words as an unordered list).
  
**Hints**:

- You can manipulate the style of an element with document.querySelector('').style property of DOM
- Use strftime("%Y-%m-%d") metod to format the date
- Requested data are sent with POST method, so make sure you check  if request.method == "POST"
- Use Flask flash() method to show the spam warning. (https://rb.gy/zxfrov)

## Expected Results

### Homepage with open comment section

![Home page with open add comments](https://github.com/nadjazaric/curriculum-hometask/blob/main/Homepage-full%20content.png?raw=true)

### Homepage with spam filter warning

![spam filter](https://github.com/nadjazaric/curriculum-hometask/blob/main/Homepage%20with%20warning%20for%20spam.png?raw=true)

### Recent comments page

![recent filter](https://github.com/nadjazaric/curriculum-hometask/blob/main/Recent%20comments.png?raw=true)

The design of the blog should be modern, minimalistic, and responsive.

## Bonus Task

There's tons of further ideas you could add to your blog if you have more time and want to make the project even cooler.

* Provide users an option to delete the comment.
* Enable user an option to choose their user image (avatar). This will require adding nore avatar images to 'img' folder OR Make a random avatar choice - add more user avatar images and randomly assign them to a comment.
  * Add search option to table of recent comments. User should input a search term in input field and search for that term in comment content.
  


There's tons more features that you could try to add, if you want. Be creative!
