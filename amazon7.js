const productsData = [
    { id: 1, name: "Laptop", price: 55000, category: "electronics" },
    { id: 2, name: "Headphones", price: 2000, category: "electronics" },
    { id: 3, name: "T-Shirt", price: 800, category: "fashion" },
    { id: 4, name: "Shoes", price: 3000, category: "fashion" }
];

let cart = [];
let currentCategory = "all";

const productsDiv = document.getElementById("products");
const cartCount = document.getElementById("cartCount");
const cartModal = document.getElementById("cartModal");
const cartItems = document.getElementById("cartItems");
const totalPrice = document.getElementById("totalPrice");
const searchInput = document.getElementById("search");

function renderProducts() {
    productsDiv.innerHTML = "";

    productsData
        .filter(p => currentCategory === "all" || p.category === currentCategory)
        .filter(p => p.name.toLowerCase().includes(searchInput.value.toLowerCase()))
        .forEach(p => {
            const div = document.createElement("div");
            div.className = "card";
            div.innerHTML = `
                <h3>${p.name}</h3>
                <p>₹${p.price}</p>
                <button onclick="addToCart(${p.id})">Add to Cart</button>
            `;
            productsDiv.appendChild(div);
        });
}

function addToCart(id) {
    const product = productsData.find(p => p.id === id);
    cart.push(product);
    cartCount.textContent = cart.length;
}

function filterCategory(cat) {
    currentCategory = cat;
    renderProducts();
}

function openCart() {
    cartModal.classList.remove("hidden");
    renderCart();
}

function closeCart() {
    cartModal.classList.add("hidden");
}

function renderCart() {
    cartItems.innerHTML = "";
    let sum = 0;

    cart.forEach((item, index) => {
        sum += item.price;
        const li = document.createElement("li");
        li.innerHTML = `
            ${item.name} - ₹${item.price}
            <button onclick="removeItem(${index})">X</button>
        `;
        cartItems.appendChild(li);
    });

    totalPrice.textContent = sum;
}

function removeItem(index) {
    cart.splice(index, 1);
    cartCount.textContent = cart.length;
    renderCart();
}

document.getElementById("cartBtn").onclick = openCart;
searchInput.oninput = renderProducts;

renderProducts();
