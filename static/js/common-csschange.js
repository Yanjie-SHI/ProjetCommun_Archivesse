$(document).ready(function () {
    /* common header */
    $("#link_to_login").hover(function () {
        $("#link_to_login").addClass("mouse_over_highlight");
    });
    $("#link_to_login").mouseleave(function () {
        $("#link_to_login").removeClass("mouse_over_highlight");
    });


    $("#link_to_selfcenter").hover(function () {
        $("#link_to_selfcenter").addClass("mouse_over_highlight");
    });
    $("#link_to_selfcenter").mouseleave(function () {
        $("#link_to_selfcenter").removeClass("mouse_over_highlight");
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
        $("#archiveSearchType").val("1");
    });
    $("#search-type-numeric").click(function () {
        $("#search-type-toutes").removeClass("search-type-btn-selected");
        $("#search-type-numeric").addClass("search-type-btn-selected");
        $("#search-type-producteurs").removeClass("search-type-btn-selected");
        $("#archiveSearchType").val("2");
    });
    $("#search-type-producteurs").click(function () {
        $("#search-type-toutes").removeClass("search-type-btn-selected");
        $("#search-type-numeric").removeClass("search-type-btn-selected");
        $("#search-type-producteurs").addClass("search-type-btn-selected");
        $("#archiveSearchType").val("3");
    });

    $("#type_switch > span:nth-child(1)").click(function () {
        $("#si1").css("display", "block");
        $("#si2").css("display", "none");
        $("#si3").css("display", "none");
        $("#search_1").css("display", "block");
        $("#search_2").css("display", "none");
        $("#search_3").css("display", "none");
        $("#searchType").val("1");
    });
    $("#type_switch > span:nth-child(3)").click(function () {
        $("#si1").css("display", "none");
        $("#si2").css("display", "block");
        $("#si3").css("display", "none");
        $("#search_1").css("display", "none");
        $("#search_2").css("display", "block");
        $("#search_3").css("display", "none");
        $("#searchType").val("2");
    });
    $("#type_switch > span:nth-child(5)").click(function () {
        $("#si1").css("display", "none");
        $("#si2").css("display", "none");
        $("#si3").css("display", "block");
        $("#search_1").css("display", "none");
        $("#search_2").css("display", "none");
        $("#search_3").css("display", "block");
        $("#searchType").val("3");
    });

    /* search result archive page */
    /*$("#search-result-bg-image > div.search_filters > div:nth-child(3) > a").click(function () {
        // search filter div display link
        $("#search-result-bg-image > div.search_filters > div:nth-child(2)").css("display", "block");
        $(".search_filters").css("height", "440px");
        $("#search-result-bg-image > div.search_filters > div:nth-child(3) > a").html("Recherche");
    });*/
    /* search result resv page */
    $("#archiveTypeRadios1").change(function () {
        if ($(this)[0].checked) {
            $("#num_archive_div").css("display", "none");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(4) > span:nth-child(1)").html("Tous");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(5)").css("display", "none");
            $("#num_archive_div > input[type=text]").val("");
        }
    });
    $("#archiveTypeRadios2").change(function () {
        if ($(this)[0].checked) {
            $("#num_archive_div").css("display", "block");
            $("#hint_info_doc").css("display", "block");
            $("#hint_info_audio").css("display", "none");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(4) > span:nth-child(1)").html("Document");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(5)").css("display", "block");
        }
    });
    $("#archiveTypeRadios3").change(function () {
        if ($(this)[0].checked) {
            $("#num_archive_div").css("display", "block");
            $("#hint_info_doc").css("display", "none");
            $("#hint_info_audio").css("display", "block");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(4) > span:nth-child(1)").html("Audio-visuelle");
            $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(5)").css("display", "block");
        }
    });
    $("#num_archive_div > input[type=text]").focusout(function () {
        $("#search-result-bg-image > div.search_resv_filters > div:nth-child(1) > div:nth-child(5) > span:nth-child(1)").html($(this).val());
    });

    /* archive detail page */
    $("#btn_star").hover(function () {
        if ($("#btn_star").css("background-image").endsWith("/star-white.png\")")) {
            $("#btn_star").css("background-image", "url(\"/static/image/star-yellow.png\")");
        } else {
            $("#btn_star").css("background-image", "url(\"/static/image/star-white.png\")");
        }
    });

    /* reservation detail join page */
    $("#doc_demand_count").change(function () {
        let needed_li_count = $("#doc_demand_count").val();
        if (needed_li_count == "0") {
            $("#doc_archive_input_ul").css("display", "none");
            $("#no_doc_archive_demand_notice_div").css("display", "block");
        } else {
            $("#doc_archive_input_ul").children("li").each(function (index) {
                $("#no_doc_archive_demand_notice_div").css("display", "none");
                $("#doc_archive_input_ul").css("display", "block");
                let li_id = $(this).attr("id");
                if (parseInt(li_id.substr(7)) > parseInt(needed_li_count)) {
                    $(this).css("display", "none");
                } else {
                    if ($(this).css("display") == "none") {
                        $(this).css("display", "block");
                    }
                }
            });
        }
    });

    $("#video_demand_count").change(function () {
        let needed_li_count = $("#video_demand_count").val();
        if (needed_li_count == "0") {
            $("#video_archive_input_ul").css("display", "none");
            $("#no_video_archive_demand_notice_div").css("display", "block");
        } else {
            $("#video_archive_input_ul").children("li").each(function (index) {
                $("#no_video_archive_demand_notice_div").css("display", "none");
                $("#video_archive_input_ul").css("display", "block");
                let li_id = $(this).attr("id");
                if (parseInt(li_id.substr(9)) > parseInt(needed_li_count)) {
                    $(this).css("display", "none");
                } else {
                    if ($(this).css("display") == "none") {
                        $(this).css("display", "block");
                    }
                }
            });
        }
    });

    /* login page */
    $("#btn_login").hover(function () {
        $("#btn_login").addClass("mouse_over_highlight");
    });
    $("#btn_login").mouseleave(function () {
        $("#btn_login").removeClass("mouse_over_highlight");
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
    $("#link_to_demand").hover(function () {
        $("#link_to_demand").addClass("mouse_over_highlight");
    });
    $("#link_to_demand").mouseleave(function () {
        $("#link_to_demand").removeClass("mouse_over_highlight");
    });
    $("#link_to_logout").hover(function () {
        $("#link_to_logout").addClass("mouse_over_highlight");
    });
    $("#link_to_logout").mouseleave(function () {
        $("#link_to_logout").removeClass("mouse_over_highlight");
    });


    /* profile */
    $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").hover(function () {
        $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").addClass("hover");
    });
    $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").mouseleave(function () {
        $("#edit_profile_form > div:nth-child(2) > div:nth-child(3) > span").removeClass("hover");
    });

    /* my reservation page */
    $("#reservation-bg-image > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").click(function () {
        $("#reservation_detail").css("display", "block");
        $("#reservation-bg-image > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div.indicator").css("display", "block");
        $("#reservation_detail_finished").css("display", "none");
        $("#reservation-bg-image > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div.indicator").css("display", "none");
    });
    $("#reservation-bg-image > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1)").click(function () {
        $("#reservation_detail_finished").css("display", "block");
        $("#reservation-bg-image > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div.indicator").css("display", "block");
        $("#reservation_detail").css("display", "none");
        $("#reservation-bg-image > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div.indicator").css("display", "none");
    });
});

