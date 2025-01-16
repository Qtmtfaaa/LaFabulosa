function decimalToBinary() {
    decNum = prompt("Introduce un numero decimal para que te lo pase a binario:");
    let binNum = "";
    while (decNum > 0 ){
        let rest = decNum %= 2;
        binNum = binNum += rest;
        decNum = decNum /= 2;
    return binNum;
    } 
}
document.write(decimalToBinary())