<!-- MainContent.svelte -->
<script lang="ts">
    import Card from './Card.svelte';
    import Prompt from './Prompt.svelte';

    export let isSidebarVisible: boolean;
</script>

<style>
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
        color: #3F2305;
    }
</style>

<div class="main-content" style="--main-content-margin: {isSidebarVisible ? '400px' : '0'};">
    <h1 class="heading-animation" style="margin-top: 200px;">FSTT CHATBOT</h1>
    <div class="image-container">
        <img src="/home.png" alt="Home Image">
    </div>
    
    <div class="card-container">
        <Card image="/t1.png" text="Courses in MST AISD examination" />
        <Card image="/t2.png" text="The details of the Mevlana program" />
        <Card image="/l4.png" text="The link to access my scholarly paper." />
        <Card image="/q4.png" text="Who is the coordinator of LSI CI?" />
    </div>

    <div style="height: 700px;"></div>

    <Prompt />
</div>
