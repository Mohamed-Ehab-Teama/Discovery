let ul_links = document.getElementById('links')
let toggle_button = document.getElementById('tog-btn')
// ul_links.style.height = '0px'
ul_links.style.display = 'none'

function toggleView()
{
    // if (ul_links.style.height == '0px')
    if (ul_links.style.display == 'none')
    {
        // ul_links.style.height = '200px'
        ul_links.style.display = 'flex'
        toggle_button.className = 'fa fa-car'
        
    }else {
        // ul_links.style.height = '0px'
        ul_links.style.display = 'none'
        toggle_button.className = 'fa fa-user'
    }
}