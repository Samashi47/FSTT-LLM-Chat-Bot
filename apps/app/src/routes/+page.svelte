<script lang="ts">
    import Sidebar from '../components/Sidebar.svelte';
    import MainContent from '../components/MainContent.svelte';
    import { onMount } from 'svelte';

    let isSidebarVisible = true;
    let darkMode = false;
    let isBrowser = typeof window !== 'undefined';

    function timeoffDarkMode() {
    darkMode = !darkMode;
    if (darkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }

  if (isBrowser) {
    onMount(() => {
      if (darkMode) {
        document.body.classList.add('dark-mode');
      } else {
        document.body.classList.remove('dark-mode');
      }
    });

    $: {
      if (darkMode) {
        document.body.classList.add('dark-mode');
      } else {
        document.body.classList.remove('dark-mode');
      }
    }
  }



    function toggleSidebar() {
        isSidebarVisible = !isSidebarVisible;
    }

    let chatRequests = [
        { text: "How does GPT-4 work?", time: new Date() },
        { text: "Can you help me with my homework?", time: new Date() },
        { text: "Tell me a joke.", time: new Date(Date.now() - 86400000) }, // Subtract 1 day in milliseconds
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
</script>

<style>
    .container {
        display: flex;
        height: 100vh; /* Full height */
        position: relative;
    }
    .timeoff{
        position: fixed;
        top: 1em;
        margin-left: 80px;
        left: 1em;
        z-index: 1000;
        background-color: #f9f9f9; /* Background color */
        color: white;
         /* Border color */
        border-radius: 50px; /* Fully rounded button */
        padding: 0.5em 1em; /* Adjusted padding for better appearance */
        cursor: pointer;
        font-size: 1em;
        transition: transform 0.2s ease; 
        background-color: black;
    }
    .toggle-button {
        position: fixed;
        top: 1em;
        left: 1em;
        z-index: 1000;
        background-color: #f9f9f9; /* Background color */
        color: white;
         /* Border color */
        border-radius: 50px; /* Fully rounded button */
        padding: 0.5em 1em; /* Adjusted padding for better appearance */
        cursor: pointer;
        font-size: 1em;
        transition: transform 0.2s ease; /* Transition the transform property on hover */
    }
    .timeoff:hover{
        transform: scale(1.1);
    }
    .toggle-button:hover {
        transform: scale(1.1); /* Scale button on hover */
    }

    .main-content-container {
        flex-grow: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    :global(body) {
    --bg-color: white;
    --text-color: black;
    background-color: var(--bg-color);
    color: var(--text-color);
    transition: background-color 0.3s, color 0.3s;
  }
  :global(body.dark-mode) {
    --bg-color: #212121;
    --text-color: rgb(0, 0, 0);
  }
  :global(body.dark-mode) input {
    color: white; /* Font color for input in dark mode */
    background-color: #555; /* Optional: adjust the input background color for better contrast */
  }

</style>

<div class="container">
    <!-- Sidebar -->
    <Sidebar {chatRequests} {isSidebarVisible} />

    <!-- Main Content -->
    <div class="main-content-container">
        <MainContent {isSidebarVisible} />
    </div>

    <!-- Toggle button for when the sidebar is hidden -->
    <button class="toggle-button" on:click={toggleSidebar}>
        {#if isSidebarVisible}
            <img src="r1.png" alt="Hide Icon" width="30px">
        {:else}
            <img src="r2.png" alt="Show Icon" width="30px">
        {/if}
    </button>
    <button class="timeoff" on:click={timeoffDarkMode}> {darkMode ? 'Light Mode' : 'Dark Mode'}
    </button>

</div>