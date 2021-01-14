var auth = firebase.auth();
var provider = new firebase.auth.GoogleAuthProvider();



//현재 로그인한 사용자 가져오기
userInfo();

//로그인 이벤트 처리
document.getElementById("google_login_btn").addEventListener("click", function(){
    firebase.auth().signInWithPopup(provider);
    userInfo();
});

//로그아웃 이벤트 처리
document.getElementById("logout_btn").addEventListener("click", function(){
    firebase.auth().signOut();

    document.getElementById("user_Name").style.display='none';
    document.getElementById("google_login_btn").style.display="block";
    document.getElementById("logout_btn").style.display="none";

    console.log("Sign-out successful.");
});

//현재 로그인한 사용자 가져오기
function userInfo(){
    auth.onAuthStateChanged(function(user){
        if(user != null){
            console.log("Signed in user");

            document.getElementById("user_Name").style.display="block";
            document.getElementById("google_login_btn").style.display="none";
            document.getElementById("logout_btn").style.display="block";

            user.providerData.forEach(function (profile) {            
                document.getElementById("user_Name").innerHTML = '"' +profile.displayName+ '"' +"님";
            });
        } else {
            console.log("Signed out user");
            document.getElementById("user_Name").style.display="none";
        } function error(e){
        }
    });
}

