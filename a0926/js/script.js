// 1. ajax 데이터 가져오기

let count = 1;
let total = 0;
let avg = 0;
var id_num;
let temp = 0; //수정버튼 클릭 확인 변수

$(function () {

  $.ajax({
    url: "js/stuData.json",
    type: "get",
    data: "",
    dataType: "json",
    success: function (data) {
      var s_data = ""
      //for문
      for (var i = 0; i < data.length; i++) {
        count++; // 총 갯수 확인 용 -> 추가할 때 총 갯수 이후 숫자부터 프린트
        total = data[i].kor + data[i].eng + data[i].math;
        avg = (total / 3).toFixed(2)

        s_data += `<tr id = ${i + 1}>`;
        s_data += `<td>${data[i].no}</td>`;
        s_data += `<td>${data[i].name}</td>`;
        s_data += `<td>${data[i].kor}</td>`;
        s_data += `<td>${data[i].eng}</td>`;
        s_data += `<td>${data[i].math}</td>`;

        s_data += `<td>${total}</td>`;
        s_data += `<td>${avg}</td>`;

        s_data += `<td>
            <button class='updateBtn'>수정</button>
            <button class='delBtn'>삭제</button>
            </td>`;
        s_data += `</tr>`;
      }; //for문

      $("tbody").html(s_data);

    }, //success
    error: function () {
      alert("불러오기 실패");
    } //error

  }) //ajax

  // 이벤트 구간

  // 삭제
  $(document).on("click", ".delBtn", function () {
    id_num = $(this).closest("tr").attr("id"); // 삭제 버튼(this)에서 가까운 tr 태그의 속성 태그 id 선택

    if (confirm(id_num + "번 학생 성적 삭제?")) {
      $("#" + id_num).remove(); // id 값이 n(id_num) 번째인 줄(tr)을 삭제
    }
  }); // 삭제

  // 입력
  $(document).on("click", "#create", function () {

    // 입력된 데이터 가져오기
    // let은 같은 변수명에 덮어쓰기 가능 const는 불가능
    let name = $("#name").val(); // input 입력창에 적힌 값을 변수에 저장
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());
    total = kor + eng + math;
    avg = (total / 3).toFixed(2);

    // 입력된 데이터가 있는지 확인
    // 하나라도 공백칸이 있으면, 알림창 뜨고 넘어가지 않음(return false)
    if (name == "" || kor == "" || eng == "" || math == "") {
      alert("데이터를 입력하세요.");
      return false;
    }

    // 표를 만들어서 추가시켜줌
    let s_data = "";
    s_data += `<tr id = ${count}>`;

    s_data += `<td>${count}</td>`; //for문 카운트 ++ //1001

    s_data += `<td>${name}</td>`;
    s_data += `<td>${kor}</td>`;
    s_data += `<td>${eng}</td>`;
    s_data += `<td>${math}</td>`;

    s_data += `<td>${total}</td>`;
    s_data += `<td>${avg}</td>`;

    s_data += `<td>
            <button class='updateBtn'>수정</button>
            <button class='delBtn'>삭제</button>
            </td>`;

    s_data += `</tr>`;

    $("#tbody").prepend(s_data); //위에서부터 추가

    // 추가 후 입력창 비우기
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    count++;
  }); // 입력버튼 이벤트

  // 수정

  $(document).on("click", ".updateBtn", function () {
    $("#create, #update, #updateCnacel").toggle() // 입력, 수정, 삭제 버튼 토글
    if (temp == 1) {
      alert("수정완료 또는 수정취소를 눌러주세요.")
      return false;
    }
    
    // 데이터 가져오기
    id_num = $(this).closest("tr").attr("id");
    console.log("id : " + id_num);

    let new_data = $(this).parent().prev().prev().prev()
    console.log("수학 : " + new_data.text());
    console.log("영어 : " + new_data.prev().text());
    console.log("국어 : " + new_data.prev().prev().text());
    console.log("이름 : " + new_data.prev().prev().prev().text());

    $("#name").val(new_data.prev().prev().prev().text());
    $("#kor").val(new_data.prev().prev().text());
    $("#eng").val(new_data.prev().text());
    $("#math").val(new_data.text());

    temp = 1;

  });

  //수정취소
  $(document).on("click", "#updateCancel", function () {
    alert("수정 취소");
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    $("#create, #update, #updateCancel").toggle();
    temp = 0;

  }); //수정취소





}); //function