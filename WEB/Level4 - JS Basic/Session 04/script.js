
// Variable
// var age = 22
// let first_name = "Mohamed"
// const GENDER = 'Male'



// Array
// var class_name = ["Mohamed", "Ali", "Reda", "Mona", "Mai"]  // Strings
// var ages = [22, 19, 23, 25, 30, 21]                         // Integers
// var numbers = [20.1, 19.5, 9.8, 12.4, 14.7]                 // Floats
// var statuses = [false, false , true, false, true]           // Boolean

// let arr = ["Mohamed Ehab", 22, 175.5, true, false, "Ahmed"]          // Mixed

// Print Array Element
// console.log( arr )

// console.log( arr[0] )
// console.log( arr[1] )
// console.log( arr[2] )
// console.log( arr[3] )
// console.log( arr[4] )

let arr = ["Mohamed Ehab", 22, 175.5, true, false, "Ahmed", "Ali", "Reda", "Mona", "Hasnaa"]          // Mixed

// Print Array Length
console.log( arr.length )


// Add and Remove Elements from array
arr.push("Reda Last One")
arr.push("Ali Last One")

arr.pop()
arr.pop()
arr.pop()
arr.pop()

// Print All Array Elements
// for ( let i = 0; i <= 5; i++ )
// {
//     console.log( arr[i] )
// }

for ( let j = 0; j < arr.length; j++ ) {
    console.log( arr[j] )
}