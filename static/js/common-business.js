$(document).ready(function () {
    /* common header */
    $("#link_to_login").click(function () {
        $(location).attr("href", "/login");
    });


    $("#link_to_selfcenter").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html();
        $(location).attr("href", "/selfcenter");
    });


    /* search page */
    $("#search_1 > div.search-input-div > span, #search_2 > div:nth-child(2) > span.input-group-addon").click(function () {
        $("#searchForm").submit();
    });


    /* archive detail page */
    $("#btn_star").hover(function () {
        $("#btn_star").css("background-image", "url('/static/image/star-yellow.png')");
        $("#form_add_favorites").submit();
    });


    /* login page */
    $("#btn_login").click(function () {
        $("#form_login").submit();
    });


    /* self_center page */
    $("#link_to_profile").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/profile");
    })
    $("#link_to_favorites").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/favorites");
    })
    $("#link_to_messagelist").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/messagelist");
    })
    $("#link_to_reservation").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/reservation");
    })
    $("#link_to_logout").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/logout");
    })

    /* profile */
    $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").click(function () {
        $("#edit_profile_form").submit();
    });
});

