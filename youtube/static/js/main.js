var currentTheme = localStorage.getItem("currentTheme");
var theme = document.querySelector('.theme-link');
var currentTheme = localStorage.getItem("currentTheme");
var theme_name = theme.getAttribute('id');
console.log(theme_name);

loadTheme();
function loadTheme(){
    if(theme_name == 'maintheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/main-dark-theme.css");
            console.log("메인 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/main-light-theme.css");
            console.log("메인 테마 : 라이트");
        }
    } else if(theme_name == 'mychanneltheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/mychannel-dark-theme.css");
            console.log("내 채널 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/mychannel-light-theme.css");
            console.log("내 채널  테마 : 라이트");
        }
    } else if(theme_name == 'searchtheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/search-dark-theme.css");
            console.log("검색 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/search-light-theme.css");
            console.log("검색  테마 : 라이트");
        }
    } else if(theme_name == 'videotheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/video-dark-theme.css");
            console.log("비디오 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/video-light-theme.css");
            console.log("비디오  테마 : 라이트");
        }
    } else if(theme_name == 'toptheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/top-dark-theme.css");
            console.log("인기 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/top-light-theme.css");
            console.log("인기  테마 : 라이트");
        }
    } else if(theme_name == 'login_signuptheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/login_signup-dark.css");
            console.log("인기 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/login_signup-light.css");
            console.log("인기  테마 : 라이트");
        }
    }
}

function ToggleTheme(){
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

    if (prefersDarkScheme.matches) {
        window.matchMedia("(prefers-color-scheme: light)").matches ? 'light' : 'dark';
    } else {
        window.matchMedia("(prefers-color-scheme: dark)").matches ? 'dark' : 'light';
    }
    
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('currentTheme', newTheme);
    window.location.reload();
}

function ToggleSidebar() {
    if(menu_box.style.width === "240px") {
        menu_box.style.width = "0";
    }else {
        menu_box.style.width = "240px";
    } 
}

function Sub() {
    var sub_btn = document.getElementById("sub_btn");
    var alarm_btn = document.getElementById("alarm_btn");

    if(sub_btn.innerText === '구독') {
        sub_btn.innerText = "구독 중";
        sub_btn.style.backgroundColor = 'var(--dark-mode5)';
        sub_btn.style.color='black';
        alarm_btn.style.display="inline-block"
    }else {
        sub_btn.innerText = '구독';
        sub_btn.style.backgroundColor='var(--red)';
        sub_btn.style.color = 'var(--dark-mode5)';
        alarm_btn.style.display="none"
    } 
}

function Alarm() {
    var alarm_btn = document.getElementById("alarm_btn");

    if(alarm_btn.style.color=="var(--dark-mode4)"){
        alarm_btn.style.color='var(--red)';
    }else{
        alarm_btn.style.color="var(--dark-mode4)";
    }
}

function CloseSearch(){
    var search_mobile = document.getElementById("search_mobile");
    var back_btn = document.getElementById("back_btn");

    search_mobile.id="search";
    back_btn.style.display = 'none';
}

function DropDownSetting() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function showTextFile() {
    const selectedFiles = document.querySelector('.upload-video_input').files;
    const list = document.createElement('ul');
    document.querySelector('.file_list').appendChild(list);

    for(const file of selectedFiles) {
        const listItem = document.createElement('li');
        const summary = document.createElement('div');
        summary.textContent = file.webkitRelativePath;
        listItem.appendChild(summary);
        list.appendChild(listItem);
    }   
}