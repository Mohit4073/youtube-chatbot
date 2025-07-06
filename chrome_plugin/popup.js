document.getElementById("askBtn").addEventListener("click", async () => {
    const videoId = document.getElementById("videoId").value;
    const query = document.getElementById("query").value;

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ video_id: videoId, query: query })
    });

    const data = await response.json();
    document.getElementById("response").innerText = data.response;
});
