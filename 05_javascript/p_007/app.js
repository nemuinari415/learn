// カウントアップ・カウントダウンアプリ
function Counter() {
    const plusBtn = document.getElementById('plus-btn');
    const minusBtn = document.getElementById('minus-btn');
    let count = document.getElementById('count');

    plusBtn.addEventListener('click', () => {
        // 文字列を数値として取得する
        let cnt = parseInt(count.textContent) + 1;
        count.textContent = cnt;
    });

    minusBtn.addEventListener('click', () => {
        // 文字列を数値として取得する
        let cnt = parseInt(count.textContent) - 1;

        if (cnt < 0) {
            cnt = 0;
        }

        count.textContent = cnt;
    });
}
Counter();