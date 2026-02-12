const searchInput = document.getElementById("searchInput");
const sortSelect = document.getElementById("sortSelect");
const cartBtn = document.getElementById("cartBtn");
const wishlistBtn = document.getElementById("wishlistBtn");
const cartDrawer = document.getElementById("cartDrawer");
const wishlistDrawer = document.getElementById("wishlistDrawer");
const cartItemsDiv = document.getElementById("cartItems");
const wishlistItemsDiv = document.getElementById("wishlistItems");
const cartCount = document.getElementById("cartCount");
const wishCount = document.getElementById("wishCount");
const totalPriceEl = document.getElementById("totalPrice");
const darkToggle = document.getElementById("darkToggle");

let cart = JSON.parse(localStorage.getItem("cart14")) || [];
let wishlist = JSON.parse(localStorage.getItem("wishlist14")) || [];

updateCart();
updateWishlist();

searchInput.onkeyup = () => {
    const value = searchInput.value.toLowerCase();
    document.querySelectorAll(".card").forEach(card => {
        card.style.display = card.dataset.name.toLowerCase().includes(value) ? "block" : "none";
    });
};

sortSelect.onchange = () => {
    const cards = [...document.querySelectorAll(".card")];
    cards.sort((a,b) => sortSelect.value === "low"
        ? a.dataset.price - b.dataset.price
        : b.dataset.price - a.dataset.price);
    const container = document.getElementById("productList");
    container.innerHTML = "";
    cards.forEach(c => container.appendChild(c));
};

document.querySelectorAll(".addBtn").forEach(btn => {
    btn.onclick = e => {
        const card = e.target.closest(".card");
        const name = card.dataset.name;
        const price = Number(card.dataset.price);
        const qty = Number(card.querySelector(".qtyInput").value);

        const item = cart.find(i => i.name === name);
        if (item) item.qty += qty;
        else cart.push({name, price, qty});

        saveCart();
    };
});

document.querySelectorAll(".wishBtn").forEach(btn => {
    btn.onclick = e => {
        const card = e.target.closest(".card");
        const name = card.dataset.name;

        if (!wishlist.includes(name)) wishlist.push(name);
        saveWishlist();
    };
});

function updateCart(){
    cartItemsDiv.innerHTML = "";
    let total = 0;

    if(cart.length === 0) cartItemsDiv.innerHTML = "<p>Cart empty</p>";

    cart.forEach((item,i)=>{
        total += item.price * item.qty;
        cartItemsDiv.innerHTML += `
            <div>
                ${item.name} x${item.qty}
                <button onclick="changeQty(${i},1)">+</button>
                <button onclick="changeQty(${i},-1)">-</button>
                <button onclick="removeItem(${i})">X</button>
            </div>
        `;
    });

    cartCount.textContent = cart.reduce((a,b)=>a+b.qty,0);
    totalPriceEl.textContent = total;
}

function changeQty(i,val){
    cart[i].qty += val;
    if(cart[i].qty <= 0) cart.splice(i,1);
    saveCart();
}

function removeItem(i){
    cart.splice(i,1);
    saveCart();
}

function saveCart(){
    localStorage.setItem("cart14", JSON.stringify(cart));
    updateCart();
}

function updateWishlist(){
    wishlistItemsDiv.innerHTML = "";
    if(wishlist.length===0) wishlistItemsDiv.innerHTML = "<p>Wishlist empty</p>";
    wishlist.forEach(name=>{
        wishlistItemsDiv.innerHTML += `<div>${name}</div>`;
    });
    wishCount.textContent = wishlist.length;
}

function saveWishlist(){
    localStorage.setItem("wishlist14", JSON.stringify(wishlist));
    updateWishlist();
}

cartBtn.onclick = ()=> cartDrawer.classList.toggle("active");
wishlistBtn.onclick = ()=> wishlistDrawer.classList.toggle("active");
darkToggle.onclick = ()=> document.body.classList.toggle("dark");
