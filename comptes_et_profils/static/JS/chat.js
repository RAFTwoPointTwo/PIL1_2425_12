document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('chat-message-input');
    const messageSubmit = document.getElementById('chat-message-submit');
    const chatMessages = document.getElementById('chat-messages');

    // WebSocket - Pour le temps réel
    const wsScheme = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
    const wsPath = wsScheme + window.location.host + '/ws/chat/' + conversationId + '/';
    const chatSocket = new WebSocket(wsPath);

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const messageElement = document.createElement('div');
        messageElement.classList.add('mb-2');
        if (data.sender === currentUser) {
            messageElement.classList.add('text-end');
        }
        messageElement.innerHTML = '<strong>${data.sender}:</strong> ${data.message}';
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    messageSubmit.onclick = function() {
        const message = messageInput.value;
        chatSocket.send(JSON.stringify({
            'message': message,
            'sender': currentUser
        }));
        messageInput.value = '';
    };
});