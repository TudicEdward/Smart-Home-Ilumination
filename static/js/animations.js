function mainServer(evt, category) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(category).style.display = "block";
    evt.currentTarget.className += " active";
  }


  
var timer;

function openPopup1(id){
    var popup=document.getElementById("popuphouse");
    popup.style.display="block";
    window.onclick=function(event){
      if(event.target == popup){
        popup.style.display="none";
      }
    }
  }

function openPopup2(id){
  unsignedBulbs();
  roomtypes();
  var popup=document.getElementById("popuproom");
  popup.style.display="block";
  window.onclick=function(event){
    if(event.target == popup){
      popup.style.display="none";
    }
  }
}

function openPopup3(id){
  var popup=document.getElementById("popupbulb");
  popup.style.display="block";
  window.onclick=function(event){
    if(event.target == popup){
      popup.style.display="none";
    }
  }
}

function openPopup4(id){
  roomTypes();
  var popup=document.getElementById("popupsens");
  popup.style.display="block";
  window.onclick=function(event){
    if(event.target == popup){
      popup.style.display="none";
    }
  }
}

function openPopup5(id){
  var popup=document.getElementById("popupuser");
  popup.style.display="block";
  window.onclick=function(event){
    if(event.target == popup){
      popup.style.display="none";
    }
  }
}

function openPopup6(id){
  sensorids();
  var popup=document.getElementById("popupdeletesens");
  popup.style.display="block";
  window.onclick=function(event){
    if(event.target == popup){
      popup.style.display="none";
    }
  }
}

function openPopup7(id){
lightbulbids();
var popup=document.getElementById("popupdeletelight");
popup.style.display="block";
window.onclick=function(event){
  if(event.target == popup){
    popup.style.display="none";
  }
}
}

function openPopup8(id){
dbusernames();
var popup=document.getElementById("popupdeleteuser");
popup.style.display="block";
window.onclick=function(event){
  if(event.target == popup){
    popup.style.display="none";
  }
}
}

function openPopup9(id){
allroomtypes();
var popup=document.getElementById("popupdeletehouseroom");
popup.style.display="block";
window.onclick=function(event){
  if(event.target == popup){
    popup.style.display="none";
  }
}
}

function openPopup10(id){
allroomtypesbulbs();
timer = setInterval(function(){getbulbsoftype();},1000);
var popup=document.getElementById("popupdeleteroomlight");
popup.style.display="block";
window.onclick=function(event){
  if(event.target == popup){
    popup.style.display="none";
  }
}
}

function openPopup11(id){
  var popup=document.getElementById("popupmodifypreferences");
  popup.style.display="block";
  window.onclick=function(event){
    if(event.target == popup){
      popup.style.display="none";
    }
  }
  }

function close1(){
  var popup=document.getElementById("popuphouse");
  popup.style.display="none";
}

function close2(){
  var popup=document.getElementById("popuproom");
  popup.style.display="none";
}

function close3(){
  var popup=document.getElementById("popupbulb");
  popup.style.display="none";
}

function close4(){
  var popup=document.getElementById("popupsens");
  popup.style.display="none";
}

function close5(){
  var popup=document.getElementById("popupuser");
  popup.style.display="none";
}

function close6(){
  var popup=document.getElementById("popupdeletesens");
  popup.style.display="none";
}

function close7(){
  var popup=document.getElementById("popupdeletelight");
  popup.style.display="none";
}

function close8(){
  var popup=document.getElementById("popupdeleteuser");
  popup.style.display="none";
}

function close9(){
  var popup=document.getElementById("popupdeletehouseroom");
  popup.style.display="none";
}

function close10(){
  clearInterval(timer);
  var popup=document.getElementById("popupdeleteroomlight");
  popup.style.display="none";
  
}

function close11(){
  var popup=document.getElementById("popupmodifypreferences");
  popup.style.display="none";
  
}

function getvalue(){
  var opt = document.getElementById("house_room_types").options[document.getElementById("house_room_types").selectedIndex].text;
  return opt;
}




