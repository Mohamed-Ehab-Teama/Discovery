
let post01 = document.getElementById('post01');
let post02 = document.getElementById('post02');
let post03 = document.getElementById('post03');


function showPost01 ()
{
    post01.style.display = 'flex';
    post02.style.display = 'none';
    post03.style.display = 'none';
}

function showPost02 ()
{
    post01.style.display = 'none';
    post02.style.display = 'flex';
    post03.style.display = 'none';
}

function showPost03 ()
{
    post01.style.display = 'none';
    post02.style.display = 'none';
    post03.style.display = 'flex';
}