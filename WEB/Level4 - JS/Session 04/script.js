// Arrays in JavaScript

let numbers = [1, 2, 3, 4, 5];
let floats = [1.5, 2.4, 3.4, 4.4, 5.4];
let booleans = [true, true, true, false, false];
let names = ['Omar', "Ali", "mai"];
let colors = ['red', true, 2.5, 15, false, 2025];

// console.log( colors );

// var text = colors.join("--")
// console.log(text)

// console.log( floats.find( function(x) {
//     return x > 4.5
// }))

// console.log( colors[2] );
// console.log( colors[4] );

// console.log( colors.length );

// colors.push("Yellow");
// colors.push("Red", "Green")

// colors.pop()
// colors.pop()
// colors.pop()

// console.log(colors)

// const arr = ["One", "Two", "Three", "Four", "Five", 'Six', "Seven"];

// for(i = 0; i < arr.length; i++)
// {
//     console.log( arr[i] )
// }

// for( i = 0; i < 5; i++ )
// {
//     console.log( arr[i] )
// }


let my_car = { 
    "Name" : "Fiat", 
    "Model" : 2015,
    'color' : "White"
}
console.log(my_car)

console.log( my_car['Name'] )
console.log( my_car.Name )

my_car.Name = "Fiat 128"
my_car['color'] = "Silver"

my_car.logo = "FiA"
my_car['number'] = 5024

console.log(my_car)