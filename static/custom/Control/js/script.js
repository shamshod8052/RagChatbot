document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const input = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    // Fetch all previous messages and display them
    function loadMessages() {
        fetch("/messages/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        })
        .then(res => res.json())
        .then(data => {
            // Iterate over all messages and display them
            data.messages.forEach(msg => {
                addMessage("Siz", msg.question, "right");
                addMessage("AI", msg.answer, "left");
            });
        })
        .catch(error => {
            console.error("Error loading messages:", error);
        });
    }

    // Load all messages when the page loads
    loadMessages();

    function addMessage(sender, text, side) {
        const msg = document.createElement("div");
        msg.className = `chat-message ${side}`;
        msg.textContent = text;
        chatBox.appendChild(msg);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function sendQuestion() {
        const question = input.value.trim();
        if (!question) return;

        addMessage("Siz", question, "right");
        input.value = "";

        fetch("/ask/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({ question: question }),
        })
        .then(res => res.json())
        .then(data => {
            if (data.answer) {
                addMessage("AI", data.answer, "left");
            } else {
                addMessage("AI", "Kechirasiz, javob topilmadi.", "left");
            }
        })
        .catch(error => {
            console.error("Xatolik:", error);
            addMessage("AI", "Server bilan bog‘lanishda xatolik yuz berdi.", "left");
        });
    }

    sendBtn.addEventListener("click", sendQuestion);
    input.addEventListener("keypress", function (e) {
        if (e.key === "Enter") sendQuestion();
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split("; ");
            for (let cookie of cookies) {
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.split("=")[1]);
                    break;
                }
            }
        }
        return cookieValue;
    }
});
