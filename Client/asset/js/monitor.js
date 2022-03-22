ws = new WebSocket("ws://" + ip + ":80/");
postMessage(1);
setTimeout("timedCount()",500);
postMessage(2);