// ログインボタンを押すとメッセージが変わる
const loginBtn = document.getElementById('loginBtn');
const st = document.getElementById('status');
let isLogin = false;

loginBtn.addEventListener("click", function() {
     
    if (isLogin === false) {
        st.textContent = "ログイン中";
        isLogin = true;
    } else {
        st.textContent = "未ログイン";
        isLogin = false;
    }
    console.log(st);
})

