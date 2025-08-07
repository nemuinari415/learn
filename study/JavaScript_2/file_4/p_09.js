try {
    const greeting = "こんにちは";
    if ( typeof greeting === "string" ) {
        console.log(`${greeting}、いい天気ですね`);
    }
    else {
        throw "不正なデータ型です";
    }
} catch ( error ) {
    console.error( error );
}