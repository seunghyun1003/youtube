const YouTube = require('youtube-node');
const youtube = new YouTube();

// 검색어 지정
const word = "강아지";
const limit = 10;  // 출력 갯수
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

    const items = result["items"]; // 결과 중 items 항목만 가져옴

    const search_list = document.querySelector('#search-list');

    for (const i in items) { 
        let li = document.createElement('li');
        let li_title = document.createElement('li');
        let a = document.createElement('a');

        let it = items[i];
        let title = it["snippet"]["title"];
        let video_id = it["id"]["videoId"];
        let url = "https://www.youtube.com/watch?v=" + video_id;
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