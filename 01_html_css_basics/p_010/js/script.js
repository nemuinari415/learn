function drawOmikuji() {
    const result_data = ["大吉", "中吉", "小吉", "末吉", "凶"];
    const randomIndex = Math.floor(Math.random() * result_data.length);
    const result = result_data[randomIndex];
    document.getElementById("result").textContent = result;
}

document.getElementById("omikuji-btn").addEventListener("click", drawOmikuji);
