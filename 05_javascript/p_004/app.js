// ボタンをクリックしたら背景色が変わる
const colorBtn = document.getElementById('colorBtn')

colorBtn.addEventListener('click', () => {
    const colors = ["red", "blue", "green", "yellow", "white"];
    const index = Math.floor(Math.random() * colors.length);
    const color = colors[index];
    document.body.style.backgroundColor = color;
});