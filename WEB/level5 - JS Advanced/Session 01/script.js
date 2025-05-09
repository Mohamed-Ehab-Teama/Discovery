// Anonymous Functions
// let greet = function () {
//     console.log( "Hello From Anonymous Function" )
// }

// let welcome = function (userName) {
//     return " Welcome " + userName 
// }

// console.log( greet )
// console.log( greet() )
// greet()
// console.log( welcome("Hanin") )

// -----------------------------------

// Map
// const numbers = [4, 9, 16, 25];

// function mul10(num)
// {
//     return num * 10
// }

// let newArr = numbers.map(Math.sqrt)
// console.log( newArr )
// console.log( numbers.map(mul10) )

// -----------------------------------

// Filter
let numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

function ages( num )
{
    return num > 40
}
console.log( numbers.find( ages ) )
console.log( numbers.filter( ages ) )

// -----------------------------------
// ForEach
sum = 0
function sumOfNumbers( num )
{
    sum += num
}
console.log( numbers.forEach(sumOfNumbers) )

console.log(sum)
// -----------------------------------
