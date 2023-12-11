const prompt = require('prompt-sync')({sigint:true});

const n = parseInt(prompt("Enter N: "));

const Fibbo = (N) =>{
    if(N==0){
        return 0;
    }
    else if(N === 1) {
        return 1;
    }
    return Fibbo(N-1) + Fibbo(N-2) ;
}
const Res = Fibbo(n);
console.log(n+"th Fibbonaci Term = "+Res);