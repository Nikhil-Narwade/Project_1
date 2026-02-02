const searchInput = document.getElementById("searchInput");
const cards = document.querySelectorAll(".card");
const cartCount = document.getElementById("cartCount");
const clearCartBtn = document.getElementById("clearCart");

let count = 0;

/* SEARCH */
searchInput.addEventListener("keyup", () => {
    const value = searchInput.value.toLowerCase();

    cards.forEach(card => {
        const name = card.dataset.name;
        card.style.display = name.includes(value) ? "block" : "none";
    });
});

/* ADD TO CART */
document.querySelectorAll(".addBtn").forEach(btn => {
    btn.addEventListener("click", () => {
        count++;
        cartCount.textContent = count;
        btn.textContent = "Added ✔";
        btn.disabled = true;
        alert("Item added to cart!");
    });
});

/* CLEAR CART */
clearCartBtn.addEventListener("click", () => {
    count = 0;
    cartCount.textContent = count;

    document.querySelectorAll(".addBtn").forEach(btn => {
        btn.textContent = "Add to Cart";
        btn.disabled = false;
    });
});
