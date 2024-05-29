<!-- Card.svelte -->
<script>
    export let image;
    export let text;
</script>

<style>
    .card {
        width: 170px;
        height: 110px;
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        transition: transform 0.3s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    .card p {
        font-size: 14px;
        text-align: center;
        margin: 0;
        color: #c6bebe;
    }

    /* Style the image */
    img {
        max-width: 15%; /* Adjust the max-width as needed */
    }
</style>

<div class="card">
    <img src={image} alt="Image">
    <p>{text}</p>
</div>
