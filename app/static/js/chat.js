const chatContent = document.getElementById("chat_content");
const chatInput = document.getElementById("chat_input");
const sendBtn = document.getElementById("send_btn");

function createImageBook(imageUrls) {
    const book = document.createElement("div");
    book.classList.add("book");

    // Create elements
    const prevBtn = document.createElement("button");
    prevBtn.textContent = "⟨ Prev";

    const nextBtn = document.createElement("button");
    nextBtn.textContent = "Next ⟩";

    const img = document.createElement("img");
    img.alt = "Image book page";

    // Add to book
    book.appendChild(prevBtn);
    book.appendChild(img);
    book.appendChild(nextBtn);

    // Add book to chat
    chatContent.appendChild(book);

    let currentIndex = 0;
    img.src = imageUrls[currentIndex];

    // Button logic
    prevBtn.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
        img.src = imageUrls[currentIndex];
    });

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % imageUrls.length;
        img.src = imageUrls[currentIndex];
    });
}

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

    // Bot response-text
    const data = await response.json();
    const botMsg = document.createElement("div");
    botMsg.classList.add("message", "left");
    botMsg.textContent = data.reply;
    chatContent.appendChild(botMsg);

    // Bot response-list of images
    images = data.images_dict;
    topicsLen = Object.keys(images).length;
    if ( topicsLen > 0 ) {
        for (let topic in images) {
            console.log(`Creating image book for ${topic}`);
            createImageBook(images[topic]);
        }
    }
    
    chatContent.scrollTop = chatContent.scrollHeight;
    
};

sendBtn.addEventListener("click", sendMessage);

chatInput.addEventListener("keydown", (e) => {
    if (e.key=="Enter") {
        e.preventDefault();
        sendMessage();
    }
});