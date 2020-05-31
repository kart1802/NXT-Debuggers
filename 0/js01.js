// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
//1st js file
function cancel(e) {
    e.parentNode.parentNode.removeChild(e.parentNode)
}

function next(copy, paste) {
    var x = document.getElementById(copy)
    var y = document.getElementById(paste)
    y.innerHTML = x.innerHTML
}