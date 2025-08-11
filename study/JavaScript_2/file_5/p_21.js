const fruits = { apple: "りんご", banana: "ばなな", cherry: "さくらんぼ" };
for( const [ key, value ] of Object.entries( fruits ) ) {
    console.log( key, value );
}