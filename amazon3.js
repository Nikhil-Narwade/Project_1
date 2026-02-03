const searchInput = document.getElementById("searchInput");
const cards = [...document.querySelectorAll(".card")];
const cartCount = document.getElementById("cartCount");
const cartModal = document.getElementById("cartModal");
const cartItemsDiv = document.getElementById("cartItems");
const totalPriceSpan = document.getElementById("totalPrice");

let cart = JSON.parse(localStorage.getItem("cart")) || [];

updateCart();

searchInput.addEventListener("input", filterProducts);

document.querySelectorAll(".menu button").forEach(btn => {
    btn.onclick = () => filterProducts(btn.dataset.category);
});

document.getElementById("sortPrice").onchange = e => {
    sortProducts(e.target.value);
};

cards.forEach(card => {
    card.querySelector("button").onclick = () => {
        cart.push({
            name: card.querySelector("h3").innerText,
            price: Number(card.dataset.price)
        });
        updateCart();
    };
});

document.getElementById("openCart").onclick = () => cartModal.style.display = "block";
document.getElementById("closeCart").onclick = () => cartModal.style.display = "none";

function filterProducts(category = "all") {
    const text = searchInput.value.toLowerCase();
    cards.forEach(card => {
        const matchText = card.dataset.name.includes(text);
        const matchCat = category === "all" || card.dataset.category === category;
        card.style.display = matchText && matchCat ? "block" : "none";
    });
}

function sortProducts(type) {
    const list = document.getElementById("productList");
    cards.sort((a, b) => {
        return type === "low"
            ? a.dataset.price - b.dataset.price
            : b.dataset.price - a.dataset.price;
    });
    cards.forEach(c => list.appendChild(c));
}

function updateCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
    cartCount.innerText = cart.length;
    cartItemsDiv.innerHTML = "";
    let total = 0;

    cart.forEach((item, i) => {
        total += item.price;
        cartItemsDiv.innerHTML += `
            <p>${item.name} - ₹${item.price}
            <button onclick="removeItem(${i})">x</button></p>`;
    });

    totalPriceSpan.innerText = total;
}

function removeItem(i) {
    cart.splice(i, 1);
    updateCart();
}
