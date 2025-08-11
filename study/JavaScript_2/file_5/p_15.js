const map = new Map;
map.set( "apple", "りんご" );
map.set( "banana", "バナナ" );

for( const row of map ) {
    console.log( row[0], row[1] );
}