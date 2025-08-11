const map = new Map;
map.set( "apple", "りんご" );
map.set( "banana", "バナナ" );

for( const [ key, value ] of map ) {
    console.log( key, value );
}