function switchCheck(room,id){
  var checkbox = document.getElementById(id);
  if(checkbox.checked == true)
  {
    checkBulbs(room,1)
    updateroomswitch(room,1)
    updateroombulbsswitch(room,0)
  }
  else
  {
    checkBulbs(room,0)
    updateroomswitch(room,0)
    updateroombulbsswitch(room,0)
  }
}

function switchCheckLight(bulb,id){
  var checkbox = document.getElementById(id);
  if(checkbox.checked == true)
  {
    updateroombulbswitch(bulb,1)
  }
  else
  {
    updateroombulbswitch(bulb,0)
  }
}


function createButton(id,text){
  let btn = document.createElement('button');
  btn.setAttribute("class","btn-format")
  btn.setAttribute("id",text+"btn");
  btn.setAttribute("value","hidden");
  btn.setAttribute("onclick","expandList(this.id,this.value)");
  btn.innerText = text;
  if(document.getElementById(text+"btn") == null)
  {
    document.getElementById(id).appendChild(btn);
  }
}

function expandList(id,value)
{
  var btn = document.getElementById(id);
  if(value=="hidden")
  {
    document.getElementById("colorpicker"+btn.innerText).setAttribute("class", "reveal")
    document.getElementById(btn.innerText).setAttribute("class","reveal");
    document.getElementById(id).value="revealed";
  }
  else
  {
    document.getElementById("colorpicker"+btn.innerText).setAttribute("class", "hide")
    document.getElementById(btn.innerText).setAttribute("class","hide")
    document.getElementById(id).value="hidden";
  }
}

function createList(btn,id,val1,val2,color){
  items=[]
  items.push(val1);
  items.push(val2);
  container = document.createElement('div')
  container.setAttribute("id","divroom"+String(id))
  container.setAttribute("class","lst-format")
  if(document.getElementById("divroom"+String(id)) == null)
  {
    document.getElementById("room"+id).appendChild(container);
    let form = document.createElement('form');
    form.setAttribute("id","colorpicker"+id);
    form.setAttribute("class","hide");
    document.getElementById("divroom"+String(id)).appendChild(form);
    let lbl = document.createElement('label')
    lbl.setAttribute("for", "pickerselect"+id);
    lbl.innerHTML = "Color &emsp; &emsp; &emsp; &emsp;";
    document.getElementById("colorpicker"+id).appendChild(lbl);
    let inp = document.createElement('input');
    inp.setAttribute("type","color");
    inp.setAttribute("id","pickerselect"+id);
    inp.setAttribute("value",color);
    inp.setAttribute("class","colorpick");
    document.getElementById("colorpicker"+id).appendChild(inp);
    updatelightbulbcolor("pickerselect"+id,id)
    let lst =  document.createElement('table');
    lst.setAttribute("class","hide");
    lst.setAttribute("id",btn);
    document.getElementById("divroom"+String(id)).appendChild(lst);
    for (i =0; i< items.length; i++)
    {
      if(i==0)
      {
        let tr = document.createElement('tr');
        lst.appendChild(tr);
        let td1 = document.createElement('td');
        tr.appendChild(td1);
        td1.innerHTML += "Status &emsp;"
        let td2 = document.createElement('td');
        tr.appendChild(td2);
        if(items[0] == "0")
        {
          let lb = document.createElement('label');
          lb.setAttribute("class","switch");
          let inp = document.createElement('input');
          inp.setAttribute("type","checkbox");
          inp.setAttribute("id","switchroom"+id);
          inp.setAttribute("onclick","switchCheck('"+id+"',this.id)");
          let spn = document.createElement('span');
          spn.setAttribute("class","slider round");
          lb.appendChild(inp);
          lb.appendChild(spn);
          td2.appendChild(lb);
        }
        else
        {
          let lb = document.createElement('label');
          lb.setAttribute("class","switch");
          let inp = document.createElement('input');
          inp.setAttribute("type","checkbox");
          inp.setAttribute("id","switchroom"+id);
          inp.setAttribute("onclick","switchCheck('"+id+"',this.id)");
          inp.checked = true;
          let spn = document.createElement('span');
          spn.setAttribute("class","slider round");
          lb.appendChild(inp);
          lb.appendChild(spn);
          td2.appendChild(lb);
        }
        
      }
      else if(i==1)
      {
        let tr = document.createElement('tr');
        lst.appendChild(tr);
        let td3 = document.createElement('td');
        tr.appendChild(td3);
        td3.innerHTML += "Consumption &emsp;"
        let td4 = document.createElement('td');
        tr.appendChild(td4);
        td4.innerHTML += items[i];
      }
    }
  }
  
}


