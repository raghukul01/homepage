function click_button(){
var x=document.getElementById('leftbut')
if(x.value==='<')x.value='>';
else x.value='<';
if(document.getElementById('division2').style.display==="none")
document.getElementById('division2').style.display="block";
else 
document.getElementById('division2').style.display="none";
}
