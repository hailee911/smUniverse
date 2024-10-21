// 제이쿼리 선언
$(function () {

  $("#searchBtn").click(function () {
    alert("검색버튼 클릭");
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Y%2BduMd7L0jpQJx4Q09xs0zpRg0z3FvIYfWQVMCwtC%2BEY33tNGgPCV8ehJtjvLj4dCCOS6koa0w%2Fw6W7qksNz4w%3D%3D&numOfRows=10&pageNo=1&MobileOS=ET&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url: surl,
      type: "get",
      data: "",
      dataType: "json    ",
      success: function (data) {
        alert("성공")
        var item_list = data.response.body.items.item
        console.log(item_list[1].galTitle);
      
        var s_data = "";
        for(var i=0; i<item_list.length; i++){
          s_data += `<tr>`
          s_data += `<td>${item_list[i].galContentId}</td>`
          s_data += `<td>${item_list[i].galTitle}</td>`
          s_data += `<td>${item_list[i].galPhotographer}</td>`
          s_data += `<td>${item_list[i].galModifiedtime}</td>`
          s_data += `<td><img src='${item_list[i].galWebImageUrl}'></td>`

          s_data += `</tr>`
        }
        $("#tbody").html(s_data);
      },
      error: function () {
        alert("실패");
      }
    }); //ajax
  }); //searchBtn

}); //제이쿼리