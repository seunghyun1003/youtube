

var firebaseConfig = {
    apiKey: "AIzaSyAzldBsf96FUTyYZninkxf6TCeBbHgKN3o",
    authDomain: "clone-41130.firebaseapp.com",
    databaseURL: "https://clone-41130-default-rtdb.firebaseio.com",
    projectId: "clone-41130",
    storageBucket: "clone-41130.appspot.com",
    messagingSenderId: "45922064950",
    appId: "1:45922064950:web:d96c56a018c5295fb05697",
    measurementId: "G-8NLBJZHVVB"
};

firebase.initializeApp(firebaseConfig);

var db = firebase.firestore();
var user = firebase.auth().currentUser;

document.getElementById("fileupload_btn").addEventListener("change", function(){
    //업로드할 파일 선택
    var fileButton = document.getElementById("fileupload_btn");
    var file = fileButton.files[0];
    var fileName = file.name;
    var inpufile_name = document.getElementById("input_file");

    inpufile_name.textContent = "파일명 : "+"<"+fileName+">";
    console.log(fileName+"이 선택됨.");
})

//파일 저장 버튼 리스너
document.getElementById("saveFile_btn").addEventListener("click", function(){
    auth.onAuthStateChanged(function(user){
        if(user != null){
            user.providerData.forEach(function (profile) {
                var result = confirm("파일을 저장하시겠습니까?");
                if(result){
                    addFile(profile);
                }
                else{
                    //파일 저장을 취소하였을 때
                    console.log("파일 저장 취소");
                }
            });
        } else {
            var result = confirm("파일을 저장하려면 로그인이 필요합니다. 로그인 후 저장하시겠습니까?");

            if(result){
                firebase.auth().signInWithPopup(provider);
                auth.onAuthStateChanged(function(user){
                    if(user != null){
                        console.log("파일저장 위해 로그인")
                    } else {
                        console.log("파일저장 위해 로그인 했지만 실패")
                    }
                });
            }else{
                console.log("파일저장을 위한 로그인 취소")
            }
        }
    })
})

//storage, firestore에 파일 저장
function addFile(profile){ 
    //업로드할 파일 선택
    var fileButton = document.getElementById("fileupload_btn");
    var file = fileButton.files[0];

    try{var fileName = file.name;}
    catch{alert("파일을 먼저 선택해주세요.");}

    //firebase-storage에 파일 업로드
    var storageRef = firebase.storage().ref(fileName);
    var uploadTask = storageRef.put(file);
    uploadTask.on('state_changed', function(snapshot){
        var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        console.log('Upload is ' + progress + '% done');
        switch (snapshot.state) {
            case firebase.storage.TaskState.PAUSED: // or 'paused'
            console.log('Upload is paused');
            break;
            case firebase.storage.TaskState.RUNNING: // or 'running'
            console.log('Upload is running');
            break;
        }
    }, function(error){
        console.log("파일 저장 실패");
    }, function() {
        //파일 업로드 성공 시
        uploadTask.snapshot.ref.getDownloadURL().then(function(downloadURL) {
            console.log("storage에 파일 업로드 성공");
            console.log(downloadURL);
            
            //firestore에 파일에 대한 정보 (파일명, 저장시간, 파일url) 저장
            //충돌을 피하기위해 doc.id에 now추가
            var now= firebase.firestore.Timestamp.fromDate(new Date());
            var File_id = fileName + " + " +now; 
            db.collection("users").doc(profile.uid).collection("filelist").doc(File_id).set({
                File_id : fileName + " + " +now,
                Create_Date : now,
                File_Title : fileName,
                File_Url : downloadURL
            });

            alert("파일을 성공적으로 저장하였습니다.");
        })
    })
}


//파일 목록에 파일 리스트 만들기
function filelist(profile){
    var docRef = db.collection("users").doc(profile.uid).collection("filelist");
    const filelist_list = document.querySelector('#filelist-list');

    docRef.get().then((snapshot) => {
        snapshot.forEach(function(docRef){     
            renderFile(docRef);     
        })
    })

    //파일 목록 : File_Title에 링크를 달아 동영상 확인
    function renderFile(docRef){
        let li = document.createElement('li');
        let title = document.createElement('a');
        let url = document.createElement('span');
        let delete_btn = document.createElement('button');

        title.setAttribute('href', docRef.data().File_Url);
        delete_btn.setAttribute = ('id', docRef.id);
        title.textContent = docRef.data().File_Title;
        delete_btn.innerHTML = "삭제";

        li.appendChild(title);
        li.appendChild(url);
        li.appendChild(delete_btn);
        filelist_list.appendChild(li);

        //파일목록 삭제 이벤트 처리
        delete_btn.addEventListener('click', function(){
            var result = confirm(docRef.data().File_Title + "을 삭제하시겠습니까?")
            if(result){
                var FileRef = docRef.data().File_id;
                console.log(FileRef + '을 삭제');
                filelist_list.removeChild(li);
                db.collection("users").doc(profile.uid).collection("filelist").doc(FileRef).delete().then(function() {
                    alert(docRef.data().File_Title + ' 삭제 완료');
                    console.log(docRef.data().File_Title + ' 삭제 완료');
                });
            }else{
                alert(docRef.data().File_Title + "삭제 실패")
            }
        })
        
        if (matchMedia("screen and (max-width: 768px)").matches) {
            // 320px 미만에서 사용할 JavaScript
            li.style.display="flex";
            li.style.justifyContent="space-between";
            li.style.padding= '1em 1em';
            li.style.borderBottom="1px solid var(--dark-mode4)";
            title.style.fontSize = '1em';
            delete_btn.style.fontSize = '0.8em';
            delete_btn.style.color = 'gray';
            delete_btn.style.padding = '0.1em';
            delete_btn.style.border = '2px solid var(--dark-mode4)';
            delete_btn.style.borderRadius = '0.25em';
        } else {
            // 320px 이상에서 사용할 JavaScript
            li.style.display="flex";
            li.style.justifyContent="space-between";
            li.style.padding= '1.2em 10em';
            li.style.textAlign = 'center';
            li.style.borderBottom="1px solid var(--dark-mode4)";
            title.style.fontSize = '1.2em';
            delete_btn.style.fontSize = '1em';
            delete_btn.style.color = 'gray';
            delete_btn.style.padding = '0.2em';
            delete_btn.style.border = '2px solid var(--dark-mode4)';
            delete_btn.style.borderRadius = '0.25em';
        }
    }
}