const originalUrlInput = document.getElementById("originalUrl");
const shortUrlInput = document.getElementById("shortUrl");
const copyBtn = document.getElementById("copyBtn");

originalUrlInput.addEventListener("input", () => {
    const value = originalUrlInput.value.trim();

    if (value.length > 0) {
        // Dummy shortened URL (placeholder)
        shortUrlInput.value = "https://nobs.ly/abc123";
    } else {
        shortUrlInput.value = "";
    }
});

copyBtn.addEventListener("click", () => {
    if (!shortUrlInput.value) return;

    navigator.clipboard.writeText(shortUrlInput.value)
        .then(() => {
            copyBtn.innerText = "Copied";
            setTimeout(() => {
                copyBtn.innerText = "Copy";
            }, 1500);
        })
        .catch(() => {
            alert("Failed to copy URL");
        });
});
