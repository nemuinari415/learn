let person = { name: "Bob", age: "32", male: true };
delete person.name;
console.log( person ); // { age: "32", male: true }
console.log( typeof person ); // object
console.log( +person.age ); // 32
console.log( person.male ); // true