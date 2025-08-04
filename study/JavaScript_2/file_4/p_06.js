let animal = "動物の名前";

animal = "ウサギ";

switch ( animal ) {
    case "ウサギ":
        console.log("ウサギ");
        animal = "ウマ";
    case "ウマ":
        console.log("ウマ");
        animal = "ゾウ";
    case "ゾウ":
        console.log("ゾウ");
        animal = "キリン";
    default:
        console.log("未知の動物です。");
        break;
}