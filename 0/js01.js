// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
function cancel(id) {
    var y = document.getElementById(id)
    y.innerHTML = ''
}

function next(copy, paste) {
    var x = document.getElementById(copy)
    var y = document.getElementById(paste)
    y.innerHTML = x.innerHTML
}