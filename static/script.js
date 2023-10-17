const chat = document.querySelector(".chats");
const message = document.querySelector('#userQuery').value;
function formSubmit() {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.innerText = message;
    chat.appendChild(messageDiv)
}