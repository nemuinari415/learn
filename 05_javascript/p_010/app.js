// 文字数カウントアプリを作ろう！
const textInput = document.getElementById('textInput');
const charCount = document.getElementById('charCount');

textInput.addEventListener('input', function() {
    const currentLength = textInput.value.length;
    charCount.textContent = `現在の文字数：${currentLength}文字`;
});