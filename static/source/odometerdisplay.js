var n = 0;
var myOdometerDec, myOdometerBin, myOdometerHex;
var keeprunning = false;
function runodometers () {
    keeprunning = true;
    update();
}
function startodometers() {
    myOdometerDec = new OdometerDec(document.getElementById("odometerDecDiv"), {value: n, digits: 8});
    myOdometerBin = new OdometerBin(document.getElementById("odometerBinDiv"), {value: n, digits: 8});
    myOdometerHex = new OdometerHex(document.getElementById("odometerHexDiv"), {value: n, digits: 8});
    runodometers();
}
function stopodometers() {
    keeprunning = false;
}
function update () {
    n=n+0.5
    myOdometerDec.set(n);
    myOdometerBin.set(n);
    myOdometerHex.set(n);

    if (myOdometerBin.get() > 255) {
        n=0;
        myOdometerDec.set(0);
        myOdometerBin.set(0);
        myOdometerHex.set(0);
    }

    if (keeprunning) {
        setTimeout("update()", 250);
    }
}