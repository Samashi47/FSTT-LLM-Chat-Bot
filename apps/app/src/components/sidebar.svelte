<script>
    export let isSidebarVisible;
    export let toggleSidebar;
    export let darkMode = false;

    function reloadPage() {
        location.reload();
    }
</script>

<style>
    .hidden { display: none; }
    .sidebar {
        width: 300px;
        background-color: var(--bg-color);
        color: var(--text-color);       
        padding: 1em;
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
        transition: transform 0.5s ease;
        z-index: 999;
    }
    .sidebar.hidden {
        transform: translateX(-100%);
    }
    .button-bar {
        display: flex;
        gap: 1em;
    }
    :global(body.dark-mode) .sidebar {
    background-color: #2f2f2f;
    color: #f0f0f0;
  }

    button {
        display: flex;
        align-items: center;
        padding: 0.5em 1em;
        margin-top: 2px;
        background-color: #f9f9f9;
        color: white;
        cursor: pointer;
        border-radius: 50px;
        font-size: 1em;
        transition: transform 0.2s ease;
    }
    button i {
        margin-right: 0.5em;
    }
    button:hover {
        transform: scale(1.1);
    }
    .bottom-buttons{
        margin-top: 600px;
    }
    .bottom-buttons p{
        color:black;
        font-family: 'Times New Roman', Times, serif;
        margin-left: 20px;
        margin-top: 2px;
    }
    
    
</style>

<div class="sidebar {isSidebarVisible ? '' : 'hidden'}">
    <div class="button-bar">
        <button style="margin-left: 210px;" on:click={reloadPage}>
            <img src="e1.png" alt="New Icon" style="vertical-align: middle;" width="25px">
        </button>
    </div>
    <slot></slot>
   
    

</div>
