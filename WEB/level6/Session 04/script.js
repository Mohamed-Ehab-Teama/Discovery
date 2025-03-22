
// localStorage.setItem('name', 'Mohamed')
// localStorage.setItem('pass', '123456')
// localStorage.setItem('age', '22')

// let userName = localStorage.getItem('name')
// let userPass = localStorage.getItem('pass')
// let userAge = localStorage.getItem('age')
// console.log(userName)
// console.log(userPass)
// console.log(userAge)


// // -----------------------------------
// console.log("========================================")
// // -----------------------------------

// sessionStorage.setItem('name', "Ali")
// sessionStorage.setItem('age', "25")
// sessionStorage.setItem('email', "ali@ali,com")

// let sessionName = sessionStorage.getItem('name')
// let sessionAge = sessionStorage.getItem('age')
// let sessionEmail = sessionStorage.getItem('email')

// console.log(sessionName)
// console.log(sessionEmail)
// console.log(sessionAge)

// console.log("========================================")

function ask()
{
    let my_name = prompt("Enter Your Name")
    localStorage.setItem('name', my_name)

    let my_age = prompt("Enter Your Age")
    localStorage.setItem('age', my_age)

    let my_email = prompt("Enter Your Email")
    localStorage.setItem('email', my_email)

}

function show()
{
    my_name = localStorage.getItem('name')
    my_age = localStorage.getItem('age')
    my_email = localStorage.getItem('email')

    alert(" Your name is " + my_name)
    alert(" Your age is " + my_age)
    alert(" Your email is " + my_email)
}