const heading = document.querySelector('#heading');

/* 文字をふわりと表示させる
const keyframes = {
    opacity: [0, 1],
    translater: ['0 50px', 0],
};
const options = {
    duration: 2000,
    esing: 'ease',
};
*/
/* くるっと回転させる。
const keyframes = {
    opacity: [0, 1],
    rotate: ['x 360deg', 0],
};

const options = {
    duration: 2000,
    esing: 'ease',
};
*/
/* 色が変化していくアニメーション 
const keyframes = {
    color: ['#f66', '#0c6', '#0bd']
};
const options = {
    duration: 8000,
    direction: 'alternate',
    iterations: Infinity,
};
*/
/* 背景が伸びる見出し
const keyframes = {
    color: ['transparent', '#fff'],
    backgroundPosition: ['100% 0', '0 0'],
};
const options = {
    duration: 1000,
    easing: 'ease',
};
*/

heading.animate(keyframes, options);
