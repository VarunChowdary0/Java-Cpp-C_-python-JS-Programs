const prompt = require('prompt-sync')({sigint:true});

const base = parseInt(prompt("Enter base: "));
const power = parseInt(prompt("Enter power: "));

const getPower = (base,power) =>{
    if(power === 0  ){
        return 1;
    }
    return getPower(base,power-1) * base ;
}
const Res = getPower(base,power);
console.log(base+"^"+power+" = "+Res);