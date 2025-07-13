const width = window.innerWidth; // 画面の幅

if (width < 600) {
  // スマホ表示と判定
  console.log("スマホ表示");

} else {
  // PC表示と判定
  console.log("PC表示")
}

/* 画面サイズが変わったときにも、自動で判定が切り替わる
function checkDisplay() {
  const width = window.innerWidth;

  if (width < 600) {
    console.log("スマホ表示");
  } else {
    console.log("PC表示");
  }
}

window.addEventListener("resize", checkDisplay); // 画面サイズ変更時に実行
checkDisplay(); // 初回実行
*/