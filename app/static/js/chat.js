const chatContent = document.getElementById("chat_content");
const chatInput = document.getElementById("chat_input");
const sendBtn = document.getElementById("send_btn");

async function sendMessage() {
    const msg = chatInput.value.trim();
    if (msg === "") return;

    // Add user message
    const userMsg = document.createElement("div");
    userMsg.classList.add("message", "right");
    userMsg.textContent = msg;
    chatContent.appendChild(userMsg);

    chatInput.value = "";

    // Scroll to bottom
    chatContent.scrollTop = chatContent.scrollHeight;

    // Redirect to API
    const response = await fetch("/api/get_reply", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    });

    const data = await response.json();
    const botMsg = document.createElement("div");
    botMsg.classList.add("message", "left");
    botMsg.textContent = data.reply;
    chatContent.appendChild(botMsg);
    chatContent.scrollTop = chatContent.scrollHeight;
    
};

sendBtn.addEventListener("click", sendMessage);

chatInput.addEventListener("keydown", (e) => {
    if (e.key=="Enter") {
        e.preventDefault();
        sendMessage();
    }
});