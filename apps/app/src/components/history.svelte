<script lang="ts">
    export let chatRequests: { text: string, time: Date }[];

    type ChatRequest = {
        text: string;
        time: Date;
    };

    type CategorizedRequests = {
        today: ChatRequest[];
        yesterday: ChatRequest[];
        last7Days: ChatRequest[];
    };

    function categorizeChatRequests(): CategorizedRequests {
        const today = new Date();
        today.setHours(0, 0, 0, 0);

        const yesterday = new Date(today);
        yesterday.setDate(yesterday.getDate() - 1);
        yesterday.setHours(0, 0, 0, 0);

        const categorizedRequests: CategorizedRequests = {
            today: [],
            yesterday: [],
            last7Days: []
        };

        chatRequests.forEach(request => {
            const requestTime = new Date(request.time);
            requestTime.setHours(0, 0, 0, 0);

            if (requestTime.getTime() === today.getTime()) {
                categorizedRequests.today.push(request);
            } else if (requestTime.getTime() === yesterday.getTime()) {
                categorizedRequests.yesterday.push(request);
            } else if (requestTime > yesterday && requestTime < today) {
                categorizedRequests.last7Days.push(request);
            }
        });

        return categorizedRequests;
    }

    let categorizedChatRequests = categorizeChatRequests();
</script>

<style>
    .history {
        flex-grow: 1;
        overflow-y: auto;
        background-color: #f9f9f9;
        border-radius: 8px;
        padding: 1em;
    }
    .history-item {
        margin-bottom: 0.5em;
        padding: 0.5em;
        background: #f9f9f9;
        border: 1px solid #f9f9f9;
        border-radius: 4px;
    }
</style>

<div class="history">
    <h2>Today</h2>
    {#each categorizedChatRequests.today as request}
        <div class="history-item">{request.text}</div>
    {/each}
    <h2>Yesterday</h2>
    {#each categorizedChatRequests.yesterday as request}
        <div class="history-item">{request.text}</div>
    {/each}
    <h2>Last 7 Days</h2>
    {#each categorizedChatRequests.last7Days as request}
        <div class="history-item">{request.text}</div>
    {/each}
</div>
