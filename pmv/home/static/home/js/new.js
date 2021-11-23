var a = parseInt(30);
var b = parseInt(4.0);
var c = parseInt(30);
var d = parseInt(15);

function test() {
    console.log("test");
    console.log(vol.value);
    a = parseInt(vol.value);
    disp();


}

function test1() {
    console.log("test1")
    b = parseInt(vol1.value);
    console.log(b)
    disp();

}

function test2() {
    console.log("test2");
    c = parseInt(vol2.value);
    console.log(c);
    disp();


}

function test3() {
    console.log("test3");
    d = parseInt(vol3.value);
    console.log(d);
    disp();

}

function disp() {

    var sum = (30 * a) * 12;
    document.getElementById("p1").innerHTML = sum.toString();

    var sumnew = ((((30 * a) * 12) / c) * b) - ((sum * (d / 100)) / 8);
    sumnew = Math.round((sumnew + Number.EPSILON) * 100) / 100;
    document.getElementById("p2").innerHTML = sumnew.toString();


    var sumnew1 = ((18.74 * sum) / c) - ((sum * 0.92) / 8);
    sumnew1 = Math.round((sumnew1 + Number.EPSILON) * 100) / 100;
    document.getElementById("p3").innerHTML = sumnew1.toString();

}