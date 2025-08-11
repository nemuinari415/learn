const obj = { prop: "値" };
const propDesc = Reflect.getOwnPropertyDescriptor(obj, "prop");
console.log(propDesc);