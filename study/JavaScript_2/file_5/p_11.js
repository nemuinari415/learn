const obj = {
    prop1: "これは列挙可能プロパティです。"
};

Reflect.defineProperty(obj, "prop2", {
    value: "これは列挙不可プロパティです。",
    enumerable: false
});

for( const key in obj ) {
    console.log( key, obj[ key ]);
}
