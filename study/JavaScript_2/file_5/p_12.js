const fruits = ["りんご", "ばなな", "さくらんぼ"];

fruitsDesc = Reflect.getOwnPropertyDescriptor(fruits, "length");
console.log(fruitsDesc);