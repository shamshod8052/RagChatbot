const chatBody = document.querySelector(".chat-body");
const messageInput = document.querySelector(".message-input");
const sendMessageButton = document.querySelector("#send-message");
const fileInput = document.querySelector("#file-input");
const chatbotToggler = document.querySelector("#chatbot-toggler");
const closeChatbot = document.querySelector("#close-chatbot");

const API_URL = "https://zal.yourproject.uz/api/message/"; // Sizning backend API

const initialInputHeight = messageInput.scrollHeight;

// Chatga xabar qo‘shish
const createMessageElement = (content, ...classes) => {
  const div = document.createElement("div");
  div.classList.add("message", ...classes);
  div.innerHTML = content;
  return div;
};

// Botdan javob olish
const generateBotResponse = async (incomingMessageDiv, userMessage) => {
  const messageElement = incomingMessageDiv.querySelector(".message-text");

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: userMessage }),
    });

    if (!response.ok) throw new Error("Server javob qaytarmadi!");

    const data = await response.json();
    messageElement.innerText = data.response || "Javob olinmadi"; // <-- server javobi
  } catch (error) {
    console.error("Fetch error:", error);
    messageElement.innerText = "Xatolik: " + error.message;
    messageElement.style.color = "red";
  } finally {
    incomingMessageDiv.classList.remove("thinking");
    chatBody.scrollTo({ top: chatBody.scrollHeight, behavior: "smooth" });
  }
};


// User xabar yuborishi
const handleOutgoingMessage = (e) => {
  e.preventDefault();
  const userMessage = messageInput.value.trim();
  if (!userMessage) return;

  messageInput.value = "";
  messageInput.dispatchEvent(new Event("input"));

  // Foydalanuvchi xabari
  const outgoingMessageDiv = createMessageElement(
    `<div class="message-text">${userMessage}</div>`,
    "user-message"
  );
  chatBody.appendChild(outgoingMessageDiv);
  chatBody.scrollTo({ top: chatBody.scrollHeight, behavior: "smooth" });

  // Bot "typing..." chiqishi
  const incomingMessageDiv = createMessageElement(
    `<svg class="bot-avatar" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 1024 1024">
       <path d="M738.3 287.6H285.7c-59 0-106.8 47.8-106.8 106.8v303.1c0 59 47.8 106.8 106.8 106.8h81.5v111.1c0 .7.8 1.1 1.4.7l166.9-110.6 41.8-.8h117.4l43.6-.4c59 0 106.8-47.8 106.8-106.8V394.5c0-59-47.8-106.9-106.8-106.9z"/>
     </svg>
     <div class="message-text">
       <div class="thinking-indicator">
         <div class="dot"></div><div class="dot"></div><div class="dot"></div>
       </div>
     </div>`,
    "bot-message",
    "thinking"
  );
  chatBody.appendChild(incomingMessageDiv);
  chatBody.scrollTo({ top: chatBody.scrollHeight, behavior: "smooth" });

  // API ga so‘rov yuborish
  generateBotResponse(incomingMessageDiv, userMessage);
};

// Enter bosilganda yuborish
messageInput.addEventListener("keydown", (e) => {
  const userMessage = e.target.value.trim();
  if (e.key === "Enter" && userMessage && !e.shiftKey && window.innerWidth > 768) {
    handleOutgoingMessage(e);
  }
});

// Input auto-resize
messageInput.addEventListener("input", () => {
  messageInput.style.height = `${initialInputHeight}px`;
  messageInput.style.height = `${messageInput.scrollHeight}px`;
});

// Yuborish tugmasi
sendMessageButton.addEventListener("click", (e) => handleOutgoingMessage(e));

// Chatbotni ochish-yopish
chatbotToggler.addEventListener("click", () => {
  document.body.classList.toggle("show-chatbot");
});

closeChatbot.addEventListener("click", () => {
  document.body.classList.remove("show-chatbot");
});
