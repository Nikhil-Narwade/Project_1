const searchInput = document.getElementById("searchInput");
const sortSelect = document.getElementById("sortSelect");
const categoryFilter = document.getElementById("categoryFilter");
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
const toast = document.getElementById("toast");

let cart = JSON.parse(localStorage.getItem("cart15")) || [];
let wishlist = JSON.parse(localStorage.getItem("wishlist15")) || [];
if(localStorage.getItem("dark15")==="true") document.body.classList.add("dark");

updateCart();
updateWishlist();

function showToast(msg){
    toast.textContent = msg;
    toast.style.opacity = 1;
    setTimeout(()=>toast.style.opacity=0,2000);
}

searchInput.onkeyup = filterProducts;
categoryFilter.onchange = filterProducts;

function filterProducts(){
    const value = searchInput.value.toLowerCase();
    const category = categoryFilter.value;
    document.querySelectorAll(".card").forEach(card=>{
        const matchName = card.dataset.name.toLowerCase().includes(value);
        const matchCategory = category === "" || card.dataset.category === category;
        card.style.display = matchName && matchCategory ? "block" : "none";
    });
}

sortSelect.onchange = () => {
    const cards = [...document.querySelectorAll(".card")];
    cards.sort((a,b)=>sortSelect.value==="low"
        ? a.dataset.price - b.dataset.price
        : b.dataset.price - a.dataset.price);
    const container = document.getElementById("productList");
    container.innerHTML = "";
    cards.forEach(c=>container.appendChild(c));
};

document.querySelectorAll(".addBtn").forEach(btn=>{
    btn.onclick = e=>{
        const card = e.target.closest(".card");
        const name = card.dataset.name;
        const price = Number(card.dataset.price);
        const qty = Number(card.querySelector(".qtyInput").value);

        const item = cart.find(i=>i.name===name);
        if(item) item.qty += qty;
        else cart.push({name,price,qty});

        saveCart();
        showToast("Added to cart");
    };
});

document.querySelectorAll(".wishBtn").forEach(btn=>{
    btn.onclick = e=>{
        const card = e.target.closest(".card");
        const name = card.dataset.name;

        if(!wishlist.includes(name)){
            wishlist.push(name);
            saveWishlist();
            showToast("Added to wishlist");
        }
    };
});

function updateCart(){
    cartItemsDiv.innerHTML = "";
    let total = 0;

    if(cart.length===0) cartItemsDiv.innerHTML = "<p>Cart empty</p>";

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
    if(cart[i].qty<=0) cart.splice(i,1);
    saveCart();
}

function removeItem(i){
    cart.splice(i,1);
    saveCart();
}

function saveCart(){
    localStorage.setItem("cart15", JSON.stringify(cart));
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
    localStorage.setItem("wishlist15", JSON.stringify(wishlist));
    updateWishlist();
}

document.getElementById("clearCart").onclick = ()=>{
    cart = [];
    saveCart();
};

document.getElementById("clearWishlist").onclick = ()=>{
    wishlist = [];
    saveWishlist();
};

cartBtn.onclick = ()=> cartDrawer.classList.toggle("active");
wishlistBtn.onclick = ()=> wishlistDrawer.classList.toggle("active");

window.onclick = e=>{
    if(!cartDrawer.contains(e.target) && !cartBtn.contains(e.target)) cartDrawer.classList.remove("active");
    if(!wishlistDrawer.contains(e.target) && !wishlistBtn.contains(e.target)) wishlistDrawer.classList.remove("active");
};

darkToggle.onclick = ()=>{
    document.body.classList.toggle("dark");
    localStorage.setItem("dark15", document.body.classList.contains("dark"));
};
