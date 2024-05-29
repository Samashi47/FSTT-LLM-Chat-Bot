<script lang="ts">
    export let isSidebarVisible: boolean;
</script>

<style>
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 1em;
        transition: margin 0.5s ease; /* Transition the margin property */
        margin-left: var(--main-content-margin, 0);
        max-width: calc(100% - 400px); /* Maximum width based on sidebar width */
        height: 100vh; /* Full height */
        text-align: center; /* Center text */
    }

    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px; /* Add space between image and cards */
    }

    img {
        max-width: 15%; /* Adjust image width */
    }

    /* Style for the cards */
    .card-container {
        display: flex;
        justify-content: center;
        gap: 20px; /* Adjust gap between cards */
        margin-top: 20px; /* Adjust margin as needed */
    }

    .card {
        width: 170px; /* Adjust width as needed */
        height: 110px; /* Adjust height as needed */
        background-color: white;
        border: 2px solid #ddd; /* Lighter grey border */
        border-radius: 10px; /* Rounded corners */
        padding: 10px; /* Adjust padding as needed */
        transition: transform 0.3s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .card:hover {
        transform: translateY(-5px); /* Pop-up effect */
        /* Add any additional styles for hover effect */
    }

    /* Animation for the heading */
    .heading-animation {
        font-family: Georgia, 'Times New Roman', Times, serif; /* Change font */
        font-size: 28px; /* Adjust font size */
        transition: color 0.3s ease; /* Transition color on hover */
    }

    .heading-animation:hover {
        color: #3F2305; /* Change color on hover */
    }

    /* Style for the text inside cards */
    .card p {
        font-size: 14px; /* Adjust font size */
        text-align: center; /* Center text */
        margin: 0; /* Remove default margin */
        color: #c6bebe;
    }

/*style for the prompt a jemi */
.prompt-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    
    width: 1000px;/* Adjust margin as needed */
}

.prompt-input {
    width: 80%; /* Adjust width as needed */
    padding: 15px; /* Adjust padding as needed */
    border-radius: 30px; /* Rounded corners */
    border: 1px solid #ccc; /* Border color */
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

<div class="main-content" style="--main-content-margin: {isSidebarVisible ? '400px' : '0'};">
    <h1 class="heading-animation" style="margin-top: 200px;">FSTT CHATBOT</h1>
    <div class="image-container">
        <img src="/home.png" alt="Home Image">
        <!-- You can add any animation classes here if needed -->
    </div>
    
    <div class="card-container">
        <!-- Card 1 -->
        <div class="card">
            <img src="/t1.png" alt="Image 1">
            <p>Courses in MST AISD examination</p>
        </div>
    
        <!-- Card 2 -->
        <div class="card">
            <img src="/t2.png" alt="Image 2">
            <p>the details of the Mevlana program </p>
        </div>
    
        <!-- Card 3 -->
        <div class="card">
            <img src="/l4.png" alt="Image 3">
            <p>the link to access my scholarly paper.</p>
        </div>
    
        <!-- Card 4 -->
        <div class="card">
            <img src="/q4.png" alt="Image 4">
            <p>Who is the coordinator of LSI CI?</p>
        </div>
    </div>

    <!-- Add space below the cards without affecting their position -->
    <div style="height: 700px;"></div>

    <!-- Prompt -->
    <div class="prompt-container">
        <input type="text" placeholder="Ask something for FSTT CHATBOT" class="prompt-input">
        <button class="send-button">
            <i class="fas fa-arrow-up"></i>
        </button>
    </div>
</div>

    
    

