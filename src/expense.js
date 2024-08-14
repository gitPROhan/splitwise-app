function displayGroups(){
    document.getElementById('form1').style.display = 'inline-block';
}

function displayFriends(){
    document.getElementById('form2').style.display = 'inline-block';
}

function hideGroups(){
    document.getElementById('form1').style.display = 'none';
}

function hideFriends(){
    document.getElementById('form2').style.display = 'none';
}

function displayFriends2(){
    document.getElementById('form3').style.display = 'inline-block';
}
function hideFriends2(){
    document.getElementById('form3').style.display = 'none';
}

function selectPerson()
{
    document.getElementById('sel').style.cursor="pointer";
    var name=document.getElementById('sel').getAttribute('data-value');
    document.getElementById('name').textContent=name;

}

function selectGrp(button)
{
    var row=button.parentNode.parentNode;
    document.getElementById('grp').style.cursor="pointer";
    var name=document.getElementById('grp').getAttribute('data-value');
    document.getElementById('name').textContent=name;

}

function cur()
{
    document.getElementById('sel').style.cursor="pointer";
}