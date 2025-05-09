/*
    HTML : to define the content of web pages
    CSS : to specify the layout of web pages
    JavaScript : to program the behavior of web pages


Introduction to JavaScript:
    Explanation: JavaScript is a programming language that allows you to implement complex features on web pages, making them interactive and dynamic.
    It's widely used for client-side development.

The difference between client-side and server-side:
    Client-side: Code runs on the user's device (e.g., computer or smartphone).
    Server-side: Code runs on a web server.
    Client-side handles user interactions and rendering within the browser.
    Server-side takes care of data processing and database interactions

Linking JavaScript with HTML:
    JavaScript can be linked to an HTML file either inline within
    `<script>` tags or as an external file using :
    `<script src="path/to/file.js"></script>` tag. It's generally a best practice to link JavaScript files externally for better organization and maintainability.
JS in head or in body:
    <script> document.getElementById("demo").innerHTML = "Paragraph changed."; </script>
JS from external files:
    <script src="myScript.js" ></script>

----------------------------------------------------------------------------------------------------------

Output in Console:
    Usage of `console.log()`: This function is used to display messages in the browser's console, which is useful for debugging and testing.
    Ex) console.log(5 + 6);

Note
    JavaScript does not have any print object or print methods.
    You cannot access output devices from JavaScript
    window.print() method in the browser to print the content of the current window

----------------------------------------------------------------------------------------------------------

Variables:
    Variables are containers for storing data values. 
    JavaScript allows you to define variables using the `var`, `let`, or `const` keywords.

    var : Function-scoped. This means that a variable is available throughout the function in which it is declared
        - Can be re-declared and re-assigned within its scope
        - Variables declared with var are 'hoisted' to the top of their scope and initialized with 'undefined'

    let : Block-scoped. available within the block (e.g., {}) in which they are declared
        - Can be re-assigned but not re-declared within the same scope
        - 'hoisted' but are 'not initialized'
        - Accessing them before declaration results in a 'ReferenceError'

    const : Block-scoped. available within the block (e.g., {}) in which they are declared
        - Cannot be re-assigned or re-declared. The value must be assigned at the time of declaration
        - 'hoisted' but are 'not initialized'
        - Accessing them before declaration results in a 'ReferenceError'


    'Hoisting' : Hoisting is a JavaScript mechanism where variable and function declarations are moved to the top of their containing scope during the compilation phase. This behavior allows variables and functions to be used before they are actually declared in the code


    var: Generally avoided in modern JavaScript due to its function-scoped nature which can lead to bugs.
    let: Used for variables that need to be re-assigned.
    const: Used for variables that should not be re-assigned


----------------------------------------------------------------------------------------------------------
Variable Naming Conventions:
    In JavaScript, following consistent variable naming conventions is crucial for writing clean and maintainable code. Here are some key conventions:
        - Variable names can contain letters, digits, underscores, and dollar signs
        - Descriptive Names: Choose names that clearly describe the variable’s purpose
        - Case Sensitivity: Variable names are usually case-sensitive
        - No Reserved Words: Avoid using language keywords or reserved words
        - Start with a Letter: Typically, variable names should start with a letter (a-z, A-Z) or an underscore (_), but not a number
        - No Special Characters: Avoid special characters like @, #, %, etc


Common Naming Conventions:
    Camel Case: Used in languages like JavaScript and Java.
        Example: myVariableName

    Snake Case: Common in Python.
        Example: my_variable_name

    Pascal Case: Often used for class names in languages like C#.
        Example: MyVariableName

    Kebab Case: Mostly used in URLs or CSS.
        Example: my-variable-name


----------------------------------------------------------------------------------------------------------
Comments: Lines that ignored by the compiler
    Single-line comments => //
    multi-line comments => / * * /
----------------------------------------------------------------------------------------------------------
Data Types: 
Data types define the type of data a variable can hold, such as numbers, strings, and booleans.

- Number: Represents numeric values. 
- String: A sequence of characters.
- Null: Represents an empty or unknown value.
- NaN: Represents a "Not-a-Number" value.
- Boolean: Represents `true` or `false`.

----------------------------------------------------------------------------------------------------------
Basic Operators:
    Basic mathematical operations include addition +, subtraction -, multiplication *, division /, and assignment =.

*/