$('#mobile-nav').click(function(event){
    $('.navbar-menu').toggleClass('is-active');
    $('.navbar-burger').toggleClass('is-active');
})

/* Logout Modal control */
$('#open-logout-modal').click(function(event){
    $('#logout-modal').toggleClass('is-active');
})

$('.close-logout-modal').click(function(event){
    $('#logout-modal').toggleClass('is-active');
})
/* Logout Modal control End */


/* Login and Signup forms */
/**
 * Login Email - Inject Bulma classes to django-auth form  
 */ 
$('#id_login').addClass("input");
$("#id_login").parent("p").addClass("block control has-icons-left");
$('#id_login').prev("label").addClass("label");
// $('#id_login').after("<span class='icon is-small is-left'><i class='fas fa-envelope'></i></span>");
$("#id_login").change(function(event){
    const mailformat = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$";
    if(!this.value.match(mailformat)){
        if(!$(this).hasClass("is-warning")){
            $(this).removeClass('is-success');
            $(this).before("<span class='tag is-warning'>Please enter a valid email.</span>");
            $(this).addClass("is-warning")
            $(".login-button").prop("disabled", true);
        }
    } else {
        if(!$(this).hasClass("is-success")){
            $(this).removeClass('is-warning');
            $(this).addClass("is-success")
            if($("#id_password").hasClass("is-success"))
                $(".login-button").prop("disabled", false);
        }
        if($(this).prev("span")){
            $(this).prev("span").remove();
        }
    }
})

/**
 * Signup Email - Inject Bulma classes to django-auth form  
 */ 
$("#id_email").addClass("input");
$("#id_email").parent("p").addClass(`control has-icons-left`);
// $("#id_email").parent("p").wrap(`<div class="field"></div>`);
$("#id_email").prev("label").addClass("label");
// $('#id_email').after(`<span class="icon is-small is-left"><i class="fas fa-envelope"></i></span>`);
$("#id_email").change(function(event){
    const mailformat = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$";
    if(!this.value.match(mailformat)){
        if(!$(this).hasClass("is-warning")){
            $(this).removeClass('is-success');
            $(this).before("<span class='tag is-warning'>Please enter a valid email.</span>");
            $(this).addClass("is-warning")
            $(".signup-button").prop("disabled", true);
        }
    } else {
        if(!$(this).hasClass("is-success")){
            $(this).removeClass('is-warning');
            $(this).addClass("is-success")
            if($("#id_password1").hasClass("is-success"))
                $(".signup-button").prop("disabled", false);
        }
        if($(this).prev("span")){
            $(this).prev("span").remove();
        }
    }
})


/**
 * Login Password - Inject Bulma classes to django-auth form  
 */ 
$("#id_password").addClass('input');
$("#id_password").parent("p").addClass("control has-icons-left block");
$("#id_password").prev("label").addClass("label");
// $('#id_password').after("<span class='icon is-small is-left'><i class='fas fa-lock'></i></span>");
$("#id_password").change(function(event){
    if(this.value.length < 8){
        if(!$(this).hasClass("is-warning")){
            $(this).removeClass('is-success');
            $(this).before("<span class='tag is-warning'>Password must be at least 8 characters.</span>");
            $(this).addClass("is-warning")
            $(".login-button").prop("disabled", true);
        }
    } else {
        if(!$(this).hasClass("is-success")){
            $(this).removeClass('is-warning');
            $(this).addClass("is-success")
            if($("#id_login").hasClass("is-success"))
                $(".login-button").prop("disabled", false);
        }
        if($(this).prev("span")){
            $(this).prev("span").remove();
        }
    }
})


/**
 * Signup Password - Inject Bulma classes to django-auth form  
 */ 
