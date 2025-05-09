/*
Template literals: provide a more flexible way to work with strings.
    They are enclosed by backticks (``) instead of single or double quotes
    to use variable inside the `` => ${}

*/

// var num1 = 9;
// var num2 = 5;

// let result = num1 + num2;

// console.log(`The Addition of ${num1} and ${num2} is ${result} `);

// console.log('Hello All and Welcome Mohamed');
// console.log('Hello All and \n Welcome Mohamed');

// console.log(`Hello All and
//             Welcome Mohamed`);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
The Document Object Model (DOM) is a programming interface for web documents, representing the structure of a document as a tree of objects.
    It allows JavaScript to access and manipulate HTML and CSS, dynamically updating content and style.
    returns null if not found.
*/
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Element by ID:
<div id="myDiv">Hello, world!</div>;
myHeading = document.getElementById("myDiv");
console.log(myDiv.innerText);
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// The querySelector() method in JavaScript is used to select the first element that matches a specified CSS selector or group of selectors within the document. If no matches are found, it returns null.

const firstParagraph = document.querySelector("p"); // Selects the first <p> element in the document

const myElement = document.querySelector("#myElement"); // Selects the element with the ID 'myElement'

const x = document.querySelector(".example"); // Get the first element with class="example":

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// The querySelectorAll() method returns all elements that matches a CSS selector(s).
// The querySelectorAll() method throws a SYNTAX_ERR exception if the selector(s) is invalid

document.querySelectorAll(".example"); // Select all elements with class="example":

const nodeList = document.querySelectorAll("p");
nodeList[0].style.backgroundColor = "red";

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Inner Text : A property used to set or get the text content of an HTML element, excluding any HTML tags.
// Inner HTML : A property used to set or get the HTML content within an element, allowing for the insertion of HTML tags and content.
let html = document.getElementById("myP").innerHTML;
document.getElementById("demo").innerHTML = "I have changed!";

let text = document.getElementById("myP").innerText;
document.getElementById("demo").innerText = text;
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Style : An object representing the inline styles of an HTML element, allowing for the direct manipulation of CSS properties via JavaScript.
element.style.backgroundColor = "red";
document.getElementById("myH1").style.color = "red";
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Class List : A property that provides methods to manipulate the class attribute of an element, including adding, removing, and toggling classes.
// It is useful for dynamically changing the appearance and behavior of elements.

const list = document.getElementById("myDIV").classList;
document.getElementById("demo").innerHTML = list;


let numb = element.classList.length; // How many class names the element have:

element.classList.add("myStyle", "anotherClass", "thirdClass");

element.classList.remove("myStyle", "anotherClass", "thirdClass");

let cl = element.classList.contains("myStyle"); // True or False
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
