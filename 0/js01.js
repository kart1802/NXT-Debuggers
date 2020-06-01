// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
// 1st js file
function cancel(e) {
    e.parentNode.parentNode.removeChild(e.parentNode)
}

function copy(copy, name) {
    var z = document.getElementById(copy).firstElementChild
    var a = z.cloneNode(true)
    a.innerHTML += '<button type="button" onclick="cancel(this)" class="cancel btn btn-danger btn-lg text-center">Delete ' + name + '</button><br><br>'
    document.getElementById(copy).appendChild(a)
}

var i = 0

function nextfield() {
    var x = document.getElementsByTagName('fieldset')
    x[i + 1].removeAttribute('hidden', true)
    x[i].setAttribute('hidden', true)
    i++
    window.i = i
    if (i > 0) {
        document.getElementById('back').removeAttribute('hidden', true)
    }
    if (i === 6) {
        document.getElementById('submit').removeAttribute('hidden', true)
        document.getElementById('next').setAttribute('hidden', true)
    }
}

function prefield() {
    var x = document.getElementsByTagName('fieldset')
    if (i !== 0) {
        x[i].setAttribute('hidden', true)
        x[i - 1].removeAttribute('hidden', true)
        i--
        window.i = i
    }
    if (i > 0) {
        document.getElementById('back').removeAttribute('hidden', true)
    } else {
        document.getElementById('back').setAttribute('hidden', true)
    }
    if (i < 6) {
        document.getElementById('submit').setAttribute('hidden', true)
        document.getElementById('next').removeAttribute('hidden', true)
    }
}