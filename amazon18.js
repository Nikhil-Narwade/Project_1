const searchInput = document.getElementById("searchInput");
const categoryFilter = document.getElementById("categoryFilter");
const priceFilter = document.getElementById("priceFilter");
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
const subtotalEl = document.getElementById("subtotal");
const gstEl = document.getElementById("gst");
const totalItemsEl = document.getElementById("totalItems");
const clearCartBtn = document.getElementById("clearCart");
const darkToggle = document.getElementById("darkToggle");
const toast = document.getElementById("toast");

let cart = JSON.parse(localStorage.getItem("cart18")) || [];
let wishlist = JSON.parse(localStorage.getItem("wishlist18")) || [];

updateCart();
updateWishlist();

function showToast(msg){
    toast.textContent = msg;
    toast.style.display = "block";
    setTimeout(()=> toast.style.display = "none", 1500);
}

function applyFilters(){
    const search = searchInput.value.toLowerCase();
    const cat = categoryFilter.value;
    const price = priceFilter.value;

    document.querySelectorAll(".card").forEach(card=>{
        let show = true;

        if(search && !card.dataset.name.toLowerCase().includes(search)) show = false;
        if(cat && card.dataset.category !== cat) show = false;

        if(price){
            const [min,max] = price.split("-").map(Number);
            const p = Number(card.dataset.price);
            if(!(p >= min && p <= max)) show = false;
        }

        card.style.display = show ? "block" : "none";
    });
}

searchInput.onkeyup = applyFilters;
categoryFilter.onchange = applyFilters;
priceFilter.onchange = applyFilters;

sortSelect.onchange = () => {
    const cards = [...document.querySelectorAll(".card")];
    cards.sort((a,b)=> sortSelect.value==="low"
        ? a.dataset.price - b.dataset.price
        : b.dataset.price - a.dataset.price);
    const container = document.getElementById("productList");
    container.innerHTML = "";
    cards.forEach(c=>container.appendChild(c));
};

document.querySelectorAll(".qtyPlus").forEach(btn=>{
    btn.onclick = ()=> btn.previousElementSibling.value++;
});
document.querySelectorAll(".qtyMinus").forEach(btn=>{
    btn.onclick = ()=>{
        const input = btn.nextElementSibling;
        if(input.value > 1) input.value--;
    };
});

document.querySelectorAll(".addBtn").forEach(btn=>{
    btn.onclick = e=>{
        const card = e.target.closest(".card");
        const name = card.dataset.name;
        const price = Number(card.dataset.price);
        const qty = Number(card.querySelector("input").value);

        const item = cart.find(i=>i.name===name);
        if(item) item.qty += qty;
        else cart.push({name,price,qty});

        saveCart();
        showToast("Added to cart");
    };
});

document.querySelectorAll(".wishBtn").forEach(btn=>{
    btn.onclick = e=>{
        const name = e.target.closest(".card").dataset.name;
        if(!wishlist.includes(name)){
            wishlist.push(name);
            saveWishlist();
            showToast("Added to wishlist");
        }
    };
});

function updateCart(){
    cartItemsDiv.innerHTML = "";
    let subtotal = 0;
    let totalItems = 0;

    cart.forEach((item,i)=>{
        subtotal += item.price * item.qty;
        totalItems += item.qty;
        cartItemsDiv.innerHTML += `
            <div>
                ${item.name} x${item.qty}
                <button onclick="removeItem(${i})">X</button>
            </div>`;
    });

    const gst = Math.floor(subtotal * 0.18);
    const total = subtotal + gst;

    subtotalEl.textContent = subtotal;
    gstEl.textContent = gst;
    totalPriceEl.textContent = total;
    totalItemsEl.textContent = totalItems;
    cartCount.textContent = totalItems;
}

function removeItem(i){
    cart.splice(i,1);
    saveCart();
}
