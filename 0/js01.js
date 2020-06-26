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

//Add Education
var Edu = 0;
function addEduSub(){
    document.getElementById(`education${Edu}`).removeAttribute('hidden' , true);
    Edu++;
}

//Remove Education
const removeEduSub = (education, id) =>{
    document.getElementById(education).setAttribute('hidden',true);
    var rmEdu = document.getElementById(education).childNodes ;
    rmEdu[2].value = ""; rmEdu[8].value = ""; rmEdu[15].value = ""; rmEdu[23].value = ""; rmEdu[30].value = ""; rmEdu[38].value = "";
   
    Edu--;

    const abc = document.getElementsByClassName("abc");
    console.log(abc);
    for (let i = 0; i < abc.length; i++) {
        abc[i].value = "";
    }
}





//Add Achievement for first list item in education
var eduA1 = 0;
function addEduAchieve1(){
    document.getElementById("eduAchievement"+ eduA1).removeAttribute('hidden',true);
    eduA1++;
}
// Remove Achievement for first list item in education
const removeEduAchieve1 = (eduAchieve1) =>{
    document.getElementById(eduAchieve1).setAttribute('hidden',true);
    document.getElementById(eduAchieve1).firstChild.value = "";
    eduA1--;
}

//Add Achievement for second list item in education
var eduA2 = 3;
function addEduAchieveSub0(){
    document.getElementById("eduAchievement"+ eduA2).removeAttribute('hidden',true);
    eduA2++;
}
// Remove Achievement for second list item in education
const removeEduAchieveSub0 = (eduAchieve2) =>{
    document.getElementById(eduAchieve2).setAttribute('hidden',true);
    document.getElementById(eduAchieve2).firstChild.value = "";
    eduA2--;
}

//Add Achievement for third list item in education
var eduA3 = 6;
function addEduAchieveSub1(){
    document.getElementById("eduAchievement"+ eduA3).removeAttribute('hidden',true);
    eduA3++;
}
// Remove Achievement for third list item in education
const removeEduAchieveSub1 = (eduAchieve3) =>{
    document.getElementById(eduAchieve3).setAttribute('hidden',true);
    document.getElementById(eduAchieve3).firstChild.value = "";
    eduA3--;
}

//Add Achievement for fourth list item in education
var eduA4 = 9;
function addEduAchieveSub2(){
    document.getElementById("eduAchievement"+ eduA4).removeAttribute('hidden',true);
    eduA4++;
}
// Remove Achievement for fourth list item in education
const removeEduAchieveSub2 = (eduAchieve4) =>{
    document.getElementById(eduAchieve4).setAttribute('hidden',true);
    document.getElementById(eduAchieve4).firstChild.value = "";
    eduA4--;
}




//Add Skill
var sId = 0;
function addSkill(){
document.getElementById("skill"+ sId).removeAttribute('hidden',true);
sId++;

}
//Delete Skill
const removeSkill = (skill) => {
    document.getElementById(skill).setAttribute('hidden',true);
    document.getElementById(skill).firstChild.value = "";
    sId--;
   
}
//Add Hobby
var hId = 0 ;
function addHobby(){
    document.getElementById("hobby" + hId).removeAttribute('hidden',true);
    hId++;
}
//Delete Hobby
const removeHobby = (hobby) => {
    document.getElementById(hobby).setAttribute('hidden',true);
    document.getElementById(hobby).firstChild.value = "";
    hId--;
}


//Add Project
var pId = 0 ;
function addProject(){
    document.getElementById("Project" + pId).removeAttribute('hidden',true);
    pId++;
}
//Remove Project
const removeProject = (Project) => {
    document.getElementById(Project).setAttribute('hidden',true);
    var rP = document.getElementById(Project).childNodes ;
    rP[2].value =""
    rP[4].value =""
    rP[6].value =""
    rP[8].value =""
    pId--;
}

//Add Internship
var iId = 0;
function addInternship(){
    document.getElementById("Internship" + iId).removeAttribute('hidden',true);
    iId++;
} 
//Remove Internship
const removeInternship = (Internship) => {
    document.getElementById(Internship).setAttribute('hidden',true);
    var rP = document.getElementById(Internship).childNodes ;
    rP[2].value =""
    rP[4].value =""
    rP[6].value =""
    rP[8].value =""
    iId--;
}

//Add Achievement
var aId = 0 ;
function addAchieve(){
    document.getElementById("Achievement" + aId).removeAttribute('hidden',true);
    aId++;
}
//Remove Achievement
const removeAchieve = (Achievement) => {
    document.getElementById(Achievement).setAttribute('hidden',true);
    document.getElementById(Achievement).firstChild.value = "";
    aId--;
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
  

}

