$(document).ready(function () {
    /* common header */
    $("#link_to_login").hover(function () {
        $("#link_to_login").addClass("mouse_over_highlight");
    });
    $("#link_to_login").mouseleave(function () {
        $("#link_to_login").removeClass("mouse_over_highlight");
    });
    $("#link_to_login").click(function () {
        $(location).attr("href", "/login");
    });


    $("#link_to_selfcenter").hover(function () {
        $("#link_to_selfcenter").addClass("mouse_over_highlight");
    });
    $("#link_to_selfcenter").mouseleave(function () {
        $("#link_to_selfcenter").removeClass("mouse_over_highlight");
    });
    $("#link_to_selfcenter").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html();
        $(location).attr("href", "/selfcenter?login_user_name=" + login_user_name);
    });


    /* search page */
    let search_particle_open_flag = 0; // 查询粒度div显示标记
    $("#search_1 > div.search-input-div > div").click(function () {
        if (search_particle_open_flag == 0) {
            $("#search_1").css("top", "-40px");
            $("#search_1_particle").css("display", "block");
            search_particle_open_flag = 1;
        } else {
            $("#search_1").css("top", "0px");
            $("#search_1_particle").css("display", "none");
            search_particle_open_flag = 0;
        }
    });

    $("#search-type-toutes").click(function () {
        $("#search-type-toutes").addClass("search-type-btn-selected");
        $("#search-type-numeric").removeClass("search-type-btn-selected");
        $("#search-type-producteurs").removeClass("search-type-btn-selected");
    });
    $("#search-type-numeric").click(function () {
        $("#search-type-toutes").removeClass("search-type-btn-selected");
        $("#search-type-numeric").addClass("search-type-btn-selected");
        $("#search-type-producteurs").removeClass("search-type-btn-selected");
    });
    $("#search-type-producteurs").click(function () {
        $("#search-type-toutes").removeClass("search-type-btn-selected");
        $("#search-type-numeric").removeClass("search-type-btn-selected");
        $("#search-type-producteurs").addClass("search-type-btn-selected");
    });

    $("#type_switch > span:nth-child(1)").click(function () {
        $("#si1").css("display", "block");
        $("#si2").css("display", "none");
        $("#search_1").css("display", "block");
        $("#search_2").css("display", "none");
    });
    $("#type_switch > span:nth-child(3)").click(function () {
        $("#si1").css("display", "none");
        $("#si2").css("display", "block");
        $("#search_1").css("display", "none");
        $("#search_2").css("display", "block");
    });


    /* login page */
    $("#btn_login").hover(function () {
        $("#btn_login").addClass("mouse_over_highlight");
    });
    $("#btn_login").mouseleave(function () {
        $("#btn_login").removeClass("mouse_over_highlight");
    });
    $("#btn_login").click(function () {
        $("#form_login").submit();
    });


    /* self_center page */
    $("#link_to_profile").hover(function () {
        $("#link_to_profile").addClass("mouse_over_highlight");
    });
    $("#link_to_profile").mouseleave(function () {
        $("#link_to_profile").removeClass("mouse_over_highlight");
    });
    $("#link_to_favorites").hover(function () {
        $("#link_to_favorites").addClass("mouse_over_highlight");
    });
    $("#link_to_favorites").mouseleave(function () {
        $("#link_to_favorites").removeClass("mouse_over_highlight");
    });
    $("#link_to_messagelist").hover(function () {
        $("#link_to_messagelist").addClass("mouse_over_highlight");
    });
    $("#link_to_messagelist").mouseleave(function () {
        $("#link_to_messagelist").removeClass("mouse_over_highlight");
    });
    $("#link_to_reservation").hover(function () {
        $("#link_to_reservation").addClass("mouse_over_highlight");
    });
    $("#link_to_reservation").mouseleave(function () {
        $("#link_to_reservation").removeClass("mouse_over_highlight");
    });
    $("#link_to_logout").hover(function () {
        $("#link_to_logout").addClass("mouse_over_highlight");
    });
    $("#link_to_logout").mouseleave(function () {
        $("#link_to_logout").removeClass("mouse_over_highlight");
    });

    $("#link_to_profile").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/profile?login_user_name=" + login_user_name);
    })
    $("#link_to_favorites").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/favorites?login_user_name=" + login_user_name);
    })
    $("#link_to_messagelist").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/messagelist?login_user_name=" + login_user_name);
    })
    $("#link_to_reservation").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/reservation?login_user_name=" + login_user_name);
    })
    $("#link_to_logout").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/logout?login_user_name=" + login_user_name);
    })
});

