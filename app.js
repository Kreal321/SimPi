// Client Javascript
const debug = true;

// Log function
function log(str, error = false){
    if (error) {
        if (debug) console.log("Error: " + str);
    } else {
        if (debug) console.log(str);
    }
    
}


// create new websocket connection
const ws = new WebSocket("ws://127.0.0.1:5678/");


const inputbox = document.getElementById("text");
const checkbox = document.getElementById("check");
const msgbox = document.getElementById("msg");


// update message
function addMsg(str) {
    var msg = msgbox.innerHTML;
    msgbox.innerHTML = msg + str + "<br />";
}


// Send a new message
function sendMsg(str){
    try {
        ws.send(str);
        addMsg("Message sent: " + str);
        log("Message send to server: " + str);
    } catch (error) {
        document.getElementById("h").innerHTML= stuff;
        log(error, true);
    }
}

function send(){
    sendMsg(inputbox.value);

}


checkbox.addEventListener('change', (event) => {
    if (checkbox.checked == true){
        sendMsg("Power up GPIO 1");
    }else{
        sendMsg("Power off GPIO 1");
    }
    
})




// Receive a new message
ws.addEventListener('message', (event)=>{
    addMsg("Message received: " + event.data);
    log("Message received from server: " + event.data);

})


// message will be json in the future