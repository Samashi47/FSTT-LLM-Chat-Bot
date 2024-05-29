<script>
    let isSidebarVisible = true;

    function toggleSidebar() {
        isSidebarVisible = !isSidebarVisible;
        document.querySelector('.sidebar').classList.toggle('hidden', !isSidebarVisible);
        document.querySelector('.main-content').style.marginLeft = isSidebarVisible ? '400px' : '0';
    }
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
        padding: 0.5em;
        border: none;
        background-color: #007BFF;
        color: white;
        cursor: pointer;
        border-radius: 4px;
        font-size: 1em;
    }

    button i {
        margin-right: 0.5em;
    }

    .toggle-button {
        position: fixed;
        top: 1em;
        left: 1em;
        z-index: 1000;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5em;
        cursor: pointer;
        font-size: 1em;
    }
</style>

<div class="container">
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="button-bar">
            <button on:click={toggleSidebar}>
                <i class="fas fa-bars"></i> Toggle
            </button>
            <button>
                <i class="fas fa-pencil-alt"></i> Edit
            </button>
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
        <i class="fas fa-bars"></i> Show Sidebar
    </button>
{/if}
