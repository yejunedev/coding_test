var fs = require("fs");
var input=fs.readFileSync(0, 'utf-8').toString().trim();

function f(n){
    if(n<=1) return 1;
    return n*f(n-1);
}

var n = parseInt(input);
var ans = f(n);
console.log(ans);