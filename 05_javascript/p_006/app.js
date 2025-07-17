// 名前を表示するボタン
const showBtn = document.getElementById('showBtn');
const nameInput = document.getElementById('nameInput');
const greeting = document.getElementById('greeting');


showBtn.addEventListener('click', () => {
   
    let name = nameInput.value;
    greeting.textContent = name;
    console.log(name);

});