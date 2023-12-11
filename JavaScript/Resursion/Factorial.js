const prompt = require('prompt-sync')({sigint:true});

const n = parseInt(prompt("Enter N: "));

const Fact = (N) =>{
    if(N === 1 || N ==0 ){
        return 1;
    }
    return Fact(N-1) * N ;
}
const Res = Fact(n);
console.log(n+"! = "+Res);