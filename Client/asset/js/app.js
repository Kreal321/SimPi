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
            addMsg(msg['data']);
            log("Info: Message received from server: " + msg['data']);
        } else if (msg.type == 3) {
            if (msg.data > 1){
                document.getElementById("alert").classList.remove("d-none")
            }
        } else if (msg.type == 4) {
            log("Info: Message received from server: " + msg['data']);
        } else if (msg.type == 5) {
            simpiStatus = msg['data'];
        }
        

    })
}

var ip = "";
var ws = null;
document.getElementById("connectBtn").addEventListener("click", autoConnect)

var simpiStatus = 0;

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
        sendMsg(btn.innerText)
        check();
    })
});


// SimPi Queue
var simpiQueue = []
document.getElementById("sendSimpiQ").addEventListener("click", () => {
    sendMsg(simpiQueue, 2)
})

function optionToString(option){
    const optionList = {
        "10": "Start",
        "11": '<button class="btn btn-outline-success" onclick="signalBtn()">Click to start</button>',
        "20": "Suspend",
        "21": "Click to spspend",
        "30": "Resume",
        "31": "Click to resume",
        "40": "Stop",
        "41": '<button class="btn btn-outline-success">Click to stop</button>',
        "51": "Wait until Sensor input high",
        "52": "Wait until Source 2 is On",
        "53": 'Wait until <button class="btn btn-outline-success" onclick="signalBtn()">Click</button>',
        "61": "On Port ",
        "62": "Off Port ",
        "71": "Play Audio ",
        "72": "Pause Audio ",
        "73": "Resume Audio ",
        "74": "Stop Audio ",
    }
    if(option.type == "50"){
        return "Wait " + option.data[0] + " seconds";
    }else{
        return optionList[option.type] + option.data[0];
    }
}

function updateQueueDisplay(){
    const queue = document.getElementById("queue");

    var text = ""
    simpiQueue.forEach((option, idx) => {
        text += (idx + 1) + ": " + optionToString(option) + "<br/>"
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

function check() {
    var intervalID = setInterval(() => {
        sendMsg("now");
        if(simpiQueue.length == simpiStatus) {
            clearInterval(intervalID)
        }
    }, 500);
}