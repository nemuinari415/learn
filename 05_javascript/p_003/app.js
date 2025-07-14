// 回復アイテムの使用
function usePotion(hp){
    hp += 30;
    if (hp > 100){
        hp = 100;
    }
    return hp
}

const maxHp = 100;
let hp = maxHp;

console.log("現在のHP" + hp);
hp -= 50;
console.log("50ダメージを受けた!現在のHP" + hp);
hp = usePotion(hp);
console.log("ポーションを使った(30回復)！現在のHP" + hp);