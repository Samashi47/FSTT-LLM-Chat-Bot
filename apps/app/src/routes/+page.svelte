<script>
    let isSidebarVisible = true;

    function toggleSidebar() {
        isSidebarVisible = !isSidebarVisible;
        const sidebar = document.querySelector('.sidebar');
        sidebar.classList.toggle('hidden', !isSidebarVisible);
        const mainContent = document.querySelector('.main-content');
        mainContent.style.marginLeft = isSidebarVisible ? '400px' : '0';
    }

    let chatRequests = [
        { text: "How does GPT-4 work?", time: new Date() },
        { text: "Can you help me with my homework?", time: new Date() },
        { text: "Tell me a joke.", time: new Date() - 86400000 }, // Subtract 1 day in milliseconds
        // Add more chat requests here
    ];

    // Generate additional chat requests to meet the minimum of 40 requests
    const additionalRequests = [
        "What is the capital of France?",
        "How do I cook spaghetti?",
        "What is the weather like today?",
        "What is machine learning?",
        "How to meditate?",
        "What is the best exercise?",
        "How to write a resume?",
        "What are the benefits of yoga?",
        "How to improve communication skills?",
        "What is the best way to learn a new language?",
        "How to get better sleep?",
        "What are the best books to read?",
        "How to boost your immune system?",
        "How to handle stress?",
        "What are some good hobbies?",
        "How to be more productive?",
        "What is climate change?",
        "How to be happier?",
        "Best practices for remote work.",
        "How to prepare for an interview?",
        "What is the future of technology?",
        "How to start a podcast?",
        "Tips for staying motivated.",
        // Add more requests to reach the minimum of 40
    ];

    // Add additional requests to the chatRequests array
    additionalRequests.forEach(request => {
        chatRequests.push({ text: request, time: new Date() });
    });

    function categorizeChatRequests() {
        const today = new Date().setHours(0, 0, 0, 0);
        const yesterday = new Date(today - 86400000).setHours(0, 0, 0, 0); // Subtract 1 day in milliseconds

        const categorizedRequests = {
            today: [],
            yesterday: [],
            last7Days: []
        };

        chatRequests.forEach(request => {
            const requestTime = new Date(request.time).setHours(0, 0, 0, 0);
            if (requestTime === today) {
                categorizedRequests.today.push(request);
            } else if (requestTime === yesterday) {
                categorizedRequests.yesterday.push(request);
            } else if (request.time > yesterday && request.time < today) {
                categorizedRequests.last7Days.push(request);
            }
        });

        return categorizedRequests;
    }

    let categorizedChatRequests = categorizeChatRequests();
</script>


<style>
    .container {
        display: flex;
        flex-direction: column; /* Change to column to align items vertically */
        align-items: center; /* Center items horizontally */
        height: 100vh; /* Full height to center vertically */
        justify-content: center; /* Center items vertically */
        position: relative;
    }

    .sidebar {
        width: 400px; /* Default width */
        background-color: #f9f9f9;
        padding: 1em;
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
        transition: transform 0.5s ease; /* Transition the transform property */
        z-index: 999; /* Ensure sidebar is above other content */
        
    }

    .sidebar.hidden {
        transform: translateX(-100%);
    }

    .main-content {
        flex-grow: 1;
        padding: 1em;
        transition: margin 0.5s ease; /* Transition the margin property */
        margin-left: 0;
        max-width: calc(100% - 400px); /* Maximum width based on sidebar width */
    }

    .button-bar {
        display: flex;
        gap: 1em;
    }

    button {
        display: flex;
        align-items: center;
        padding: 0.5em 1em; /* Adjusted padding for better appearance */
        border: 2px solid #526D82; /* Border color */
        background-color: #3F2305; /* Background color */
        color: white;
        cursor: pointer;
        border-radius: 50px; /* Fully rounded button */
        font-size: 1em;
        transition: transform 0.2s ease; /* Transition the transform property on hover */
    }

    button i {
        margin-right: 0.5em;
    }

    button:hover {
        transform: scale(1.1); /* Scale button on hover */
    }

    .toggle-button {
        position: fixed;
        top: 1em;
        left: 1em;
        z-index: 1000;
        background-color: #3F2305; /* Background color */
        color: white;
        border: 2px solid #526D82; /* Border color */
        border-radius: 50px; /* Fully rounded button */
        padding: 0.5em 1em; /* Adjusted padding for better appearance */
        cursor: pointer;
        font-size: 1em;
        transition: transform 0.2s ease; /* Transition the transform property on hover */
    }

    .toggle-button:hover {
        transform: scale(1.1); /* Scale button on hover */
    }
    .history {
    flex-grow: 1;
    overflow-y: auto; /* Add scrollbar when content exceeds viewport height */
    background-color: #f9f9f9; /* Light background color for history section */
    border-radius: 8px; /* Rounded corners for history section */
    padding: 1em;
}


    .history-item {
        margin-bottom: 0.5em; /* Space between history items */
        padding: 0.5em;
        background: #f9f9f9;
        border: 1px solid #f9f9f9;
        border-radius: 4px;
    }

</style>

<div class="container">
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="button-bar">
            <button on:click={toggleSidebar}>
                <i class="fas fa-bars"></i> Hide 
            </button>
            <button style="margin-left: 160px;">
                <i class="fas fa-pencil-alt"></i> New
            </button>
        </div>
        <div class="history">
            <!-- Today's chat requests -->
            <h2>Today</h2>
            {#each categorizedChatRequests.today as request}
                <div class="history-item">{request.text}</div>
            {/each}
        
            <!-- Yesterday's chat requests -->
            <h2>Yesterday</h2>
            {#each categorizedChatRequests.yesterday as request}
                <div class="history-item">{request.text}</div>
            {/each}
        
            <!-- Last 7 days chat requests -->
            <h2>Last 7 Days</h2>
            {#each categorizedChatRequests.last7Days as request}
                <div class="history-item">{request.text}</div>
            {/each}
        </div>
        
        
        
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <h1>Welcome to SvelteKit</h1>
        <p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
        <img src="/f1.png" alt="F1 Image">
    </div>
</div>

<!-- Toggle button for when the sidebar is hidden -->
{#if !isSidebarVisible}
    <button class="toggle-button" on:click={toggleSidebar}>
        <i class="fas fa-bars"></i> Show 
    </button>
{/if}
