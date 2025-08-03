let a = 0;
a += 3;
a *= 4;
a /= 2;
a %= 5;
console.log("a: ", a); // Output: a:  2

console.log( (0 || undefined) && "こんにちわ" ); // Output: undefined
console.log( !(0 && undefined) && "こんにちわ" ); // Output: こんにちわ

console.log( null ? "リンゴ" : "バナナ" ); // Output: バナナ
console.log( null ?? "パイナップル" ); // Output: パイナップル
console.log( {apple: "リンゴ"} ?.fruit ?? "バナナ" ); // Output: バナナ