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
        var msg = JSON.parse(event.data)
        if (msg.type == 0) {
            addMsg("Message received: " + msg['data']);
            log("Info: Message received from server: " + msg['data']);
        } else if (msg.type == 3) {
            if (msg.data > 1){
                document.getElementById("alert").classList.remove("d-none")
            }
        }
        

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


/**
 * Send a new message and encoding to json
 * 
 * @param {*} data data to send
 * @param {int} type 0: server message, 1: client message, 2: simpi config queue, 3: Multi-client management
 */

function sendMsg(data, type = 1){
    try {
        msg = {data: data, type: type}
        ws.send(JSON.stringify(msg));
        addMsg("<br/>Message sent: " + data);
        log("Message send to server: " + data);
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


var simpiQueue = []

function updateQueueDisplay(){
    const queue = document.getElementById("queue");
    var text = ""
    simpiQueue.forEach((option) => {
        text += option.options[0] + "<br/>"
    })
    queue.innerHTML = text;
}


function addToSimpiQueue(){
    switch(this.parentNode.getAttribute('simpiType')){
        case "1":
            simpiQueue.push({
                type: 1,
                options: ["Click to start"]
            })
            break;
        case "2":
            simpiQueue.push({
                type: 2,
                options: ["Suspend"]
            })
            break;
        case "3":
            simpiQueue.push({
                type: 3,
                options: ["Click to resume"]
            })
            break;
        case "4":
            simpiQueue.push({
                type: 4,
                options: ["Resume"]
            })
            break;
        case "5":
            const inputs = this.parentNode.getElementsByTagName("input");
            simpiQueue.push({
                type: 5,
                options: ["Wait " + inputs[0].value + " minutes", inputs[0].value]
            })
            break;
        default:
            console.log(this.parentNode.getAttribute('simpiType'))
            break;
    }
    console.log(simpiQueue)
    updateQueueDisplay();
}


const simpiOptions = document.getElementsByClassName("btn-option")
for (let i = 0; i < simpiOptions.length; i++) {
    simpiOptions[i].addEventListener("click", addToSimpiQueue)
}

