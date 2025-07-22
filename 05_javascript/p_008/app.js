// 利用規約に同意しないと送信できないボタンを作ろう！
const agreeBtn = document.getElementById('agree');
const submitBtn = document.getElementById('submitBtn');

agreeBtn.addEventListener('change', function() {
    submitBtn.disabled = !agreeBtn.checked;
    // チェックしていないとき → true → disabled = true（送信ボタンが無効）
    // チェックしているとき → false → disabled = false（送信ボタンが有効）
});