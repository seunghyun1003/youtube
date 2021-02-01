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
            console.log("로그인 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/login_signup-light.css");
            console.log("로그인  테마 : 라이트");
        }
    } else if(theme_name == 'whotheme'){
        if (currentTheme == "dark") {
            theme.setAttribute('href', "static/css/who-dark.css");
            console.log("내 계정 테마 : 다크");
        } else{
            theme.setAttribute('href', "static/css/who-light.css");
            console.log("내 계정 테마 : 라이트");
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
    if(menu_box.style.width = "0") {
        menu_box.style.width = "240px";
    }else {
        menu_box.style.width = "0";
    } 
}

function DropDownSetting() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function VideoDesShow(){
    var des = document.getElementById("video_des");
    var des_showbtn = document.getElementById("videodes_showbtn");

    if(des.style.display == "none"){
        des.style.display = "block"
        des_showbtn.style.display = "none"
    } else{
        des.style.display = "none"
        des_showbtn.style.display = "inline"
    }
}