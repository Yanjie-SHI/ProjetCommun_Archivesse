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
    $("#search_1 > div.search-input-div > span").click(function () {
        $("#searchForm").attr("action", "/search_archive")
        $("#searchForm").submit();
    });
    $("#search_2 > div:nth-child(2) > span.input-group-addon").click(function () {
        $("#searchForm").attr("action", "/search_resv")
        $("#searchForm").submit();
    });
    $("#search_3 > div > span").click(function () {
        $("#searchForm").attr("action", "/search_demand")
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

    /* search result demand page */
    $("#btn_create_demand").click(function () {
        $(location).attr("href", "/to_create_demand");
    });
    $("div[id^=help_btn_]").click(function () {
        let this_node = $(this);
        $.ajax({
            url: "/verify_login",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            success: function (result) {
                if (result.msg == "success") {
                    let demander_username = this_node.parent().children()[3].value;
                    let demander_mail = this_node.parent().children()[4].value;
                    $.MsgBox.Alert("Merci d'envoyer les archives au adresse suivante : ", "Demandé par : " + demander_username + "</br></br>E-mail : " + demander_mail);
                    $("#mb_con").css({width: '450px'});
                } else {
                    $(location).attr("href", "/login");
                }
            },

        });
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
                    //alert("Vous avez réservé avec succès");
                    $.MsgBox.Alert("Messages", "Vous avez réservé avec succès");
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
                    //alert("Vous avez réservé avec succès");
                    $.MsgBox.Alert("Messages", "Vous avez réservé avec succèss");
                }
            }
        });
    });

    /* demand create page */
    $("#btn_div_create_demand").click(function () {
        $("#form_create_demand")
        $.ajax({
            url: "/create_demand",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: $('#form_create_demand').serialize(),
            success: function (result) {
                if (result.msg == "success") {
                    //alert("Vous avez réservé avec succès");
                    $.MsgBox.Alert("Messages", "Vous avez réservé avec succès");
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

    /* register page */
    $("#register-bg-image > form > div:nth-child(4) > div:nth-child(2) > div").click(function () {
        $("#form_register").submit();
    });

    /* self_center page */
    $("#link_to_profile").click(function () {
        $(location).attr("href", "/profile");
    });
    $("#link_to_favorites").click(function () {
        $(location).attr("href", "/favorites");
    });
    $("#link_to_messagelist").click(function () {
        $(location).attr("href", "/messagelist");
    });
    $("#link_to_reservation").click(function () {
        $(location).attr("href", "/to_my_reservation");
    });
    $("#link_to_demand").click(function () {
        $(location).attr("href", "/to_my_demand");
    });
    $("#link_to_logout").click(function () {
        $(location).attr("href", "/logout");
    });

    /* my profile page */
    $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").click(function () {
        $("#edit_profile_form").submit();
    });

    /* my_reservation page */
    $("a[id^=submit_undo_join_link]").click(function () {
        let resv_id = $(this).attr("id").substr(22);
        $.ajax({
            url: "/undo_join_resv",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: {"resv_id": resv_id},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Vous avez annulé avec succès");
                    //alert("Vous avez annulé avec succès");
                }
            }
        });
    });

    $("a[id^=submit_confirm_status_link]").click(function () {
        let resv_id = $(this).attr("id").substr(27);
        $.ajax({
            url: "/confirm_sent_receive_status",
            type: "POST",
            dataType: "json",
            data: {"resv_id": resv_id},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Vous avez reçu avec succès");
                }
            }
        });
    });

    /* my demand page */
    $("a[id^=terminate_demand_]").click(function () {
        let demand_id = $(this).attr("id").substr(17);
        $.ajax({
            url: "/terminate_demand",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: {"demand_id": demand_id},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Vous avez annulé avec succès");
                }
            }
        });
    });

    $("a[id^=delete_demand_]").click(function () {
        let demand_id = $(this).attr("id").substr(14);
        $.ajax({
            url: "/delete_demand",
            type: "POST",
            dataType: "json",
            data: {"demand_id": demand_id},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Vous avez reçu avec succès");
                }
            }
        });
    });

    /* reservation creator view from selfcenter */
    $("#notgo_radio").click(function () {
        $.ajax({
            url: "/update_resv_status",
            type: "POST",
            dataType: "json",
            data: {"resv_id": $("#resv_id").val(), "status": "0"},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Reservation status change success");
                }
            }
        });
    });
    $("#gone_radio").click(function () {
        $.ajax({
            url: "/update_resv_status",
            type: "POST",
            dataType: "json",
            data: {"resv_id": $("#resv_id").val(), "status": "1"},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Reservation status change success");
                }
            }
        });
    });
    $("a[id^=doc_send_link]").click(function () {
        let receiver_id = $(this).attr("id").substr(14);
        $.ajax({
            url: "/confirm_sent_receive_status",
            type: "POST",
            dataType: "json",
            data: {"resv_id": $("#resv_id").val(), "receiver_id": receiver_id, "arch_type": 0},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Send success");
                }
            }
        });
    });
    $("a[id^=video_send_link]").click(function () {
        let receiver_id = $(this).attr("id").substr(16);
        $.ajax({
            url: "/confirm_sent_receive_status",
            type: "POST",
            dataType: "json",
            data: {"resv_id": $("#resv_id").val(), "receiver_id": receiver_id, "arch_type": 2},
            success: function (result) {
                if (result.msg == "success") {
                    $.MsgBox.Alert("Messages", "Send success");
                }
            }
        });
    });
});

