/*
- 猫 35%、犬 30%、きりん 20%、その他 15%
- 円グラフのオプションには 幅100%、高さ300px を指定
*/
var animalData = {
    labels: ['猫', '犬', 'きりん', 'その他'],
    series: [35, 30, 20, 15]
};

var animalOptions = {
    width: '100%',
    height: '300px'
};

new Chartist.Pie('.animal-chart', animalData, animalOptions);