$("#id_password1").addClass('input');
$("#id_password1").parent("p").addClass("control has-icons-left");
$("#id_password1").parent("p").wrap("<div class='field'></div>")
$("#id_password1").prev("label").addClass("label");
// $('#id_password1').after("<span class='icon is-left'><i class='fas fa-lock'></i></span>");
$("#id_password1").change(function(event){
    if(this.value.length < 8){
        if(!$(this).hasClass("is-warning")){
            $(this).removeClass('is-success');
            $(this).before("<span class='tag is-warning'>Password must be at least 8 characters.</span>");
            $(this).addClass("is-warning")
            $(".signup-button").prop("disabled", true);
        }
    } else {
        if(!$(this).hasClass("is-success")){
            $(this).removeClass('is-warning');
            $(this).addClass("is-success")
            if($("#id_email").hasClass("is-success"))
                $(".signup-button").prop("disabled", false);
        }
        if($(this).prev("span")){
            $(this).prev("span").remove();
        }
    }
})

/* Login and Signup form End */

/* New Character form */
// Default display on new character
$(".display-area").hide().first().next().next().next().show();

const switchStep = function switchStep(event) {
    if($(this).hasClass('is-active')) return;
    const chosenClass = this.className.match(/\b[^\s]+-box\b/);
    $('.display-area').hide();
    $('.'+chosenClass).show();
    $('.steps-marker').removeClass("is-hollow");
    $('.steps-segment').removeClass("is-active");
    $(this).addClass("is-hollow");
    $(this).parent().addClass("is-active");
}

$('.steps-marker').click(switchStep);

// Top level accordion on form
$("header[data-action='collapse']").click(function(){
    
    if($(this).find("i").hasClass("fa-plus")){
        $(this).find("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).find("i").addClass("fa-plus").removeClass("fa-minus");
    }
    const uncollapseId = $(this).attr("data-target");
    if(!$(uncollapseId).hasClass("is-active")){
        $(".is-collapsible.is-active").removeClass("is-active").prev().find("i").addClass("fa-plus").removeClass("fa-minus");
        $(uncollapseId).addClass("is-active")
        $('body, html').animate({
            scrollTop: $(uncollapseId).offset().top -150
        }, 600);
    } else {
        $(uncollapseId).removeClass("is-active");
    }
})

// Race sub-accordions
$("div.message-header[data-action='collapse-race']").click(function(){
    console.log(this)
    if($(this).children("i").hasClass("fa-plus")){
        $(this).children("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).children("i").addClass("fa-plus").removeClass("fa-minus");
    }
    const collapseId = $(this).attr("data-target");
    $(collapseId).toggleClass("is-active")
})

// Trainer Features box toggle
const toggleNext = function toggleNext(){
    if($(this).children("i").hasClass("fa-plus")){
        $(this).children("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).children("i").addClass("fa-plus").removeClass("fa-minus");
    }
    $(this).next().toggleClass("is-active");
}

$("#trainer-features").click(toggleNext);
$("#specializations").click(toggleNext);

// Trainer class features sub accordions
$("div.message-header[data-action='collapse-trainer']").click(function(){
    if($(this).children("i").hasClass("fa-plus")){
        $(this).children("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).children("i").addClass("fa-plus").removeClass("fa-minus");
    }
    const collapseId = $(this).attr("data-target");
    $(collapseId).toggleClass("is-active")
})

$("div[data-action='select']").click(function(){
    const data = $(this).attr("id").split("-");
    const target = data[0]+"-input";
    const value = data[1];

    console.log($("div.select-"+data[0]+"[data-action='select']"))
    $("div.select-"+data[0]+"[data-action='select']").text("Select").removeClass("is-outlined is-danger");
    $(this).text("Selected").addClass("is-outlined is-danger");

    if(data[0] == "race"){
        $(".race-card .card-header").removeClass("selected-highlight");
        $(this).parent().parent().parent().children("header").addClass("selected-highlight")
    } else if (data[0] == "spec"){
        $(".spec-message .message-header").removeClass("selected-highlight");
        $(this).parent().parent().prev().addClass("selected-highlight")
    }

    $('#'+target).val(value);
    console.log($("#race-input"));
})


/* New Character form End */

