module.exports.name = "youtube-node"
var youtube = new YouTube();

// 검색어 지정
var word = "강아지";
var limit = 10;  // 출력 갯수
console.log(word);

// API 키 입력
youtube.setKey('AIzaSyBfCzYMuvsqgKwtmhfzLUTXgNONM8nbodw'); 

//// 검색 옵션
youtube.addParam('order', 'rating'); // 평점 순으로 정렬
youtube.addParam('type', 'video');   // 타입 지정
youtube.addParam('videoLicense', 'creativeCommon'); // 크리에이티브 커먼즈 아이템만 불러옴



// 검색 실행
youtube.search(word, limit, function (err, result) { 
    if (err) { console.log(err); return; } // 에러일 경우 에러공지하고 빠져나감

    console.log(JSON.stringify(result, null, 2)); // 받아온 전체 리스트 출력

    var items = result["items"]; // 결과 중 items 항목만 가져옴

    const search_list = document.querySelector('#search-list');

    for (var i in items) { 
        let li = document.createElement('li');
        let li_title = document.createElement('li');
        let a = document.createElement('a');

        var it = items[i];
        var title = it["snippet"]["title"];
        var video_id = it["id"]["videoId"];
        var url = "https://www.youtube.com/watch?v=" + video_id;
        console.log("제목 : " + title);
        console.log("URL : " + url);
        console.log("-----------");

        li_title.textContent = title;
        li_title.setAttribute('id', url);
        a.setAttribute('href', url);


        li.appendChild(li_title);
        li.appendChild(a);
        search_list.appendChild(li);
    }
});

//유튜브 동영상 썸네일 추출
const dwnld = document.querySelector(".ytdwnld"),
    preveal = document.querySelector(".ytpreveal-img"),
    jpga = document.createElement("a"),
    img = document.createElement("img");
let newSrc, tmp;

document.querySelector(".button").addEventListener("click", function() {
    const input = document.getElementById("ytinput").value;
        canvas = document.createElement("canvas");
        context = canvas.getContext("2d");
    
        (input !== "" && tmp !== 1) && (
        tmp = 1,
        newSrc = `https://i.ytimg.com/vi/${input.replace(/(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?/g, "")}/original.jpg`,
        dwnld.innerHTML = "",
        preveal.innerHTML = "",
        document.getElementById("result-wrapper").style.display = "block",
        jpga.href = newSrc,
        jpga.download = "thumbnail.jpg",
        jpga.innerText = "Download",
        jpga.target = "_blank",
        img.src = newSrc,
        canvas.width = 1280,
        canvas.height = 720,
        img.addEventListener("load", function() {
        context.drawImage(img, 0, 0),
        tmp = 0
        }),
        img.style.marginBottom = "10px",
        preveal.append(img),
        preveal.append(canvas)
    )
})