async function houseRooms(){
  await fetch('http://localhost:5000/getrooms')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      for(var i =0; i < data.length;i++)
      {
        container = document.createElement('div')
        container.setAttribute("id","room"+data[i][0])
        container.setAttribute("class","btn-column")
        if(document.getElementById("room"+data[i][0]) == null)
        {
        document.getElementById("house").appendChild(container);
        container = document.createElement('div')
        container.setAttribute("id","div"+data[i][0])
        document.getElementById("room"+data[i][0]).appendChild(container);
        createButton("div"+data[i][0],data[i][0]);
        createList(data[i][0],data[i][0],data[i][1],data[i][2],data[i][3])
        }
      }
    })
}

async function unsignedBulbs(){
  await fetch('http://localhost:5000/getunsignedbulbs')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("selectbulbs").options.length>0)
        {
          for (var j = document.getElementById("selectbulbs").options.length; j >= 0; j--) {
            document.getElementById("selectbulbs").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("selectbulbs").appendChild(option);
      }
    })
}
async function roomtypes(){
  await fetch('http://localhost:5000/getroomtypes')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("room_type").options.length>0)
        {
          for (var j = document.getElementById("room_type").options.length; j >= 0; j--) {
            document.getElementById("room_type").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("room_type").appendChild(option);
        
      }
    })
}
async function roomTypes(){
  await fetch('http://localhost:5000/getroomtypes')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("room_types").options.length>0)
        {
          for (var j = document.getElementById("room_types").options.length; j >= 0; j--) {
            document.getElementById("room_types").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("room_types").appendChild(option);
        
      }
    })
}
async function bulbsids(){
  await fetch('http://localhost:5000/getroomtypes')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("bulb_id").options.length>0)
        {
          for (var j = document.getElementById("bulb_id").options.length; j >= 0; j--) {
            document.getElementById("bulb_id").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("bulb_id").appendChild(option);
        
      }
    })
}
async function sensorids(){
  await fetch('http://localhost:5000/getsensorids')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("sens_id").options.length>0)
        {
          for (var j = document.getElementById("sens_id").options.length; j >= 0; j--) {
            document.getElementById("sens_id").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("sens_id").appendChild(option);
        
      }
    })
}
async function lightbulbids(){
  await fetch('http://localhost:5000/getlightbulbids')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("lightbulb_id").options.length>0)
        {
          for (var j = document.getElementById("lightbulb_id").options.length; j >= 0; j--) {
            document.getElementById("lightbulb_id").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("lightbulb_id").appendChild(option);
        
      }
    })
}
async function dbusernames(){
  await fetch('http://localhost:5000/getusernames')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("user_name").options.length>0)
        {
          for (var j = document.getElementById("user_name").options.length; j >= 0; j--) {
            document.getElementById("user_name").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("user_name").appendChild(option);
        
      }
    })
}
async function allroomtypes(){
  await fetch('http://localhost:5000/getrooms')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("house_room_type").options.length>0)
        {
          for (var j = document.getElementById("house_room_type").options.length; j >= 0; j--) {
            document.getElementById("house_room_type").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i][0];
        option.setAttribute("value",data[i][0])
        document.getElementById("house_room_type").appendChild(option);
        
      }
    })
}
async function allroomtypesbulbs(){
  await fetch('http://localhost:5000/gethouserooms')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("house_room_types").options.length>0)
        {
          for (var j = document.getElementById("house_room_types").options.length; j >= 0; j--) {
            document.getElementById("house_room_types").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        option = document.createElement('option')
        option.innerText = data[i];
        option.setAttribute("value",data[i])
        document.getElementById("house_room_types").appendChild(option);
        
      }
    })
}
async function getbulbsoftype(){
  await fetch('http://localhost:5000/getbulbsid')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      if(document.getElementById("bulb_id").options.length>0)
        {
          for (var j = document.getElementById("bulb_id").options.length; j >= 0; j--) {
            document.getElementById("bulb_id").remove(j);
          }
        }
      for(var i =0; i < data.length;i++)
      {
        if(data[i][0] == getvalue())
        {
          option = document.createElement('option')
          option.innerText = data[i][1];
          option.setAttribute("value",data[i][1])
          document.getElementById("bulb_id").appendChild(option);
        }       
      }
    })
}

