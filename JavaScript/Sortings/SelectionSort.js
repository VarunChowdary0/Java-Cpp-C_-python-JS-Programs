const  prompt = require('prompt-sync')({sigint:true});
const n = parseInt(prompt("Enter no.of elements: "));
const arr = []
let min_idx;
console.log("Enter elements line by line: ");
for(i=0;i<n;i++){
    const a = parseInt(prompt());
    arr.push(a);
}
for(i=0;i<n;i++){
    min_idx = i;
    for(j=i;j<n;j++){
        if(arr[min_idx] > arr[j]){
            min_idx = j;
        }
    }
    let temp = arr[min_idx];
    arr[min_idx] = arr[i] ;
    arr[i] = temp;
}
console.log("Sorted Array : "+arr)
