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

    var sum = 30 * a;
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


    var sum3 = sum1 * b;
    sum3 = Math.round((sum3 + Number.EPSILON) * 100) / 100
        // var h = f / b;
    document.getElementById("p4").innerHTML = sum3.toString();


    var sum4 = (e * d) / 100;
    sum4 = Math.round((sum4 + Number.EPSILON) * 100) / 100
        // var h = f / b;
        // h = h.toFixed(2);
    document.getElementById("p5").innerHTML = sum4.toString();


    var sum5 = 18.74 * sum1;
    sum5 = Math.round((sum5 + Number.EPSILON) * 100) / 100
        // var i = (g / d) / 100;
    document.getElementById("p6").innerHTML = sum5.toString();


    var sum6 = 0.92 * sum2;
    sum6 = Math.round((sum6 + Number.EPSILON) * 100) / 100
    document.getElementById("p7").innerHTML = sum6.toString();


    var sum7 = sum3 * 12;
    sum7 = Math.round((sum7 + Number.EPSILON) * 100) / 100
        // var k = 0.92 / g;
    document.getElementById("p8").innerHTML = sum7.toString();


    var sum8 = sum4 * 12;
    sum8 = Math.round((sum8 + Number.EPSILON) * 100) / 100
    document.getElementById("p9").innerHTML = sum8.toString();


    var sum9 = sum5 * 12;
    sum9 = Math.round((sum9 + Number.EPSILON) * 100) / 100;
    document.getElementById("p10").innerHTML = sum9.toString();


    var sum10 = sum6 * 12;
    sum10 = Math.round((sum10 + Number.EPSILON) * 100) / 100
    document.getElementById("p11").innerHTML = sum10.toString();

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