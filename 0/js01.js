// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
// 1st js file
function cancel(e) {
    e.parentNode.parentNode.removeChild(e.parentNode)
}
 
var x = `
<label for="ed1">Name of Institution :</label><input class="container" size="50" type="text"
    id="ed1" placeholder="Veermata Jijabai Technological Institute" size="100" required
    class="col-sm-9 col-md-6 col-lg-12"> <br>
<div class="row">
    <div class="w-65 p-3">
        <span><label for="ed2">Admission Year:</label><br>
            <input class="duration" type="date" id="ed2" placeholder="DD-MM-YYYY"
                required=""></span><br>
        <span><label class="grad_year" for="ed3">Year of Graduation(Or
                Expected):</label><br><input type="date" class="duration" id="ed3"
                required></span>
    </div><br>
    <div class="w-65 p-3">
        <label for="ed4">CGPA:</label><br><span class="text-light" style="font-size: medium;">If
            not applicable enter " - "</span><br><input type="number" id="ed4"
            placeholder="Out Of 10"><br>
        <label for="ed7">Percentage</label><br><span class="text-light"
            style="font-size: medium;">If not applicable enter " - "</span><br><input
            type="number" id="ed7" placeholder="91%"><br>
    </div>
</div>
<label for="ed5">Core Classes:</label><br>
<span class="text-light" style="font-size: medium;">This input field is only for
    undergraduate/graduate courses or beyond</span>
<textarea class="container" rows="2" cols="100" size="55" id="ed5"
    placeholder="Thermodynamics,Fluid Mechanics,etc. for mechanical degree"
    class="col-sm-9 col-md-6 col-lg-12"></textarea>
<label for="ed6">Associtations /Committees:</label><br>
<span class="text-light" style="font-size: medium;">Activities done/reponsibilities undertaken
    in a particular association in college</span><br>
<ol class="eduachieve container">
    <li class="firstlistitem"><textarea rows="2" cols="100" id="ed6" placeholder="Achievement"
            class="col-sm-9 col-md-6 col-lg-12"></textarea>

    </li>
    <button type="button" onclick="achievement(this)"
        class="next rotate button btn btn-secondary btn-md text-center achbtn">&crarr;Add
        Achievement</button>
    <br>
</ol><br>
<br><button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-lg text-center">Delete Education</button><br>

`

function edu_copy(edu_copy, education) {
    const node = document.createElement("LI")
    node.innerHTML = x 
    document.getElementById(edu_copy).appendChild(node)
        
}

function copy(copy,name){
    const z = document.getElementById(copy).firstElementChild
    const a = z.cloneNode(true)
    a.innerHTML += `<br><button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-lg text-center">Delete `+ name +`</button><br>`
    document.getElementById(copy).appendChild(a)

}

function achievement(e) {
    var x = e.parentNode.firstElementChild.cloneNode(true)
    x.innerHTML += '<button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-md text-center">Delete Achievement</button>'
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