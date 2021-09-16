# Pokemon 5e Character Creator

<img src="./README/Poke-Ball_DND3_Large.png" height="200" />

<h2>Introduction</h2>

This application is a character creator for the Dungeons & Dragons 5th Edition supplement for Pokemon. Users will be able to create their own Trainer characters using Pokemon 5e Character Creator.

Deployed Application - [Pokemon5e Character Creator](https://pokemon5e-character-creator.herokuapp.com/)

<h2>UI Wireframes and Design</h2>

||||
|:-------------------------:|:-------------------------:|:-------------------------:|
|Main Page <br> <img src="./README/LandingPageWithMenu.PNG" width="100px"/>| Register <br> <img src="./README/Register.PNG" width="100px"/>| Login <br> <img src="./README/Login.PNG" width="100px"/>|
| All Characters <br> <img src="./README/AllCharacters.PNG" width="100px"/>| My Characters <br> <img src="./README/MyCharacters.PNG" width="100px"/>| New Character Form - Race <br> <img src="./README/NewCharacter_Race.PNG" width="100px"/>|
 | New Character Form - Class <br> <img src="./README/NewCharacter_Class.PNG" width="100px"/>| New Character Form - Specialization <br> <img src="./README/NewCharacter_Specialization.PNG" width="100px"/>| New Character Form - Description <br> <img src="./README/NewCharacter_Description.PNG" width="100px"/>|
| New Character Form - Path <br> <img src="./README/NewCharacter_Path.PNG" width="100px"/>| New Character Form - Abilities <br> <img src="./README/NewCharacter_Abilities.PNG" width="100px"/>| New Character Form - Pokemon <br> <img src="./README/NewCharacter_Starter.PNG" width="100px"/>|| Database ERD <br> <img src="./README/NP5e_ERD.PNG" width="100px"/>| | | 

<h2></h2>



<h2>MVP - User Story</h2>

- User can login/register
- User taken to character list on login
- User can click button to go to form to make a new character
- User fills out form to create and save character
- Saved characters can be viewed on character list and my characters
- User will be able to edit and delete characters they have created


<h2>Snippet Highlight</h2>
 
 Bulma does not have built in acordions, which were imperative to a manageable data display for users. I built working scalable accordions in jQuery to solve this issue. There are 2 controls, one for 'top level' accordions throughout the form, and one specificically for the race abilities, which are within the character race accordions. The ability sub-accordions are separated due to my design allowing them to have multiple open at once.
 ```Javascript
 // Top level accordion on form
$("header[data-action='collapse']").click(function(){
    //Change clicked header bar icon from minus to plus or plus to minus
    if($(this).find("i").hasClass("fa-plus")){
        $(this).find("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).find("i").addClass("fa-plus").removeClass("fa-minus");
    }
    
    // Collapse other accordions' content and open clicked accordion content
    const uncollapseId = $(this).attr("data-target");
    if(!$(uncollapseId).hasClass("is-active")){
        //Collapse other accordions and change header bar icon to minus
        $(".is-collapsible.is-active").removeClass("is-active").prev().find("i").addClass("fa-plus").removeClass("fa-minus");
        
        // Show selected accordion's content
        $(uncollapseId).addClass("is-active")
        
        // Scroll selected accordion to top of screen
        $('body, html').animate({
            scrollTop: $(uncollapseId).offset().top -150
        }, 600);
    } else {
        // Hide content of clicked accordion when its already open
        $(uncollapseId).removeClass("is-active");
    }
})

// Character Race sub-accordions, separated as I wanted multiple character race accordions to be open at once
$("div.message-header[data-action='collapse-race']").click(function(){
    //Change clicked header bar icon from minus to plus or plus to minus
    if($(this).children("i").hasClass("fa-plus")){
        $(this).children("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).children("i").addClass("fa-plus").removeClass("fa-minus");
    }
    
    //Grab content area and change style to display or hide
    const collapseId = $(this).attr("data-target");
    $(collapseId).toggleClass("is-active")
    
    //Scroll screen to display opened accordion near top of screen
    $('body, html').animate({
        scrollTop: $(collapseId).offset().top -150
    }, 600);
})
 ```

<h2>Technology</h2>

- Django
- Postgresql
- django-allauth application
- Bulma CSS
- HTML
- CSS
- Javascript
- jQuery

<h2>Reference Material</h2>

[Pokemon 5e Supplement](https://www.pokemon5e.com/)

<h2>Deployed Application</h2>

[Pokemon5e Character Creator](https://pokemon5e-character-creator.herokuapp.com/)
