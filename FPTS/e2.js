// ex2 - write a function that function that returns Either on square root
console.log(Math.sqrt(-1)); // NaN
var leftz = function (l) { return ({
    _tag: "leftz",
    value: l,
}); };
var rightz = function (r) { return ({
    _tag: "rightz",
    value: r,
}); };
function square_root(x) {
    if (x < 0) {
        return leftz("i");
    }
    else {
        return rightz(Math.sqrt(x));
    }
}
console.log(square_root(2));
console.log(square_root(0));
console.log(square_root(-3));
