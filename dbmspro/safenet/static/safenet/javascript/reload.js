var i;
var url;
function reload() {
	$.getJSON("../../static/safenet/javascript/urls.json", function(json) {
		url = json;
	    for (i=0; i<8; i++){
	        if(url[i]=='TRUE'){
	            if(i==0){
					document.getElementById("customCheck1").checked = true;
					myCheck1Function();
	            }
	            if(i==1){
					document.getElementById("customCheck2").checked = true;
					myCheck2Function();
	            }
	            if(i==2){
					document.getElementById("customCheck3").checked = true;
					myCheck3Function();
	            }
	            if(i==3){
					document.getElementById("customCheck4").checked = true;
					myCheck4Function();
	            }
	            if(i==4){
					document.getElementById("customCheck5").checked = true;
					myCheck5Function();
	            }
	            if(i==5){
					document.getElementById("customCheck6").checked = true;
					myCheck6Function();
	            }
	            if(i==6){
					document.getElementById("customCheck7").checked = true;
					myCheck7Function();
	            }
	            if(i==7){
					document.getElementById("customCheck8").checked = true;
					myCheck8Function();
	            }
	        }
	        else if(url[i]=='NULL'){
	            continue;
	        }
	        else{
	            if(i==0){
					document.getElementById("customCheck1").checked = true;
					myCheck1Function();
					document.getElementById("customSwitch1").checked = true;
					mySwitch1Function();
	                document.getElementById("URL1").value = url[i];
	            }
	            if(i==1){
					document.getElementById("customCheck2").checked = true;
					myCheck2Function();
					document.getElementById("customSwitch2").checked = true;
					mySwitch2Function();
	                document.getElementById("URL2").value = url[i];
	            }
	            if(i==2){
					document.getElementById("customCheck3").checked = true;
					myCheck3Function();
					document.getElementById("customSwitch3").checked = true;
					mySwitch3Function();
	                document.getElementById("URL3").value = url[i];
	            }
	            if(i==3){
					document.getElementById("customCheck4").checked = true;
					myCheck4Function();
					document.getElementById("customSwitch4").checked = true;
					mySwitch4Function();
	                document.getElementById("URL4").value = url[i];
	            }
	            if(i==4){
					document.getElementById("customCheck5").checked = true;
					myCheck5Function();
					document.getElementById("customSwitch5").checked = true;
					mySwitch5Function();
	                document.getElementById("URL5").value = url[i];
	            }
	            if(i==5){
					document.getElementById("customCheck6").checked = true;
					myCheck6Function();
					document.getElementById("customSwitch6").checked = true;
					mySwitch6Function();
	                document.getElementById("URL6").value = url[i];
	            }
	            if(i==6){
					document.getElementById("customCheck7").checked = true;
					myCheck7Function();
					document.getElementById("customSwitch7").checked = true;
					mySwitch7Function();
	                document.getElementById("URL7").value = url[i];
	            }
	            if(i==7){
					document.getElementById("customCheck8").checked = true;
					myCheck8Function();
					document.getElementById("customSwitch8").checked = true;
					mySwitch8Function();
	                document.getElementById("URL8").value = url[i];
	            }
	        }
	    }

	    if (url.length > 8) {

    	    var count = 0;
    	    if (url[8] != 'NULL' && count==0 ){
    	        count++;
    	        if (url[9] == 'NULL'){
    	            document.getElementById("URLcust1").defaultValue = url[8];
    	            document.getElementById("customSwitchCust1").checked = false;
    	        }
    	        else{
    	            document.getElementById("URLcust1").defaultValue = url[8];
					document.getElementById("customSwitchCust1").checked = true;
					mySwitchCust1Function();
    	            document.getElementById("CustURLRed1").value = url[9];
    	        }
    	    }

    	    if (url.length > 10)
    	    {
        	    if (url[10] != 'NULL' && count==1 ){
        	        count++;
        	        if (url[11] == 'NULL'){
        	            document.getElementById("URLcust2").defaultValue = url[10];
        	            document.getElementById("customSwitchCust2").checked = false;
        	        }
        	        else{
        	            document.getElementById("URLcust2").defaultValue = url[10];
						document.getElementById("customSwitchCust2").checked = true;
						mySwitchCust2Function();
        	            document.getElementById("CustURLRed2").value = url[11];
        	        }
        	    }

        	    if (url.length > 12) {
        	    	if (url[12] != 'NULL' && count==2 ){
            	        count++;
            	        if (url[13] == 'NULL'){
            	            document.getElementById("URLcust3").defaultValue = url[12];
            	            document.getElementById("customSwitchCust3").checked = false;
            	        }
            	        else{
            	            document.getElementById("URLcust3").defaultValue = url[12];
							document.getElementById("customSwitchCust3").checked = true;
							mySwitchCust3Function();
            	            document.getElementById("CustURLRed3").value = url[13];
            	        }
            	    }
            	}
        	}
    	}
	});
    
}

window.onload = reload();
