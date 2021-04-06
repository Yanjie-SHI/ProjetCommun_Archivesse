$(document).ready(function () {
    /* common header */
    $("#link_to_login").click(function () {
        $(location).attr("href", "/login");
    });
    $("#header-left > img").click(function () {
        $(location).attr("href", "/to_search");
    });

    $("#link_to_selfcenter").click(function () {
        let login_user_name = $("#header-right > span:nth-child(3)").html();
        $(location).attr("href", "/selfcenter");
    });

    $("#site_language").change(function () {
        let lang = $(this).val();
        $(location).attr("href", "/change_language?lang=" + lang);
    });
    let myInterval = setInterval(function () {
        $.ajax({
            url: "/fetch_my_mew_message_for_header_icon",
            type: "POST",
            dataType: "json",
            success: function (result) {
                if (result.msg == true) {
                    $("#new_msg_icon").css("display", "block");
                } else {
                    $("#new_msg_icon").css("display", "none");
                }
            }
        });
    }, 3000);
    $("#new_msg_icon").click(function () {
        $(location).attr("href", "/messagelist");
    });


    /* search page */
    $("#search_1 > div.search-input-div > span").click(function () {
        // main page archive search button
        $("#searchForm").attr("action", "/search_archive")
        $("#searchForm").submit();
    });
    $("#result_search_1 > div.search-input-div > span").click(function () {
        // search result archive page, search button
        $("#searchArchiveForm").attr("action", "/search_archive")
        $("#searchArchiveForm").submit();
    });
    $("#search_2 > div:nth-child(2) > span.input-group-addon").click(function () {
        // main page resv search button
        $("#searchForm").attr("action", "/search_resv")
        $("#searchForm").submit();
    });
    $("#result_search_2 > div:nth-child(2) > span.input-group-addon").click(function () {
        // search result resv page, search button
        $("#form_search_result_resv").attr("action", "/search_resv")
        $("#form_search_result_resv").submit();
    });
    setInputMuseumValue = function (value) {
        $("#inputMuseumName").val(value);
        $("#museum_name_hint_ul").remove();
        $("#museum_name_hint_ul2").remove();
    };
    $("#inputMuseumName").keyup(function (event) {
        if (event.keyCode == '8' || event.keyCode == '46') {
            $("#museum_name_hint_ul").remove();
        }
        let museum_name = $(this).val();
        if (museum_name.length >= 3) {
            $.ajax({
                url: "/fetchmuseumname",
                type: "POST",
                dataType: "json",//预期服务器返回的数据类型
                data: {"museum_name": museum_name},
                success: function (result) {
                    $("#museum_name_hint_ul").remove();
                    $("#museum_name_hint_ul2").remove();
                    if (result.museum_list.length > 0) {
                        let _html = "";
                        _html += '<ul id="museum_name_hint_ul">';
                        for (let item in result.museum_list) {
                            _html += '<li onclick="setInputMuseumValue($(this).html())">' + result.museum_list[item].name + '</li>';
                        }
                        _html += '</ul>';
                        //必须先将_html添加到body，再设置Css样式
                        $("#search_2").append(_html);
                        //生成Css
                        $("#museum_name_hint_ul").css({
                            width: '100%', height: '100%', zIndex: '99999', position: 'fixed',
                            top: '48.5%', left: '31.8%', listStyle: 'none', color: 'black',
                        });
                        $("#museum_name_hint_ul > li").css({
                            width: '648px', height: '30px', lineHight: '30px', fontSize: '18px', paddingLeft: '5px',
                            backgroundColor: 'white', cursor: 'pointer',
                        });
                        $("#museum_name_hint_ul > li:even").css({
                            backgroundColor: '#eeeeee',
                        });
                        // search result resv page, search div
                        let _html2 = "";
                        _html2 += '<ul id="museum_name_hint_ul2">';
                        for (let item in result.museum_list) {
                            _html2 += '<li onclick="setInputMuseumValue($(this).html())">' + result.museum_list[item].name + '</li>';
                        }
                        _html2 += '</ul>';
                        $("#search_result_2").append(_html2);
                        $("#museum_name_hint_ul2").css({
                            width: '100%', height: '100%', zIndex: '99999', position: 'fixed',
                            top: '22.5%', left: '31%', listStyle: 'none', color: 'black',
                        });
                        $("#museum_name_hint_ul2 > li").css({
                            width: '656px', height: '30px', lineHight: '30px', fontSize: '18px', paddingLeft: '5px',
                            backgroundColor: 'white', cursor: 'pointer',
                        });
                        $("#museum_name_hint_ul2 > li:even").css({
                            backgroundColor: '#eeeeee',
                        });
                    }
                },
            });
        }
    });
    $("#search_2 > div:nth-child(3) > a").click(function () {
        // main page resv create link
        $(location).attr("href", "/to_create_resv");
    });
    $("#search_3 > div > span").click(function () {
        // main page demand search button
        $("#searchForm").attr("action", "/search_demand")
        $("#searchForm").submit();
    });
    $("#result_search_1 > div > span").click(function () {
        // search result demand page, search button
        $("#form_search_result_demand").attr("action", "/search_demand")
        $("#form_search_result_demand").submit();
    });
    $("#search_3 > div:nth-child(2) > a").click(function () {
        // main page demand create link
        $(location).attr("href", "/to_create_demand");
    });

    /* search result archive page */
    $("a[id^=archive_page_link_]").click(function () {
        $("#currentPage").val($(this).html());
        $("#searchArchiveForm").submit();
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
    $("#search-result-bg-image > div.search_resv_filters > div:nth-child(3) > a").click(function () {
        if ($(this).html() == "Recherche") {
            $("#form_search_result_resv").attr("action", "/search_resv");
            $("#form_search_result_resv").submit();
        } else {
            // search filter div display link
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(2)").css("display", "block");
            $(".search_resv_filters").css("height", "300px");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(3) > a").html("Recherche");
        }
    });
    $("#btn_create_reservation").click(function () {
        $("#form_search_result_resv").attr("action", "/to_create_resv");
        $("#form_search_result_resv").submit();
    });
    $("a[id^=resv_page_link_]").click(function () {
        $("#currentPage").val($(this).html());
        $("#form_search_result_resv").submit();
    });

    /* search result demand page */
    $("#btn_create_demand, #btn_create_demand_inresv").click(function () {
        $(location).attr("href", "/to_create_demand");
    });
    $("a[id^=demand_page_link_]").click(function () {
        $("#currentPage").val($(this).html());
        $("#form_search_result_demand").submit();
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
                $("#resv_create_detail > div:nth-child(4) > div:nth-child(1)").html("Nombre document disponible : " + result.available_doc_archive_count);
                $("#resv_create_detail > div:nth-child(4) > div:nth-child(2)").html("Nombre vidéo disponible : " + result.available_video_archive_count);

                for (let i = $("#doc_demand_count").children().length - 1; i > 0; i--) {
                    if ($("#doc_demand_count").children()[i].value > result.available_doc_archive_count) {
                        $("#doc_demand_count").children()[i].remove();
                        let li_obj = document.getElementById("li_doc_" + i);
                        li_obj.style.display = "none";
                    }
                }
                for (let i = $("#video_demand_count").children().length - 1; i > 0; i--) {
                    if ($("#video_demand_count").children()[i].value > result.available_video_archive_count) {
                        $("#video_demand_count").children()[i].remove();
                        let li_obj = document.getElementById("li_video_" + i);
                        li_obj.style.display = "none";
                    }
                }
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
        $.ajax({
            url: "/profile",
            type: "POST",
            dataType: "json",//预期服务器返回的数据类型
            data: $('#edit_profile_form').serialize(),
            success: function (result) {
                if (result.msg == "success") {
                    //alert("Vous avez réservé avec succès");
                    $.MsgBox.Alert("Messages", "Les modifications sont bien enregistrées");
                } else {
                    $.MsgBox.Alert("Messages", "Votre ancien mot de passe n'est pas correct");
                }
            }
        });
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
                    $.MsgBox.Alert("Messages", "Vous avez terminé avec succès");
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
                    $.MsgBox.Alert("Messages", "Vous avez supprimé avec succès");
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
                    $.MsgBox.Alert("Messages", "Le status de réservation est bien changé");
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
                    $.MsgBox.Alert("Messages", "Le status de réservation est bien changé");
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
                    $.MsgBox.Alert("Messages", "Envoyer avec succès", true);
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
                    $.MsgBox.Alert("Messages", "Envoyer avec succès", true);
                }
            }
        });
    });
});

