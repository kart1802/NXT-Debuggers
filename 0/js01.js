// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
// 1st js file
function cancel(e) {
    e.parentNode.parentNode.removeChild(e.parentNode)
}

function next(copy, name) {
    var x = document.getElementById(copy).firstElementChild
    var y = x.cloneNode(true)
    y.innerHTML += '<button type="button" onclick="cancel(this)" class="cancel btn btn-danger btn-lg text-center">Delete ' + name + '</button><br><br>'
    document.getElementById(copy).appendChild(y)
}