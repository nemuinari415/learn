try {

    const num = "3";

    if ( typeof num !== "number" ) {
        throw "numは数値型でなければなりません";
    }

    console.log(`${ num } x 5 = ${ num * 5 }`);
} catch ( error ) {

    console.error( error );
}