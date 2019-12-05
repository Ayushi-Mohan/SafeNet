var i;
function reload(url) {
    for (i=0; i<11; i++){
        if(url[i]=='TRUE'){
            if(i==0){
                document.getElementById("customCheck1").checked = true;
            }
            if(i==1){
                document.getElementById("customCheck2").checked = true;
            }
            if(i==2){
                document.getElementById("customCheck3").checked = true;
            }
            if(i==3){
                document.getElementById("customCheck4").checked = true;
            }
            if(i==4){
                document.getElementById("customCheck5").checked = true;
            }
            if(i==5){
                document.getElementById("customCheck6").checked = true;
            }
            if(i==6){
                document.getElementById("customCheck7").checked = true;
            }
            if(i==7){
                document.getElementById("customCheck8").checked = true;
            }
            if(i==8 || i==9 || i==10){
                continue;
            }
        }
        else if(url[i]=='NULL'){
            continue;
        }
        else{
            if(i==0){
                document.getElementById("customCheck1").checked = true;
                document.getElementById("customSwitch1").checked = true;
                document.getElementById("URL1").value = url[i];
            }
            if(i==1){
                document.getElementById("customCheck2").checked = true;
                document.getElementById("customSwitch2").checked = true;
                document.getElementById("URL2").value = url[i];
            }
            if(i==2){
                document.getElementById("customCheck3").checked = true;
                document.getElementById("customSwitch3").checked = true;
                document.getElementById("URL3").value = url[i];
            }
            if(i==3){
                document.getElementById("customCheck4").checked = true;
                document.getElementById("customSwitch4").checked = true;
                document.getElementById("URL4").value = url[i];
            }
            if(i==4){
                document.getElementById("customCheck5").checked = true;
                document.getElementById("customSwitch5").checked = true;
                document.getElementById("URL5").value = url[i];
            }
            if(i==5){
                document.getElementById("customCheck6").checked = true;
                document.getElementById("customSwitch6").checked = true;
                document.getElementById("URL6").value = url[i];
            }
            if(i==6){
                document.getElementById("customCheck7").checked = true;
                document.getElementById("customSwitch7").checked = true;
                document.getElementById("URL7").value = url[i];
            }
            if(i==7){
                document.getElementById("customCheck8").checked = true;
                document.getElementById("customSwitch8").checked = true;
                document.getElementById("URL8").value = url[i];
            }
            if(i==8){
                document.getElementById("customSwitchCust1").checked = true;
                document.getElementById("CustURLRed1").value = url[i];
            }
            if(i==9){
                document.getElementById("customSwitchCust2").checked = true;
                document.getElementById("CustURLRed2").value = url[i];
            }
            if(i==10){
                document.getElementById("customSwitchCust3").checked = true;
                document.getElementById("CustURLRed3").value = url[i];
            }
        }
    }
}