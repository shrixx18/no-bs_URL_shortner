const originalUrlInput = document.getElementById("originalUrl");
const shortUrlInput = document.getElementById("shortUrl");
const copyBtn = document.getElementById("copyBtn");

const API_BASE = "https://YOUR-BACKEND.onrender.com";

originalUrlInput.addEventListener("change", async () => {
    const originalUrl = originalUrlInput.value.trim();

    if (!originalUrl) {
        shortUrlInput.value = "";
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/shorten`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                original_url: originalUrl
            })
        });

        if (!response.ok) {
            throw new Error("Failed to shorten URL");
        }

        const data = await response.json();
        shortUrlInput.value = data.short_url;

    } catch (error) {
        alert("Error shortening URL");
        console.error(error);
    }
});

copyBtn.addEventListener("click", () => {
    if (!shortUrlInput.value) return;

    navigator.clipboard.writeText(shortUrlInput.value)
        .then(() => {
            copyBtn.innerText = "Copied";
            setTimeout(() => copyBtn.innerText = "Copy", 1500);
        });
});
