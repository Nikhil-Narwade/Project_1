const searchInput = document.getElementById("searchInput");
const cards = [...document.querySelectorAll(".card")];
const cartModal = document.getElementById("cartModal");
const cartItemsDiv = document.getElementById("cartItems");
const cartCount = document.getElementById("cartCount");
const totalSpan = document.getElementById("total");

let cart = JSON.parse(localStorage.getItem("cart")) || [];
let wishlist = JSON.parse(localStorage.getItem("wishlist")) || [];

updateCart();

searchInput.oninput = () => {
    const v = searchInput.value.toLowerCase();
    cards.forEach(c => {
        c.style.display = c.dataset.name.includes(v) ? "block" : "none";
    });
};

document.querySelectorAll(".menu button").forEach(b => {
    b.onclick = () => {
        const cat = b.dataset.category;
        cards.forEach(c => {
            c.style.display = cat === "all" || c.dataset.category === cat ? "block" : "none";
        });
    };
});

cards.forEach(card => {
    card.querySelector(".add").onclick = () => {
        const name = card.querySelector("h3").innerText;
        const price = Number(card.dataset.price);
        const item = cart.find(i => i.name === name);
        if (item) item.qty++;
        else cart.push({ name, price, qty: 1 });
        updateCart();
    };

    card.querySelector(".wish").onclick = () => {
        const name = card.querySelector("h3").innerText;
        if (!wishlist.includes(name)) wishlist.push(name);
        localStorage.setItem("wishlist", JSON.stringify(wishlist));
        alert("Added to wishlist ❤️");
    };
});

document.getElementById("openCart").onclick = () => cartModal.style.display = "block";
document.getElementById("closeCart").onclick = () => cartModal.style.display = "none";

document.getElementById("checkout").onclick = () => {
    alert("Order placed! Total ₹" + totalSpan.innerText);
    cart = [];
    updateCart();
};

document.getElementById("darkMode").onclick = () => {
    document.body.classList.toggle("dark");
};

function updateCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
    cartItemsDiv.innerHTML = "";
    let total = 0;
    let count = 0;

    cart.forEach((i, idx) => {
        total += i.price * i.qty;
        count += i.qty;
        cartItemsDiv.innerHTML += `
            <p>${i.name} x ${i.qty}
            <button onclick="changeQty(${idx},1)">+</button>
            <button onclick="changeQty(${idx},-1)">-</button></p>
        `;
    });

    totalSpan.innerText = total;
    cartCount.innerText = count;
}

window.changeQty = function (i, d) {
    cart[i].qty += d;
    if (cart[i].qty <= 0) cart.splice(i, 1);
    updateCart();
};
