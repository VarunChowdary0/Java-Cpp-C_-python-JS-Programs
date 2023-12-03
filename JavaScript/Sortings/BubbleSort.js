const prompt = require('prompt-sync')({sigint:true})
const n = parseInt(prompt("Enter no of elements: "));
const arr = [];
for(i=0;i<n;i++){
    const a = parseInt(prompt());
    arr.push(a);
}
for(i=0;i<n;i++){
    for(j=i;j<n;j++){
        if(arr[i]>arr[j]){
            const temp = arr[i];
            arr[i] =arr[j] ;
            arr[j] =temp;
        }
    }
}
console.log("Elemets sorted in accending order => ",arr);