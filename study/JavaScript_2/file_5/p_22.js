const obj = {
    prop1: 10,
    prop2: 20,
    prop3: "文字列",
    skip: 20,
    prop4: true,
    prop5: 23,
    prop6: 47,
};

let sum = 0;
const props = Object.keys(obj);

for(const key of props) {
    let value = obj[ key ];
    if (typeof value === "number" && key !== "skip") {
        sum += value;
    }
}
console.log(sum);