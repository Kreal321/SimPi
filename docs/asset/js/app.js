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

// Debug btn
function showDebug() {
    document.querySelectorAll(".hide").forEach((item) => {
        item.classList.remove("hide");
    })
}

document.getElementById("debug-btn").addEventListener("click", showDebug);

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
        } else if (msg.type == 6) {
            updateConfigList(msg.data);
        } else if (msg.type == 7) {
            simpiQueue = msg.data;
            updateQueueDisplay();
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
    console.log(this);
    this.classList.add("not-allowed");
}

const controllerBtns = document.getElementById("controller-btns").childNodes

controllerBtns.forEach( (btn) => {
    btn.addEventListener('click', (e) => {
        sendMsg(btn.innerText);

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
    updateQueueDisplay2()
    setTimeout(() => {  check(); }, 1000);
    
})

function optionToString(option){
    const optionList = {
        "10": 'Start',
        "11": 'Click to start',
        "40": 'Stop',
        "50": `Wait ${option.data[0]} seconds`,
        "51": "Wait until Sensor input high",
        "52": "Wait until Source 2 is On",
        "53": 'Click to resume',
        "61": `On ${option.data[1]} <br/> (GPIO ${option.data[0]})`,
        "62": `Off ${option.data[1]} <br/> (GPIO ${option.data[0]})`,
        "71": `Play Audio ${option.data[0]}.mp3`,
        "72": `Pause Audio ${option.data[0]}.mp3`,
        "73": `Resume Audio ${option.data[0]}.mp3`,
        "74": `Stop Audio ${option.data[0]}.mp3`,
        "80": `End If`,
        "81": `If True`,
        "82": `If False`,
    }
    return optionList[option.type];
}

function updateQueueDisplay() {
    const queue = document.getElementById("queue");
    var text = "";
    simpiQueue.forEach((option, idx) => {
        text += `
            <div class="draggable" draggable="true">
                <span class="text text-outline-success blue" id="${idx+1}">${optionToString(option)}</span>
                <span class="icon simpi-icon-menu"></span>
                <span class="icon simpi-icon-trash-2"></span>
            </div>
        `;

        if (idx != simpiQueue.length - 1) {
            text += `
                <svg class="blue" id="${(idx+1.5)}" viewbox="0 0 10 100">
                    <line x1="5" x2="5" y1="0" y2="100"/>
                </svg>
            `;
        };
    })

    queue.innerHTML = text;

    document.querySelectorAll('.draggable').forEach((item) => {
        item.addEventListener("dragstart", dragStart);
        item.addEventListener("dragenter", dragEnter);
        item.addEventListener("dragleave", dragLeave);
        item.addEventListener("dragover", dragOver);
        item.addEventListener("drop", dragDrop);
    })
    document.querySelectorAll('.draggable .simpi-icon-trash-2').forEach((item) => {
        item.addEventListener("click", removeItem);
    })
    
}

function updateQueueDisplay2() {
    const queue = document.getElementById("queue");
    var text = "";
    simpiQueue.forEach((option, idx) => {
        if(option.type == 11 || option.type == 53) {
            text += `<button class="text btn btn-outline-primary text-outline-success blue" id="${idx+1}">${optionToString(option)}</button>`;
        } else {
            text += `<span class="text text-outline-success blue" id="${idx+1}">${optionToString(option)}</span>`;
        }

        if (idx != simpiQueue.length - 1) {
            text += `
                <svg class="blue" id="${(idx+1.5)}" viewbox="0 0 10 100">
                    <line x1="5" x2="5" y1="0" y2="100"/>
                </svg>
            `;
        };
    })

    queue.innerHTML = text;

    document.querySelectorAll('button.text').forEach((item) => {
        item.addEventListener("click", signalBtn);
    })
}

function removeItem() {
    simpiQueue.splice(this.parentNode.children[0].id - 1, 1);
    updateQueueDisplay();
}

let dragIdx = -1;

function dragStart() {
    dragIdx = this.children[0].id - 1;
}
function dragEnter() {
    this.classList.add('over');
}
function dragLeave() {
    this.classList.remove('over');
}
function dragOver(e) {
    e.preventDefault();
}
function dragDrop() {
    this.classList.remove('over');
    simpiQueue.splice(this.children[0].id - 1, 0, simpiQueue.splice(dragIdx, 1)[0]);
    updateQueueDisplay();
}

function addToSimpiQueue(){
    const type = this.parentNode.getAttribute('simpiType');
    switch(type){
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "8":
            var selects = this.parentNode.getElementsByTagName("select");
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
            var selects = this.parentNode.getElementsByTagName("select");
            var inputs = this.parentNode.getElementsByTagName("input");
            simpiQueue.push({
                type: type + selects[0].value,
                data: [selects[1].value, inputs[0].value]
            })
            break;
        case "7":
            var selects = this.parentNode.getElementsByTagName("select");
            var inputs = this.parentNode.getElementsByTagName("input");
            simpiQueue.push({
                type: type + selects[0].value,
                data: [inputs[0].value]
            })
            break;
        case "80":
            simpiQueue.push({
                type: "80",
                data: [""]
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

// config file
function updateConfigList(data) {
    var list = document.getElementById("configList");
    var configList = "";
    data.forEach((file) => {
        configList += `<option value="${file}">${file}</option>`
    })
    list.innerHTML = configList;
}

function clearConfig() {
    simpiQueue = [];
    updateQueueDisplay();
    if (intervalID != null) {
        clearInterval(intervalID);
    }
    sendMsg("Stop");
}

function loadConfig() {
    var data = {};
    data.type = "load";
    data.file = document.getElementById("configList").value;
    sendMsg(data, 8);
}

function saveConfig() {
    var data = {};
    data.type = "save";
    data.file = document.getElementById("configName").value;
    data.data = simpiQueue;
    sendMsg(data, 8);
}

function deleteConfig() {
    var data = {};
    data.type = "delete";
    data.file = document.getElementById("configName").value;
    sendMsg(data, 8);
}


document.getElementById("clearConfig").addEventListener("click", clearConfig);
document.getElementById("loadConfig").addEventListener("click", loadConfig);
document.getElementById("saveConfig").addEventListener("click", saveConfig);
document.getElementById("deleteConfig").addEventListener("click", deleteConfig);