let ws = new WebSocket("ws://localhost:8765");

ws.onmessage = (event)=>{
  let d = JSON.parse(event.data);
  document.getElementById("data").innerText =
    JSON.stringify(d,null,2);
};