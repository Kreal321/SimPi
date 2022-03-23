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
function autoConnect() {
    ip = document.getElementById("ip").value;
    connectStatus = document.getElementById("connectStatus");
   
    ws = new WebSocket("ws://" + ip + ":80/");
    connectStatus.innerText = "Connecting";
        
    ws.addEventListener('open', (event)=>{
        connectStatus.classList.remove("text-danger");
        connectStatus.classList.add("text-success");
        connectStatus.innerText = "Connected";
    });
    ws.addEventListener('error', (event)=>{
        connectStatus.classList.remove("text-success");
        connectStatus.classList.add("text-danger");
        connectStatus.innerText = "Failed to connect";
    })

    // Receive a new message
    ws.addEventListener('message', (event)=>{
        var msg = JSON.parse(event.data)
        if (msg.type == 0) {
            // addMsg(msg['data']);
            log("Info: Message received from server: " + msg['data']);
        } else if (msg.type == 3) {
            if (msg.data > 1){
                document.getElementById("alert").classList.remove("d-none")
            }
        } else if (msg.type == 4) {
            log("Info: Message received from server: " + msg['data']);
        } else if (msg.type == 5) {
            simpiStatus = parseInt(msg['data']);
        }
        

    })
}

var ip = "";
var ws = null;
document.getElementById("connectBtn").addEventListener("click", autoConnect)

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
        log("Message send to server: " + data);
    } catch (error) {
        document.getElementById("h").innerHTML= stuff;
        log(error, true);
    }
}

function send(){
    sendMsg(inputbox.value);
}

function signalBtn(){
    sendMsg("signal");
}

const controllerBtns = document.getElementById("controller-btns").childNodes

controllerBtns.forEach( (btn) => {
    btn.addEventListener('click', (e) => {
        sendMsg(btn.innerText);
        if (btn.innerText == "Start") {
            setTimeout(() => {  check(); }, 1000);
        }
        if (btn.innerText == "Stop") {
            clearInterval(intervalID);
            intervalID = null;
        }
    })
});


// SimPi Queue
var simpiQueue = []
document.getElementById("sendSimpiQ").addEventListener("click", () => {
    sendMsg(simpiQueue, 2)
    updateQueueDisplay()
})

function optionToString(option, id){
    const optionList = {
        "10": '<div class="text-outline-success blue" id="' + id + '">Start</div>',
        "11": '<button class="btn btn-outline-primary text-outline-success blue" onclick="signalBtn()" id="' + id + '">Click to start</button>',
        "40": '<div class="text-outline-success blue" id="' + id + '">Stop</div>',
        "50": '<div class="text-outline-success blue" id="' + id + '">Wait ' + option.data[0] + ' seconds</div>',
        "51": "Wait until Sensor input high",
        "52": "Wait until Source 2 is On",
        "53": '<button class="btn btn-outline-primary text-outline-success blue" onclick="signalBtn()" id="' + id + '">Click to resume</button>',
        "61": '<div class="text-outline-success blue" id="' + id + '">On Port ' + option.data[0] + '</div>',
        "62": '<div class="text-outline-success blue" id="' + id + '">Off Port ' + option.data[0] + '</div>',
        "71": "Play Audio ",
        "72": "Pause Audio ",
        "73": "Resume Audio ",
        "74": "Stop Audio ",
    }

    return optionList[option.type];
    
}

function updateQueueDisplay(){
    const queue = document.getElementById("queue");

    var text = ""
    simpiQueue.forEach((option, idx) => {
        text += optionToString(option, idx + 1)
        if(idx != simpiQueue.length - 1) {
            text += '<svg class="blue" id="' + (idx+1.5) + '" viewbox="0 0 10 100"><line x1="5" x2="5" y1="0" y2="100"/></svg>'
        }
    })
    queue.innerHTML = text;
}


function addToSimpiQueue(){
    const type = this.parentNode.getAttribute('simpiType');
    switch(type){
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
            var selects = this.parentNode.getElementsByTagName("select")
            simpiQueue.push({
                type: type + selects[0].value,
                data: [""]
            })
            break;
        case "50":
            var inputs = this.parentNode.getElementsByTagName("input");
            simpiQueue.push({
                type: "50",
                data: [inputs[0].value]
            })
            break;
        case "6":
            var selects = this.parentNode.getElementsByTagName("select")
            simpiQueue.push({
                type: type + selects[0].value,
                data: [selects[1].value]
            })
            break;
        case "7":
            var selects = this.parentNode.getElementsByTagName("select")
            var inputs = this.parentNode.getElementsByTagName("input");
            simpiQueue.push({
                type: type + selects[0].value,
                data: [inputs[0].value]
            })
            break;
        default:
            console.log(this.parentNode.getAttribute('simpiType'))
            break;
    }
    console.log("item: " + JSON.stringify(simpiQueue));
    updateQueueDisplay();
}


const simpiOptions = document.getElementsByClassName("btn-option")
for (let i = 0; i < simpiOptions.length; i++) {
    simpiOptions[i].addEventListener("click", addToSimpiQueue)
}


// Simpi Queue Status
var simpiStatus = 0;

function updateDisplayColor(id){
    try{
        document.getElementById(id.toString()).classList.remove("blue");
        document.getElementById((id-0.5).toString()).classList.remove("blue");
        document.getElementById((id-1).toString()).classList.add("grey");
        document.getElementById((id-0.5).toString()).classList.add("grey");
    } catch(e){
        console.log(e);
    }
    
}

var intervalID;

function check() {
    simpiStatus = 0;
    document.getElementById("1").classList.remove("blue");
    var current = simpiStatus;
    if (intervalID != null) {
        clearInterval(intervalID);
    }
    intervalID = setInterval(() => {
        sendMsg("status");
        console.log(current + "/" + simpiStatus);
        while(current < simpiStatus){
            current += 1;
            updateDisplayColor(current);
        }
        if (simpiQueue.length == simpiStatus) {
            clearInterval(intervalID);
            intervalID = null;
            
        }
    }, 500);
}

// Test

simpiQueue = [{"type":"10","data":[""]},{"type":"61","data":["5"]},{"type":"50","data":["1"]},{"type":"62","data":["5"]},{"type":"50","data":["1"]},{"type":"61","data":["5"]},{"type":"50","data":["1"]},{"type":"62","data":["5"]},{"type":"50","data":["1"]},{"type":"61","data":["5"]},{"type":"40","data":[""]}];
updateQueueDisplay();
autoConnect();
sendMsg(simpiQueue, 2);
sendMsg("Start");