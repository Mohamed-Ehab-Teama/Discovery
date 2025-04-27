// let num1 = 10
// let num2 = 20
// console.log(num1 + num2)
// console.log(num1 - num2)
// console.log(num1 * num2)
// console.log(num1 / num2)

// function addTwoNumbers ( number1 = 0, number2 = 0 ) {
//     console.log( number1 + number2  )
//     console.log( "Working" )
// }

// function addTwoNumbers ( number1 = 0, number2 = 0 ) {
//     // console.log( number1 + number2 )
//     return number1 + number2 
//     console.log("Eng Hanin")
// }

// addTwoNumbers(400, 50)
// console.log( addTwoNumbers(400, 50) )

// let res = addTwoNumbers(400, 50)
// console.log(res)

// addTwoNumbers()
// console.log("------------------------")
// addTwoNumbers(400)
// console.log("------------------------")

// function evenOrOdd (num)
// {
//     if( num % 2 == 0 )
//     {
//         console.log("EVEN")
//     }else {
//         console.log("ODD")
//     }
// }

// evenOrOdd(70)

function calculator ( operator, num1, num2 )
{
    if(operator == '+')
    {
        console.log( num1 + num2)
    }
    else if (operator == '-') 
    {
        console.log( num1 - num2)
    }else{
        console.log( "Invlaid operator")
    }
}

calculator( '*' , 70, 80)