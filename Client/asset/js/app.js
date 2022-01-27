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
var ip = "";
var ws = null;
document.getElementById("ipBtn").addEventListener("click", ()=>{
    ip = document.getElementById("ip").value;
    ws = new WebSocket("ws://" + ip + ":80/");
    // Receive a new message
    ws.addEventListener('message', (event)=>{
        addMsg("Message received: " + event.data);
        log("Message received from server: " + event.data);

    })
})



const inputbox = document.getElementById("text");
const checkbox = document.getElementById("check");
const msgbox = document.getElementById("msg");


// update message
function addMsg(str) {
    var msg = msgbox.innerHTML;
    msgbox.innerHTML = msg + str + "<br />";
    msgbox.scrollTop = msgbox.scrollHeight;
}


// Send a new message
function sendMsg(str){
    try {
        ws.send(str);
        addMsg("<br/>Message sent: " + str);
        log("Message send to server: " + str);
    } catch (error) {
        document.getElementById("h").innerHTML= stuff;
        log(error, true);
    }
}

function send(){
    sendMsg(inputbox.value);

}

const controllerBtns = document.getElementById("controller-btns").childNodes

controllerBtns.forEach( (btn) => {
    btn.addEventListener('click', (e) => {
        sendMsg(btn.innerText)
    })
});






// message will be json in the future