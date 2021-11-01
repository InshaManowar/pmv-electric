var a = parseInt(30);
var b = parseInt(4);
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
    // e = 30 * a;
    document.getElementById("p1").innerHTML = sum.toString();


    var sum1 = sum / c;
    sum1 = Math.round((sum1 + Number.EPSILON) * 100) / 100
    document.getElementById("p2").innerHTML = sum1.toString();


    var sum2 = sum / 8;
    var e = sum / 8;
    document.getElementById("p3").innerHTML = sum2.toString();
    sum2 = Math.round((sum2 + Number.EPSILON) * 100) / 100

    // var g = e / 8;


    var sumnew = ((sum1 * b) - ((e * d) / 100)) * 12;
    sumnew = Math.round((sumnew + Number.EPSILON) * 100) / 100
        // var h = f / b;
    document.getElementById("p4").innerHTML = sumnew.toString();

    var sumnew1 = ((18.74 * sum1) - ((e * d) / 100)) * 12;
    sumnew1 = Math.round((sumnew1 + Number.EPSILON) * 100) / 100
        // var h = f / b;
    document.getElementById("p5").innerHTML = sumnew1.toString();


}

// function disp1() {
//     var sum1 = e / c;
//     f = e / c;
//     document.getElementById("p2").innerHTML = sum1.toString();
// }

// function disp2() {
//     var sum2 = e / 8;
//     g = e / 8;
//     document.getElementById("p3").innerHTML = sum2.toString();
// }


// function disp3() {
//     var sum3 = f / b;
//     h = f / b;
//     document.getElementById("p7").innerHTML = sum3.toString();
// }

// function disp4() {
//     var sum4 = (g / d) / 100;
//     i = (g / d) / 100;
//     document.getElementById("p8").innerHTML = sum4.toString();
// }


// function disp6() {
//     var sum6 = 18.74 / ((30 * a) / c);
//     document.getElementById("p10").innerHTML = sum6.toString();
// }

// function disp7() {
//     var sum7 = 0.92 / g;
//     k = 0.92 / g;
//     document.getElementById("p11").innerHTML = sum7.toString();
// }

// function disp8() {
//     var sum8 = h * 12;
//     document.getElementById("p12").innerHTML = sum8.toString();
// }

// function disp9() {
//     var sum9 = 12 * i;
//     document.getElementById("p13").innerHTML = sum9.toString();
// }

// function disp10() {
//     var sum10 = j * 13;
//     document.getElementById("p14").innerHTML = sum10.toString();
// }

// function disp11() {
//     var sum11 = k * 13;
//     document.getElementById("p15").innerHTML = sum11.toString();
// }