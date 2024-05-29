<!-- Prompt.svelte -->
<style>
    .prompt-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    
    width: 1000px;/* Adjust margin as needed */
}

.prompt-input {
    width: 80%; /* Adjust width as needed */
    padding: 17px; /* Adjust padding as needed */
    border-radius: 30px; /* Rounded corners */

    background-color: #f4f4f4;
}

.send-button {
    background-color: #3F2305; /* Button background color */
    color: white; /* Button text color */
    border: none; /* Remove button border */
    border-radius: 50%; /* Rounded button */
    padding: 15px; /* Adjust padding as needed */
    cursor: pointer; /* Add cursor pointer */
    margin-left: 10px; /* Adjust margin as needed */
}

.send-button i {
    transform: rotate(-90deg); /* Rotate arrow icon */
}
</style>

<div class="prompt-container">
    <input type="text" placeholder="Ask something for FSTT CHATBOT" class="prompt-input">
    <button class="send-button">
        <i class="fas fa-arrow-up"></i>
    </button>
</div>
