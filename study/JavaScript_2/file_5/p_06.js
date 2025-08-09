const numArray = [ 10, 20, 30 ];

for( let index = 0; index < numArray.length; index++ ) {
    // 配列の値をコンソールに出力
    numArray[ index ] = numArray[ index ] + 10;
}

console.log( numArray ); // Output: [ 20, 30, 40 ]