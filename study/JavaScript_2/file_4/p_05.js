let val = "";

if ( "" === val) {
    val = "Hello";
    console.log(val); // Output: Hello
}

if ( val === null ) {
    val = "Hello";
    console.log(val); // This block will not execute
}