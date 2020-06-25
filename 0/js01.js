// You may make differnt files for differnt purposes.
// REPORT ABOUT CHANGES AND FILE IN WORK TO WHATSAPP GROUP TO KEEP EVERYONE UPDATED
// 1st js file

//VALIDATION
const F_name = document.getElementById('fname');
const L_name = document.getElementById('lname');
const contact = document.getElementById('cnum');
const email = document.getElementById('mail');
const HS = document.getElementById('HnS');
const city = document.getElementById('City');
const state = document.getElementById('State');
const country = document.getElementById('Country');
const pincode = document.getElementById('Pin');
const Name_Insti = document.getElementById('ed1');
const admission = document.getElementById('ed2');
const Grad_Year = document.getElementById('ed3');
const cgpa = document.getElementById('ed4');
const perc = document.getElementById('ed7');
const core_class = document.getElementById('ed5');
const objec = document.getElementById('obj');





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
        class="next rotate button btn btn-secondary btn-md text-center achbtn container m-1">&crarr;Add
        Achievement</button>
    <br>
</ol><br>
<br><button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-lg text-center m-3">Delete Education</button><br>`

function edu_copy(edu_copy, education) {
    const node1 = document.createElement("LI")
    node1.innerHTML = x
    document.getElementById(edu_copy).appendChild(node1)

}
/*var y = `<li class="firstlistitem"><textarea rows="2" cols="100" id="ed6" placeholder="Achievement"
    class="col-sm-9 col-md-6 col-lg-12"></textarea>
</li> 
<button type="button" onclick="achievement(this)"
class="next rotate button btn btn-secondary btn-md text-center achbtn m-1">&crarr;Add
Achievement</button>
<button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-md text-center m-1">Delete Achievement</button>`

function copy_edu_achieve(eduachieve, achievement) {
    const node2 = document.createElement("LI")
    node2.innerHTML = y
    document.getElementById(eduachieve).appendChild(node2)
}*/

/*var y = `<input type="text" class="col" placeholder="Skill"><br>
<button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-lg text-center m-3">Delete Skill</button><br>`*/
var s = 0;
function add_skill(){
document.getElementById("skill"+ s).removeAttribute('hidden',true);
s++
window.s = s
}

const removeSkill = (skill) => {
    document.getElementById(skill).remove();
    window.s = s;
}

function copy(copy, name) {
    const z = document.getElementById(copy).firstElementChild
    const a = z.cloneNode(true)
    a.innerHTML += `<br><button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-lg text-center m-3">Delete ` + name + `</button><br>`
    document.getElementById(copy).appendChild(a)

}

function achievement(e) {
    var x = e.parentNode.firstElementChild.cloneNode(true)
    x.innerHTML += '<button type="button" onclick="cancel(this)" class="rotate cancel btn button btn-danger btn-md text-center m-1">Delete Achievement</button>'
    e.parentNode.insertBefore(x, e)
}
var m = 1;
function removeAlert(){
    document.getElementById("val_alert"+ m).setAttribute('hidden',true)
    m++
    window.m = m
}

var i = 0;
var nex = 0;
var width = 0;
function validAll() {
    //personal
    if (i === 0) {
        if (!F_name.value) {
            document.getElementById("val_alert1").removeAttribute('hidden', true);
        }
        else if (!L_name.value) {
            document.getElementById("val_alert2").removeAttribute('hidden', true);
        }

        else if (!contact.value) {
            document.getElementById("val_alert3").removeAttribute('hidden', true);
        }

        else if (!email.value) {
            document.getElementById("val_alert4").removeAttribute('hidden', true);
        }

        else if (!HS.value) {
            document.getElementById("val_alert5").removeAttribute('hidden', true);
        }

        else if (!city.value) {
            document.getElementById("val_alert6").removeAttribute('hidden', true);
        }

        else if (!state.value) {
            document.getElementById("val_alert7").removeAttribute('hidden', true);
        }

        else if (!country.value) {
            document.getElementById("val_alert8").removeAttribute('hidden', true);
        }

        else if (!pincode.value) {
            document.getElementById("val_alert9").removeAttribute('hidden', true);
        }
        else {
            nextfield();

        }
    }
    //education
    else if (i === 1) {
        if (!Name_Insti.value) {
            document.getElementById("val_alert10").removeAttribute('hidden', true);
        }
        else if (!admission.value) {
            document.getElementById("val_alert111").removeAttribute('hidden', true);
        }
        else if (!Grad_Year.value) {
            document.getElementById("val_alert12").removeAttribute('hidden', true);
        }
        //else if (!cgpa.value || !perc.value) {
        //  document.getElementById("val_alert13").removeAttribute('hidden',true);
        //}
        else if (!core_class.value) {
            document.getElementById("val_alert13").removeAttribute('hidden', true);
        }
        else {
            nextfield();

        }


    }
    //objective
    else if (i === 2) {
        if (!objec.value) {
            document.getElementById("val_alert14").removeAttribute('hidden', true);
        }
        else {
            nextfield();
        }
    }
    else {
        nextfield();
    }


}
function nextfield() {
    /*next fieldset */
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

    /*Increase Progress bar */
    if (width == 0) {
        document.getElementById("back").removeAttribute('disabled', true)
    }
    else {
        document.getElementById("next").removeAttribute('disabled', true)

    }
    nex += 1
    var id = setInterval(fun, 10);
    var ele = document.getElementById("myBar")
    function fun() {
        if (width == 20 * nex) {
            clearInterval(id)
        }
        else {
            width++
            ele.style.width = width + '%'
        }
    }

}










function prefield() {

    /*previous fieldset */
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
    /*decrease progress bar*/
    var ele = document.getElementById("myBar")
    nex -= 1
    var id = setInterval(fun, 10)
    function fun() {

        if (width == 20 * nex) {
            clearInterval(id)

        }
        else {

            width--
            ele.style.width = width + '%'

        }
    }

}

