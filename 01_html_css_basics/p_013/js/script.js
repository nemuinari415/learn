clickBtn = document.getElementById("click-btn");
clickCount = document.getElementById("click-count");
let clickCountValue = 0;


clickBtn.addEventListener("click", function() {
    clickCountValue++;
    clickCount.textContent = clickCountValue + "回クリックされました";
});