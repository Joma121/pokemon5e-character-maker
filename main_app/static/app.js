/* ===Nav controls=== */

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
$("#id_login").parent("p").addClass("block control");
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
$("#id_email").parent("p").addClass(`block control`);
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
$("#id_password").parent("p").addClass("control block");
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
$("#id_password1").parent("p").addClass("control block");
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
            $(this).addClass("is-success");
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

const switchStep = function switchStep(event) {
    if($(this).hasClass('is-active')) return;
    const chosenClass = this.className.match(/\b[^\s]+-box\b/);

    if(chosenClass == "race-box") {
        $(".prev-button").addClass("is-static");
    }else{
        $(".prev-button").removeClass("is-static");
    }
    if(chosenClass == "description-box") {
        $(".next-button").hide();
        $("#submit-character").show();
    }else{
        $(".next-button").show();
        $("#submit-character").hide();
    }

    $('.display-area').hide().removeClass("is-active");
    $('.display-area.'+chosenClass).show().addClass("is-active");
    $('.steps-marker').removeClass("is-hollow");
    $('.steps-segment').removeClass("is-active");
    $(this).addClass("is-hollow");
    $(this).parent().addClass("is-active");
    return;
}


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
    if($(this).children("i").hasClass("fa-plus")){
        $(this).children("i").addClass("fa-minus").removeClass("fa-plus");
    } else {
        $(this).children("i").addClass("fa-plus").removeClass("fa-minus");
    }
    const collapseId = $(this).attr("data-target");
    $(collapseId).toggleClass("is-active")
    $('body, html').animate({
        scrollTop: $(collapseId).offset().top -150
    }, 600);
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

    $("div.select-"+data[0]+"[data-action='select']").text("Select").removeClass("is-outlined is-danger");
    $(this).text("Selected").addClass("is-outlined is-danger");

    if(data[0] == "race"){
        $(".race-card .card-header").removeClass("selected-highlight");
        $(this).parent().parent().parent().children("header").addClass("selected-highlight")
    } else if (data[0] == "specialization"){
        $(".spec-message .message-header").removeClass("selected-highlight");
        $(this).parent().parent().prev().addClass("selected-highlight")
    }

    $("select[name="+data[0]+"]").val(data[1]).change();
    $("select[name='"+data[0]+"']").children("[value='"+data[1]+"']").attr("selected", true);

})

// check required fields, unstatic create button if all filled out

//add selected pack to django field
//default
$("#id_pack").attr("value","Dungeoneering");
$("#pack").change(function(){
    const pack = $(this).find(":selected").val();
    $("#id_pack").attr("value", pack);
})

//previous button
$(".prev-button").click(function(){
    if(!$(".display-area.is-active").hasClass(".description-box")){
        let targetDOMObject = $(".display-area.is-active").prev().get(0);
        let target = targetDOMObject.className.match(/\b[^\s]+-box\b/)[0];
        $('body, html').animate({
            scrollTop: $(".display-area.is-active").offset().top -150
        }, 200);
        $(".steps-marker."+target)[0].click();
        return;
    }
    return;
})
// next button
$(".next-button").click(function(){
    if(!$(".display-area.is-active").hasClass(".description-box")){
        let targetDOMObject = $(".display-area.is-active").next().get(0);
        let target = targetDOMObject.className.match(/\b[^\s]+-box\b/)[0];
        $('body, html').animate({
            scrollTop: $(".display-area.is-active").offset().top -150
        }, 200);
        $(".steps-marker."+target)[0].click();
        return;
    }
    return;
})
// submit button
$("#submit-character").click(function(){
    $("#character-form").submit();
})

// Event handler assignments

$('.steps-marker').click(switchStep);
$("#trainer-features").click(toggleNext);
$("#specializations").click(toggleNext);
console.log($("input,textarea,select").filter('[required]'))


// inject classes to django form elements
$("textarea").addClass("textarea");
$("input[type='text']").addClass("input");
$("input[type='number']").not("#id_pokedollars").attr("max","99").attr("min","1");

// Default display on new character
$(".display-area").hide().first().show();
$("#submit-character").hide();
$(".hidden").hide();

/* ===New Character form End=== */

/* Delete Modal control */
$('.open-delete-modal').click(function(event){
    const target = $(this).attr('id').split('-')[2]
    $('#delete-modal-'+target).addClass('is-active');
})

$('.close-delete-modal').click(function(event){
    $('.delete-modal').removeClass('is-active');
})
/* Delete Modal control End */


