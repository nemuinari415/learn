const obj = {
    prop1: 10,
    prop2: 20,
    skip: 20,
    prop3: 23,
    prop4: 47
}
let total = 0;

for ( let key in obj ) {
    if ( key !== "skip" ) {
        total += obj[key];
    }
}

console.log(total); // 100