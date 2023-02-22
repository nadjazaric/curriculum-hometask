# Project: Kibo Blog

Blogs are regularly updated websites that provide insight into a certain topic. At their inception, blogs were simply an online diary where people could keep a log about their daily lives on the web. They have since morphed into an essential forum for individuals and businesses alike to share information and updates. Much like social media platforms, blogs allow people to share their thoughts and experiences with others. Given the active comment sections, they enable people to interact with one another and build relationships based on shared interests. Essentially, blogs have become a social platform unto themselves.

In this project, you'll build a Blog Post page. The focus of the project is set arround interaction with the post - comment, like, and **share**.

As in any social network, comments section usually shows: content of the comment, post date and user information.

## Your Task

The basic design of a Blog Post page includes Post title, Post content, interaction section (like, comment, share) and comment section.

I probably have some favourite news blog your read or an account on at least one social network like Facebook, Instagram, YouTube ot Linkedin, so you are quite familiar with how interaction with content usually works. Just in case you have doubts, take a look at some of the examples here:

- [Facebook](shorturl.at/afBKU)
- [Linkedin](shorturl.at/deEM9)
- [Blog](https://yyj.be/mfbSd) (scroll to bottom to see the comment section)

Building these features require you to apply both frontend (HTML, CSS, JavaScript) and backend (Python and Flask) skills.
The design of the blog should be modern, minimalistic, and responsive.

## Starter Code

There are (mostly) empty files index.html, style.css, and script.js wired
together for you to begin your project. Feel free to add other files (such as
images) as you build out the gallery.

## Steps

### Choose Content

Choose content for your gallery.

You can use images, videos, or audio files. Images are probably the easiest choice. Audio files may be the hardest, since you'll have to find and download them, and then figure out how to display them visually. Videos are a middle ground. They are fairly easy to find, but dealing with iframe embeds will likely be slightly more challenging than images.

Whichever content you choose, be sure to find at least 6 items. That way, you'll have enough for a meaningful gallery.

For images or audio, download the files and add them to the project, either at the top level or in a folder. For video, copy the iframe embed snippets that you'll need.

### Add the content as HTML elements

Add the content you picked above as plain HTML elements in `index.html`.

For each of the items, add text content labeling the items, like titles, tags, and descriptions. You will probably find it helpful to group the item with the text in an enclosing `<div>`.
 
Also add a site title, a page description, and any other text content you want to include on the page.

At this point, the site won't look very good, and the interactions won't work, but it will have content!

### Style the selected element

Now you'll start working in `style.css` in addition to `index.html`.

Add the class `selected` to one of the elements, and use the CSS selector `.selected` to start your styling. Later on, you'll add and remove this class with JavaScript.

Change the size and position of the element and whatever content is associated with it. The selected item should end up with a different layout, positioning, and other styles from the other items.

Be sure that the element with the selected class gets styled correctly no matter where it is in the HTML. Try manually changing which item has the class 'selected' and confirming that the styles still work, no matter where the element is in your HTML.

### Style the gallery

Lay out the rest of the items as cards or list items.

Usually, gallery items go below the selected item. They are often smaller, and arranged in a grid or list.

Use the skills you learned about the box model and layout - add margins and padding, and maybe a border. Cards often look nice with a `border-radius` set.

Style the text content so that they look like titles, tags, etc. You might look back at past projects where you've styled cards for ideas on some ways to do this. You may also hide some text content when an item is in the gallery, and only show it when the item is selected.

Add a different background color for the gallery items and the background for the rest of the page, to help distinguish the items from the rest of the page.

At this point, the page should look good, but it will be missing the interactivity.

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

## Bonus Task

There's tons of further ideas you could add to your gallery if you have more time and want to make the project even cooler.

* Add more content. Galleries are more fun when there is more stuff to browse.
* Style the cursor, hover state, and the gallery cards or list items to make the gallery more appealing.
* Add a 'load more' button that shows more content. One way to do this is to have that content hidden at the start, then have the button remove a class that was hiding the content.
* Style the focused item as a modal. See  https://codeshack.io/pure-css3-modal-example/ for a suggestion on how you could style this.
* If you have videos or audio, play them when the item is focused, and stop playing when it gets unfocused.

There's tons more features that you could try to add, if you want. Be creative!
