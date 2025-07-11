/*
プレイヤーのHPと敵の攻撃力を渡すと、攻撃を受けた後のHPを計算して返す関数 calcDamage(playerHp, enemyAtk) を作成しよう。
もし攻撃を受けた結果、HPが0以下になったら「戦闘不能」と表示しよう。
*/
function calcDamage(playerHp, enemyAtk){
    
    playerHp = playerHp - enemyAtk;

    if (playerHp <= 0) {
        console.log("戦闘不能");
        return playerHp = 0;
    } else {
        console.log("現在のHPは" + playerHp + "です。");
        return playerHp;
    }
}

const maxHp = 100;
let hp = maxHp

hp = calcDamage(hp, 10);
hp = calcDamage(hp, 90);