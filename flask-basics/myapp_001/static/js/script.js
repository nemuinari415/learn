// 入力された文字数をカウントする
document.addEventListener("DOMContentLoaded", () => {
    const text = document.querySelector('#message-box'); // id="message-box"
    const count = document.querySelector('#count'); // id="count"


    text.addEventListener('keyup', () => {
        // キー入力された時の処理
        count.textContent = text.value.length;  // 文字数

        if (text.value.length > 100) { // 100文字以上なら
            count.classList.add('alert');
        } else {
            count.classList.remove('alert');
        }
    });
});