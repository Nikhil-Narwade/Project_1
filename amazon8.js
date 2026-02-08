const products = [
    { id: 1, name: "Headphones", price: 1999, category: "electronics" },
    { id: 2, name: "Smart Watch", price: 2999, category: "electronics" },
    { id: 3, name: "T-Shirt", price: 799, category: "fashion" },
    { id: 4, name: "Shoes", price: 2499, category: "fashion" }
];

let cart = JSON.parse(localStorage.getItem("cart")) || [];

const productDiv = document.getElementById("products");
const cartDiv = document.getElementById("cart");
const cartItems = document.getElementById("cartItems");
const totalSpan = document.getElementById("total");
const cartCount = document.getElementById("cartCount");

function renderProducts(list) {
    productDiv.innerHTML = "";
    list.forEach(p => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
            <h3>${p.name}</h3>
            <p>₹${p.price}</p>
            <button onclick="addToCart(${p.id})">Add to Cart</button>
        `;
        productDiv.appendChild(div);
    });
}

function addToCart(id) {
    const item = cart.find(i => i.id === id);
    if (item) {
        item.qty++;
    } else {
        const product = products.find(p => p.id === id);
        cart.push({ ...product, qty: 1 });
    }
    updateCart();
}

function updateCart() {
    cartItems.innerHTML = "";
    let total = 0;
    cart.forEach(item => {
        total += item.price * item.qty;
        cartItems.innerHTML += `
            <div class="cart-item">
                <span>${item.name} x ${item.qty}</span>
                <button onclick="removeItem(${item.id})">❌</button>
            </div>
        `;
    });
    totalSpan.textContent = total;
    cartCount.textContent = cart.reduce((a,b)=>a+b.qty,0);
    localStorage.setItem("cart", JSON.stringify(cart));
}

function removeItem(id) {
    cart = cart.filter(i => i.id !== id);
    updateCart();
}

document.getElementById("cartBtn").onclick = () => {
    cartDiv.classList.toggle("hidden");
};

document.getElementById("search").oninput = e => {
    const value = e.target.value.toLowerCase();
    renderProducts(products.filter(p => p.name.toLowerCase().includes(value)));
};

document.getElementById("category").onchange = e => {
    const value = e.target.value;
    renderProducts(value === "all" ? products : products.filter(p => p.category === value));
};

renderProducts(products);
updateCart();
