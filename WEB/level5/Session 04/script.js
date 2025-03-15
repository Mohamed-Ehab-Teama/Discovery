
function saveName()
{
    let name = prompt("Enter Your Name")
    localStorage.setItem( 'user name', name)
}

function getName()
{
    let my_name = localStorage.getItem('user name')
    alert('Welcome ' + my_name)
}

// ============================

function setNameSession()
{
    let color = prompt("Enter Color")
    sessionStorage.setItem('selectedColor', color)
}

function getNameSession()
{
    let my_color = sessionStorage.getItem('selectedColor')
    alert('Welcome ' + my_color)
}

// ============================

function addToCart()
{
    var item = prompt("Enter Item, please!")
    localStorage.setItem( 'item' , item )
    show()
}

function show() {
    let item =  localStorage.getItem('item') 
    document.getElementById('my_list').innerText = item
};