async function getroomasignedbulbs(){
  await fetch('http://localhost:5000/getroomasignedbulbs')
    .then(fetchedData => fetchedData.json())
    .then(data =>{
      
      for(var i =0; i < data.length;i++)
      {
        const bulblist =  document.createElement('table');
        bulblist.setAttribute("id","bulbs"+data[i][0]);
        document.getElementById(data[i][0]).appendChild(bulblist);
        let tr = document.createElement('tr');
        bulblist.appendChild(tr);
        let td1 = document.createElement('td');
        tr.appendChild(td1);
        td1.innerHTML += "Lightbulb "+data[i][1] +"&emsp;"
        let td2 = document.createElement('td');
        tr.appendChild(td2);
        if(data[i][2] == "0")
        {
          let lb = document.createElement('label');
          lb.setAttribute("class","switch");
          let inp = document.createElement('input');
          inp.setAttribute("type","checkbox");
          inp.setAttribute("id","switchbulb"+data[i][1]);
          inp.setAttribute("onclick","switchCheckLight('"+data[i][1]+"',this.id)");
          let spn = document.createElement('span');
          spn.setAttribute("class","slider round");
          lb.appendChild(inp);
          lb.appendChild(spn);
          td2.appendChild(lb);
        }
        else
        {
          let lb = document.createElement('label');
          lb.setAttribute("class","switch");
          let inp = document.createElement('input');
          inp.setAttribute("type","checkbox");
          inp.setAttribute("id","switchbulb"+data[i][1]);
          inp.setAttribute("onclick","switchCheckLight('"+data[i][1]+"',this.id)");
          inp.checked = true;
          let spn = document.createElement('span');
          spn.setAttribute("class","slider round");
          lb.appendChild(inp);
          lb.appendChild(spn);
          td2.appendChild(lb);
        }
              
      }
    })
}

async function checkBulbs(room,value){
  await fetch('http://localhost:5000/getroomasignedbulbs')
  .then(fetchedData => fetchedData.json())
  .then(data =>{
    for(var i =0; i < data.length;i++)
    {
      if(data[i][0] == room)
      {
        if(value ==1){
          document.getElementById("switchbulb"+data[i][1]).checked = true;
        }
        else{
          document.getElementById("switchbulb"+data[i][1]).checked = false;
        }
      }    
    }
  })
}

async function updateroomswitch(room,status){
  fetch('/updateroomstatus',{
    headers: {'Content-Type': 'application/json'},
    method: 'POST',
    body: JSON.stringify([room,status])
}).then(function(response){return response.text();})
  .then(function(text){console.log('POST response:');console.log(text);})
}

async function updateroombulbswitch(bulb,status){
  fetch('/updateroombulbstatus',{
    headers: {'Content-Type': 'application/json'},
    method: 'POST',
    body: JSON.stringify([bulb,status])
}).then(function(response){return response.text();})
  .then(function(text){console.log('POST response:');console.log(text);})
}

async function updatelightbulbcolor(id,room){
  colorPicker = document.getElementById(id);
  colorPicker.addEventListener('change', function() {
      fetch('/updatelightbulbcolor',{
        headers: {'Content-Type': 'application/json'},
        method: 'POST',
        body: JSON.stringify([room,this.value])
    }).then(function(response){return response.text();})
      .then(function(text){console.log('POST response:');console.log(text);})
 });
}

function autorun(time){
  setInterval(function(){
    houseRooms();
  },time);
}

houseRooms();
getroomasignedbulbs();
autorun(5000);



var x = document.getElementById("startpage").click();
