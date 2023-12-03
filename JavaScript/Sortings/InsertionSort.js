const prompt = require('prompt-sync')({sigint:true})

const arr = [];
const n = parseInt(prompt("Enter number of elements: "));

console.log("Enter elements into the Array ")
for(i=0;i<n;i++){
    const a = parseInt(prompt());
    arr.push(a);
}

for(i=1;i<n;i++){
    let j = i ;
    while( j && (arr[j-1]>arr[j])){
        const temp = arr[j];
        arr[j] = arr[j-1];
        arr[j-1] = temp;
        j--;
    } 
}
console.log("Elements sorted using Insetion : "+arr);