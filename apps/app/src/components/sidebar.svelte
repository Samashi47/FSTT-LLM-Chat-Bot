<script>
    export let isSidebarVisible;
    export let toggleSidebar;
</script>

<style>
    .hidden { display: none; }
    .sidebar {
        width: 400px;
        background-color: #f9f9f9;
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
    button {
        display: flex;
        align-items: center;
        padding: 0.5em 1em;
        border: 2px solid #526D82;
        background-color: #3F2305;
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
</style>

<div class="sidebar {isSidebarVisible ? '' : 'hidden'}">
    <div class="button-bar">

        <button style="margin-left: 160px;">
            <i class="fas fa-pencil-alt"></i> New
        </button>
    </div>
    <slot></slot>
</div>
