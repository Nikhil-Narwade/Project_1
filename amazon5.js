const products = [
    { id: 1, name: "Smartphone", price: 9999, img: "https://via.placeholder.com/200" },
    { id: 2, name: "Headphones", price: 1499, img: "https://via.placeholder.com/200" },
    { id: 3, name: "Smart Watch", price: 1999, img: "https://via.placeholder.com/200" },
    { id: 4, name: "Laptop Bag", price: 799, img: "https://via.placeholder.com/200" }
];

let cart = JSON.parse(localStorage.getItem("cart")) || [];

const productList = document.getElementById("productList");
const cartPanel = document.getElementById("cartPanel");
const cartBtn = document.getElementById("cartBtn");
const cartItems = document.getElementById("cartItems");
const cartCount = document.getElementById("cartCount");
const totalEl = document.getElementById("total");

function renderProducts() {
    productList.innerHTML = "";
    products.forEach(p => {
        productList.innerHTML += `
            <div class="card">
                <img src="${p.img}">
                <h3>${p.name}</h3>
                <p>₹${p.price}</p>
                <button onclick="addToCart(${p.id})">Add to Cart</button>
            </div>`;
    });
}

function addToCart(id) {
    const item = cart.find(i => i.id === id);
    if (item) item.qty++;
    else {
        const p = products.find(p => p.id === id);
        cart.push({ ...p, qty: 1 });
    }
    updateCart();
}

function updateCart() {
    cartItems.innerHTML = "";
    let total = 0;
    cart.forEach(i => {
        total += i.price * i.qty;
        cartItems.innerHTML += `<p>${i.name} x ${i.qty}</p>`;
    });
    totalEl.textContent = total;
    cartCount.textContent = cart.reduce((a, b) => a + b.qty, 0);
    localStorage.setItem("cart", JSON.stringify(cart));
}

cartBtn.onclick = () => cartPanel.classList.add("open");
document.getElementById("closeCart").onclick = () => cartPanel.classList.remove("open");

renderProducts();
updateCart();

