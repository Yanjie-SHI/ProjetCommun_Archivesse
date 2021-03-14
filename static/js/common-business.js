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
    $("#btn_star").click(function () {
        if ($("#session_login_user_id").val() == '') {
            $(location).attr("href", "/login");
        } else {
            if ($("#favorite_flag").val() == "false") {
                $("#form_add_favorites").submit();
            } else {
                $("#form_add_favorites").attr("action", "/remove_favorites");
                $("#form_add_favorites").submit();
            }
        }
    });

    /* search result reservation page */
    $("#btn_create_reservation").click(function () {
        $("#form_search_result_resv").attr("action", "/to_create_resv");
        $("#form_search_result_resv").submit();
    });

    /* reservation create page */
    $("#select_museum").change(function () {
        $.ajax({
            url: "/fetchmuseumaddress",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: {"museum_id": $("#select_museum").val()},
            success: function (result) {
                $("#auto_museum_address").html(result.address);
            }
        });
    });

    $("#btn_create_request").click(function () {
        $.ajax({
            url: "/create_resv",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: $('#form_create_reservation').serialize(),
            success: function (result) {
                if (result.msg == "success") {
                    alert("Vous avez réservé avec succès");
                }
            }
        });
    });

    /* reservation detail join page */
    $("#btn_send_request").click(function () {
        $.ajax({
            url: "/join_resv",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: $('#form_join_reservation').serialize(),
            success: function (result) {
                if (result.msg == "success") {
                    alert("Vous avez réservé avec succès");
                }
            }
        });
    });


    /* login page */
    $("#btn_login").click(function () {
        $("#form_login").submit();
    });

    $("#login-bg-image > div:nth-child(6) > div:nth-child(3)").click(function () {
        $(location).attr("href", "/register");
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
        $(location).attr("href", "/to_my_reservation");
    })
    $("#link_to_logout").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html()
        $(location).attr("href", "/logout");
    })

    /* my profile page */
    $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").click(function () {
        $("#edit_profile_form").submit();
    });

    /* my_reservation page */
    $("#submit_undo_join_link").click(function () {
        $.ajax({
            url: "/undo_join_resv",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: {"resv_id": $("#resv_list_item_id").html()},
            success: function (result) {
                if (result.msg == "success") {
                    alert("Vous avez annulé avec succès");
                }
            }
        });
    });

    $("#submit_confirm_status_link").click(function () {
        let role = $("#resv_list_item_role").html() == "Proposeur" ? "1" : "2";
        $.ajax({
            url: "/confirm_sent_receive_status",
            type: "POST",
            dataType: "json",
            data: {"resv_id": $("#resv_list_item_id").html()},
            success: function (result) {
                if (result.msg == "success") {
                    alert("Vous avez reçu avec succès");
                }
            }
        });
    });
});

