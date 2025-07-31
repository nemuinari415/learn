let obj = {
    prop: true,
    subobj : {
        val: 100,
        val2: 1000
    },
    greeting: "こんにちわ"
};
console.log(obj.prop); // true
console.log(obj.subobj.val); // 100
console.log(obj.subobj.val2); // 1000
console.log(obj.greeting); // こんにちわ