const s = Symbol();
const obj = { [s]: "Symbol description" };

for( const key in obj ) {
    console.log( key, obj[key] );
}