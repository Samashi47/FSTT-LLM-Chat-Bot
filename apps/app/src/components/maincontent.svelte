<script lang="ts">
    import Card from './Card.svelte';

    export let isSidebarVisible: boolean;

    let userText = '';
    let messages = [];

    // Handle sending a message
    const sendMessage = () => {
        if (userText.trim() !== '') {
            messages = [...messages, { text: userText, type: 'user' }];
            userText = '';
            messages = [...messages, { text: 'typing...', type: 'bot', loading: true }];
            scrollToBottom();
            setTimeout(() => {
                messages.pop(); // Remove the typing indicator
                messages = [...messages, { text: 'ser lheh a jomi', type: 'bot' }];
                scrollToBottom();
            }, 2000);

            // Update styles when sending a message
            updateStyles();
        }
    };

    // Handle keydown event to send a message when Enter is pressed
    const handleKeydown = (event: KeyboardEvent) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    };

    // Scroll to bottom of the chat container
    const scrollToBottom = () => {
        const chatContainer = document.querySelector('.chat-container');
        chatContainer.scrollTo({
            top: chatContainer.scrollHeight,
            behavior: 'smooth'
        });
    };

    // Copy bot response text to clipboard
    const copyBotResponse = (text: string) => {
        navigator.clipboard.writeText(text);
    };

    // Update styles when sending a message
    const updateStyles = () => {
        const intro = document.querySelector('.intro');
        const chatContainer = document.querySelector('.chat-container');
        
        if (intro && chatContainer) {
            intro.style.opacity = '0';
            intro.style.pointerEvents = 'none';
            chatContainer.style.marginTop = '-300px';
        }
    };
</script>



<div class="main-content" style="--main-content-margin: {isSidebarVisible ? '300px' : '0'};">
    <div class="intro">
        <h1 class="heading-animation">FSTT CHATBOT</h1>
        <div class="image-container">
            <img src="/home.png" alt="Home Image" />
        </div>
    

    <div class="card-container">
        <Card image="/t1.png" text="Courses in MST AISD examination" />
        <Card image="/t2.png" text="The details of the Mevlana program" />
        <Card image="/l4.png" text="The link to access my scholarly paper." />
        <Card image="/q4.png" text="Who is the coordinator of LSI CI?" />
    </div>
</div>

<div class="chat-container">
    {#each messages as message}
        <div class="message {message.type}">
            {#if message.type === 'user'}
                <div class="circle">U</div>
            {:else}
                <div class="circle">C</div>
            {/if}
            <div class="message-content">
                {#if message.type === 'bot'}
                    <div class="bot-response">
                        {#if message.loading}
                            <div class="typing-indicator">
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>
                        {:else}
                            <img src="/home.png" alt="Bot Logo" class="bot-logo" />
                            <div>{message.text}</div>
                        {/if}
                        <!-- Add small picture button outside the response -->
                        {#if !message.loading}
                            <img src="/c1.png" alt="Copy" class="copy-button" on:click={() => copyBotResponse(message.text)} />
                        {/if}
                    </div>
                {:else}
                    <div class="user-response">{message.text}</div>
                {/if}
            </div>
        </div>
    {/each}
</div>




    <div class="typing-container">
        <textarea bind:value={userText} on:keydown={handleKeydown} placeholder="Ask Chat for anything about fstt" style="font-family: Georgia, 'Times New Roman', Times, serif;"></textarea>
        <!-- Replace the button with an image -->
        <img src="/send.png" width="60px" height="50px" alt="Send" class="send-button" on:click={sendMessage} />
    </div>
	<div class="notes">
		<p>ChatBot can make mistakes. Check important info.</p>
	</div>
    
</div>

<style>

.notes{
	color: #cccccc;
	font-family: Georgia, 'Times New Roman', Times, serif;
	font-size: 10px;
}
    .message-content {
    display: flex;
    align-items: center;
}

.bot-response {
    display: flex;
    align-items: center;
}

.user-response {
    margin-left: 30px; /* Adjust as needed */
}

.bot-logo {
    width: 20px;
    height: 20px;
    margin-right: 10px; /* Adjust as needed */
}

.copy-button {
    width: 20px;
    height: 20px;
    cursor: pointer; margin-left: 10px;
}

.circle {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background-color: #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    margin-right: 10px; /* Adjust as needed */
}

	.main-content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 1em;
		transition: margin 0.5s ease;
		margin-left: var(--main-content-margin, 0);
		max-width: calc(100% - 400px);
		height: 100vh;
		text-align: center;
	}

	.image-container {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 20px;
	}

	img {
		max-width: 15%;
	}

	.card-container {
		display: flex;
		justify-content: center;
		gap: 20px;
		margin-top: 20px;
	}

	.heading-animation {
		font-family: Georgia, 'Times New Roman', Times, serif;
		font-size: 28px;
		transition: color 0.3s ease;
	}

	.heading-animation:hover {
		color: #3f2305;
	}

	.chat-container {
		margin-top: 100px;
		width: 1000px;
		height: 950px;
		border-radius: 8px;
		overflow-y: auto;
		padding: 10px;
		margin-bottom: 20px;
		display: flex;
		flex-direction: column;
		gap: 10px;
		animation: fadeIn 0.5s ease-in-out;
	}

	@keyframes fadeIn {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}

	.message {
		padding: 10px;
		border-radius: 8px;
		margin-bottom: 10px;
		max-width: 70%;
		word-wrap: break-word;
		display: flex;
		align-items: center;
		gap: 10px;
		animation: slideIn 0.5s ease-in-out;
	}

	@keyframes slideIn {
		0% {
			transform: translateX(-50px);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}

	.message.user {
		background-color: #eeeeee;
		align-self: flex-end;
	}

	.message.bot {
		background-color: #cccccc;
		align-self: flex-start;
	}

	.bot-logo {
		width: 20px;
		height: 20px;
	}

	.typing-indicator {
		display: flex;
		gap: 5px;
	}

	.typing-indicator span {
		width: 5px;
		height: 5px;
		background-color: #333;
		border-radius: 50%;
		display: inline-block;
		animation: blink 1.4s infinite both;
	}

	.typing-indicator span:nth-child(1) {
		animation-delay: 0.2s;
	}

	.typing-indicator span:nth-child(2) {
		animation-delay: 0.4s;
	}

	.typing-indicator span:nth-child(3) {
		animation-delay: 0.6s;
	}

	@keyframes blink {
		0%,
		80%,
		100% {
			opacity: 0;
		}
		40% {
			opacity: 1;
		}
	}

	.typing-container {
  
		display: flex;
		align-items: center;
		width: 100%;
		max-width: 800px;
	}

	.typing-container textarea {
		width: 100%;
		height: 40px;
		resize: none;
		padding: 10px;
		border-radius: 12px;
		border: 1px solid #ccc;
		background-color:#eeeeee;
	}

	.send-button {
		margin-left: 10px;
		padding: 10px 20px;
		background-color: #ffffff;
		color: white;
		border: none;
		border-radius: 8px;
		cursor: pointer;
	}
    .copy-button {
        width: 20px;
        height: 20px;
        cursor: pointer;
    }
    .intro{

    }
    .circle {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background-color: #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
}

</style>
