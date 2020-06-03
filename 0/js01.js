// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
// 1st js file
function cancel(e) {
    e.parentNode.parentNode.removeChild(e.parentNode)
}

function copy(copy, name) {
    const z = document.getElementById(copy).firstElementChild
    const a = z.cloneNode(true)
    a.innerHTML += '<br><button type="button" onclick="cancel(this)" class="cancel btn btn-danger btn-lg text-center">Delete ' + name + '</button><br>'
    document.getElementById(copy).appendChild(a)
}

function achievement(e) {
    var x = e.parentNode.firstElementChild.cloneNode(true)
    x.innerHTML += '<button type="button" onclick="cancel(this)" class="cancel btn btn-danger btn-md text-center">Delete Achievement</button>'
    e.parentNode.insertBefore(x, e)
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
    if (i === 5) {
        document.getElementById('submit').removeAttribute('hidden', true)
        document.getElementById('next').setAttribute('hidden', true)
    }
    var list = document.getElementsByTagName('input')
    for (var num = 0; num < list.length; num++) {
        if (list[num].value == 0) {
            $('.cancel').trigger('click')
        }
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
    if (i < 5) {
        document.getElementById('submit').setAttribute('hidden', true)
        document.getElementById('next').removeAttribute('hidden', true)
    }
    var list = document.getElementsByTagName('input')
    for (var num = 0; num < list.length; num++) {
        if (list[num].value == 0) {
            $('.cancel').trigger('click')
        }
    }
}