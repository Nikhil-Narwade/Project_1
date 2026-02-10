const searchInput = document.getElementById("searchInput");
const cards = document.querySelectorAll(".card");
const cartCount = document.getElementById("cartCount");
const cartItemsDiv = document.getElementById("cartItems");
const totalPriceEl = document.getElementById("totalPrice");
const clearCartBtn = document.getElementById("clearCart");

let cart = JSON.parse(localStorage.getItem("cart")) || [];

updateCart();

searchInput.addEventListener("keyup", () => {
    const value = searchInput.value.toLowerCase();
    cards.forEach(card => {
        const text = card.dataset.name + " " + card.dataset.category;
        card.style.display = text.includes(value) ? "block" : "none";
    });
});

cards.forEach(card => {
    card.querySelector("button").addEventListener("click", () => {
        const name = card.querySelector("h3").textContent;
        const price = Number(card.dataset.price);

        const item = cart.find(p => p.name === name);
        if (item) item.qty++;
        else cart.push({ name, price, qty: 1 });

        saveCart();
    });
});

function updateCart() {
    cartItemsDiv.innerHTML = "";
    let total = 0;

    if (cart.length === 0) {
        cartItemsDiv.innerHTML = "<p>Cart is empty</p>";
    }

    cart.forEach((item, index) => {
        total += item.price * item.qty;
        cartItemsDiv.innerHTML += `
            <div class="cart-item">
                ${item.name} (₹${item.price})
                <div>
                    <button onclick="changeQty(${index}, -1)">-</button>
                    ${item.qty}
                    <button onclick="changeQty(${index}, 1)">+</button>
                </div>
            </div>
        `;
    });

    cartCount.textContent = cart.reduce((a,b) => a + b.qty, 0);
    totalPriceEl.textContent = total;
}

function changeQty(index, change) {
    cart[index].qty += change;
    if (cart[index].qty === 0) cart.splice(index, 1);
    saveCart();
}

function saveCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCart();
}

clearCartBtn.addEventListener("click", () => {
    cart = [];
    saveCart();
});
