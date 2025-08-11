const fruits = { apple: "りんご", banana: "バナナ" };
const entries = Object.entries( fruits );
console.log( entries ); // [ [ 'apple', 'りんご' ], [ 'banana', 'バナナ' ] ]

for( const entry of entries ) {
    console.log( entry[0], entry[1] );
}