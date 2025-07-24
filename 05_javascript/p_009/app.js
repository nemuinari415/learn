// チェックした選択肢を表示しよう
const fruits = document.querySelectorAll('.fruit');
const button = document.getElementById('showFruitBtn');
const result = document.getElementById('result');

button.addEventListener('click', () => {
    const selectedFruits = [];
    fruits.forEach(fruit => {
        if (fruit.checked) {
        selectedFruits.push(fruit.value);
        }
    });
    
    if (selectedFruits.length > 0) {
        result.textContent = `選択した果物: ${selectedFruits.join(', ')}`;
    } else {
        result.textContent = '果物が選択されていません。';
    }
});