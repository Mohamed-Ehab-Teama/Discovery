let links = document.getElementById('nav_links')
links.style.height = "0px"

function toggleView()
{
    if (links.style.height == '0px')
    {
        links.style.height = '200px'
    }else {
        links.style.height = '0px'
    }
}