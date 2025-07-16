const profCard = document.getElementById("profile-card");
const bgColorList =  ["#FFDDC1", "#C1FFD7", "#C1D4FF", "#FFC1C1"];
const message = document.querySelector(".message");

profCard.addEventListener("click", function() {
    
    // 背景色を変える
    let index = Math.floor(Math.random() * bgColorList.length);
    let color = bgColorList[index];
    document.body.style.backgroundColor = color;

    message.textContent = `色コード: ${color}`;
    console.log(color);
});