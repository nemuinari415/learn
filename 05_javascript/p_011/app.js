// 年齢確認チェック
const agreeBtn = document.getElementById("agree");
const over20Btn = document.getElementById("over20");
const submitBtn = document.getElementById("submitBtn");
    
agreeBtn.addEventListener("change", checkSubmitButton);
over20Btn.addEventListener("change", checkSubmitButton);

function checkSubmitButton() {
    if (agreeBtn.checked && over20Btn.checked) {
        submitBtn.disabled = false;
    } else {
        submitBtn.disabled = true;
    }
}

/*
<input type="checkbox" id="agree"> 利用規約に同意する<br>
<input type="checkbox" id="over20"> 20歳以上です<br>
<button id="submitBtn" disabled>送信</button></br>
*/