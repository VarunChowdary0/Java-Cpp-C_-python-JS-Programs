const prompt = require('prompt-sync')({sigint:true});
let n = prompt("Enter no of elements: ");
let arr = [];
console.log("Enter elements : ---| ");
for(i=0;i<n;i++){
    let a = prompt();
    arr.push(a); 
}
const x = prompt("Enter value to be found: ");
let found = false;
for(i=0;i<n;i++){
    if(x === arr[i]){
        console.log("Found at index "+i+" !!");
        found = true;
        break;
    }
}
if(!found){
    console.log("Element Not Found !!");
}