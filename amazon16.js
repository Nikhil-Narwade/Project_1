const searchInput = document.getElementById("searchInput");
const ratingFilter = document.getElementById("ratingFilter");
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

const modal = document.getElementById("productModal");
const modalImg = document.getElementById("modalImg");
const modalName = document.getElementById("modalName");
const modalPrice = document.getElementById("modalPrice");

let cart = [];
let wishlist = [];

searchInput.onkeyup = filterProducts;
ratingFilter.onchange = filterProducts;

function filterProducts(){
    const value = searchInput.value.toLowerCase();
    const rating = ratingFilter.value;
    document.querySelectorAll(".card").forEach(card=>{
        const matchName = card.dataset.name.toLowerCase().includes(value);
        const matchRating = rating==="" || card.dataset.rating >= rating;
        card.style.display = matchName && matchRating ? "block":"none";
    });
}

document.querySelectorAll(".viewBtn").forEach(btn=>{
    btn.onclick = e=>{
        const card = e.target.closest(".card");
        modalImg.src = card.querySelector("img").src;
        modalName.textContent = card.dataset.name;
        modalPrice.textContent = "₹" + card.dataset.price;
        modal.style.display = "block";
    };
});

document.getElementById("closeModal").onclick = ()=> modal.style.display="none";
window.onclick = e=>{ if(e.target==modal) modal.style.display="none"; };

document.querySelectorAll(".addBtn").forEach(btn=>{
    btn.onclick = e=>{
        const card = e.target.closest(".card");
        const name = card.dataset.name;
        const price = Number(card.dataset.price);

        const item = cart.find(i=>i.name===name);
        if(item) item.qty++;
        else cart.push({name,price,qty:1});
        updateCart();
    };
});

document.querySelectorAll(".wishBtn").forEach(btn=>{
    btn.onclick = e=>{
        const name = e.target.closest(".card").dataset.name;
        if(!wishlist.includes(name)){
            wishlist.push(name);
            updateWishlist();
        }
    };
});

function updateCart(){
    cartItemsDiv.innerHTML="";
    let total=0;

    cart.forEach((item,i)=>{
        total+=item.price*item.qty;
        cartItemsDiv.innerHTML+=`
        <div>
            ${item.name}
            <input type="number" value="${item.qty}" min="1" onchange="changeQty(${i},this.value)">
            <button onclick="removeItem(${i})">X</button>
        </div>`;
    });

    cartCount.textContent = cart.reduce((a,b)=>a+b.qty,0);
    totalPriceEl.textContent = total;
}

function changeQty(i,val){
    cart[i].qty = Number(val);
    updateCart();
}

function removeItem(i){
    cart.splice(i,1);
    updateCart();
}

function updateWishlist(){
    wishlistItemsDiv.innerHTML="";
    wishlist.forEach((name,i)=>{
        wishlistItemsDiv.innerHTML+=`
        <div>
            ${name}
            <button onclick="removeWish(${i})">X</button>
        </div>`;
    });
    wishCount.textContent = wishlist.length;
}

function removeWish(i){
    wishlist.splice(i,1);
    updateWishlist();
}

cartBtn.onclick = ()=> cartDrawer.classList.toggle("active");
wishlistBtn.onclick = ()=> wishlistDrawer.classList.toggle("active");
darkToggle.onclick = ()=> document.body.classList.toggle("dark");
