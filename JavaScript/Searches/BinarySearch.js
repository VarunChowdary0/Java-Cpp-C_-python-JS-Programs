const prompt = require('prompt-sync')({sigint:true}); // for input
const n = prompt("Enter no of elements: ")
let arr = [];
console.log("Enter elements in accending order : --| ");
for(i=0;i<n;i++){
    const a = prompt();
    arr.push(parseInt(a));
}// parseInt() => type castes string to int; 
const x = prompt("Enter the element to be found: ");
let found = false;
let start=0;
let mid;
let end = n;
while(true){
    mid = Math.floor((start+end)/2);
    if(parseInt(x) === arr[mid]){
        console.log("Found at index "+mid+" !!");
        found = true;
        break;
    }
    if(start = mid){
        break;
    }
    else if( parseInt(x) > arr[mid]){
        start = mid;
    }
    else{
        end = mid;
    }
}
if(!found){
    console.log("Element not found !!");
}
