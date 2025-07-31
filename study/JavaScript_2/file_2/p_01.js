let person = {
    hello: function() {
        console.log("こんにちわ");
    }
}
person.hello(); // > こんにちわ

person.bye = function() {
    console.log("さようなら");
}
person.bye(); // > さようなら

person.hello = function() {
    confirm("Hello");
}
person.hello(); // > Hello