const fruits = {
    apple: "りんご",
    banana: "ばなな",
    orange: "オレンジ"
}

for ( const key in fruits ) {
    console.log(`キー[${key}] 値:[${fruits[key]}]`);
}