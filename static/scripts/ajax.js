document.getElementById("frmadd").addEventListener("submit", e=>{
    e.preventDefault();

    const xhttp = new XMLHttpRequest();

    let data = new FormData();
    data.append("reg", document.getElementById("txtreg").value);
    data.append("type", document.getElementById("cbxtype").value);

    xhttp.addEventListener("load", e => {
        if(e.target.status == 200){
            const json = JSON.parse(e.target.responseText);

            const li = document.createElement("li");
            li.innerHTML = json.reg
            document.getElementById("spaces").appendChild(li);
            document.getElementById("result").innerHTML = "Car added successfully";
            let spaces = document.getElementById("spacecount").textContent;
            document.getElementById("spacecount").innerHTML = spaces -= 1;
            document.querySelector("#carlist p").innerHTML = "Current vehicles in car park";
        }
        else{
            document.getElementById("result").innerHTML = "Sorry, the vehicle was not added";
        }
    });

    xhttp.open("POST", "/add", true);
    xhttp.send(data);

});


document.getElementById("frmremove").addEventListener("submit", e=>{
    e.preventDefault();

    const xhttp = new XMLHttpRequest();

    let data = new FormData();
    data.append("reg", document.getElementById("txtregrm").value);

    xhttp.addEventListener("load", e => {
        if(e.target.status == 200){
            const json = JSON.parse(e.target.responseText);

            const spaces = document.getElementById("spaces");
            spaces.innerHTML = "";
            json.forEach(car => {
                const li = document.createElement("li");
                li.innerHTML = car.reg
                spaces.appendChild(li);
            });

            document.getElementById("result").innerHTML = "Car removed successfully";
            let spacecount = Number(document.getElementById("spacecount").textContent);
            document.getElementById("spacecount").innerHTML = spacecount + 1

            const capacity = Number(document.getElementById("capacity").textContent)
            if(spacecount+1 == capacity){
                document.querySelector("#carlist p").innerHTML = "The carpark is empty";
            }
        }
        else{
            document.getElementById("result").innerHTML = "Sorry, that vehicle does not exist";
        }
    });

    xhttp.open("POST", "/remove", true);
    xhttp.send(data);

});