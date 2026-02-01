const searchInput = document.getElementById("searchInput");
const cards = document.querySelectorAll(".card");

searchInput.addEventListener("keyup", function () {
    const value = searchInput.value.toLowerCase();

    cards.forEach(card => {
        const productName = card.getAttribute("data-name");

        if (productName.includes(value)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});
