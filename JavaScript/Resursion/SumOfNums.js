const prompt = require('prompt-sync')({sigint:true});

const n = parseInt(prompt("Enter N: "));

const getSum = (N) =>{
    if(N === 0){
        return 0;
    }
    return getSum(N-1) + N ;
}
const Res = getSum(n);
console.log("Sum: "+Res);