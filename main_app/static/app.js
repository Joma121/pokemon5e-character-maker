$('#mobile-nav').click(function(event){
    $('.navbar-menu').toggleClass('is-active');
    $('.navbar-burger').toggleClass('is-active');
})

$('#open-logout-modal').click(function(event){
    $('#logout-modal').toggleClass('is-active');
})

$('.close-logout-modal').click(function(event){
    $('#logout-modal').toggleClass('is-active');
})


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