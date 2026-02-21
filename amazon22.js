const productList=document.getElementById("productList");
const overlay=document.getElementById("overlay");

const products=[
{name:"Smartphone",price:9999,cat:"electronics"},
{name:"Headphones",price:1999,cat:"electronics"},
{name:"Smart Watch",price:2499,cat:"electronics"},
{name:"Keyboard",price:699,cat:"electronics"},
{name:"Mouse",price:499,cat:"electronics"},
{name:"Power Bank",price:1299,cat:"electronics"},
{name:"T-Shirt",price:499,cat:"fashion"},
{name:"Shoes",price:2199,cat:"fashion"},
{name:"Backpack",price:999,cat:"fashion"},
{name:"Handbag",price:1499,cat:"fashion"},
{name:"Desk Lamp",price:899,cat:"home"},
{name:"Office Chair",price:5499,cat:"home"},
{name:"Coffee Mug",price:199,cat:"home"},
{name:"Water Bottle",price:299,cat:"home"},
{name:"Bedsheet",price:1299,cat:"home"}
];

let cart=JSON.parse(localStorage.getItem("cart21"))||[];
let wishlist=JSON.parse(localStorage.getItem("wishlist21"))||[];
let discountPercent=0;

const cartBtn=document.getElementById("cartBtn");
const wishlistBtn=document.getElementById("wishlistBtn");
const cartDrawer=document.getElementById("cartDrawer");
const wishlistDrawer=document.getElementById("wishlistDrawer");

const cartItemsDiv=document.getElementById("cartItems");
const wishlistItemsDiv=document.getElementById("wishlistItems");

const cartCount=document.getElementById("cartCount");
const wishCount=document.getElementById("wishCount");

const subtotalEl=document.getElementById("subtotal");
const gstEl=document.getElementById("gst");
const deliveryEl=document.getElementById("delivery");
const discountEl=document.getElementById("discount");
const totalPriceEl=document.getElementById("totalPrice");

const toast=document.getElementById("toast");

function showToast(msg){
toast.textContent=msg;
toast.classList.add("show");
setTimeout(()=>toast.classList.remove("show"),1500);
}

function randomRating(){return (Math.random()*2+3).toFixed(1)}

function renderProducts(){
productList.innerHTML="";

let filtered=[...products];

const search=document.getElementById("searchInput").value.toLowerCase();
const cat=document.getElementById("categoryFilter").value;
const sort=document.getElementById("sortPrice").value;

if(search)filtered=filtered.filter(p=>p.name.toLowerCase().includes(search));
if(cat)filtered=filtered.filter(p=>p.cat===cat);

if(sort==="low")filtered.sort((a,b)=>a.price-b.price);
if(sort==="high")filtered.sort((a,b)=>b.price-a.price);

filtered.forEach(p=>{
const discount=Math.floor(Math.random()*40)+10;
const mrp=Math.floor(p.price*(1+discount/100));

const inCart=cart.find(i=>i.name===p.name);
const inWish=wishlist.includes(p.name);

productList.innerHTML+=`
<div class="card ${inCart?"inCart":""} ${inWish?"inWish":""}" data-name="${p.name}" data-category="${p.cat}" data-price="${p.price}">
<span class="badge">${discount}% off</span>
<img src="https://via.placeholder.com/200">
<h3>${p.name}</h3>
<div class="rating">⭐ ${randomRating()}</div>
<div class="price">₹${p.price} <span class="mrp">₹${mrp}</span></div>
<div class="free">Free Delivery</div>

<div class="qtyBox">
<button class="qtyMinus">-</button>
<input type="number" value="1" min="1">
<button class="qtyPlus">+</button>
</div>

<button class="addBtn">Add to Cart</button>
<button class="wishBtn">Wishlist</button>
</div>`;
});
}

renderProducts();

document.addEventListener("click",e=>{

if(e.target.classList.contains("qtyPlus"))e.target.previousElementSibling.value++;
if(e.target.classList.contains("qtyMinus")){
const input=e.target.nextElementSibling;
if(input.value>1)input.value--;
}

if(e.target.classList.contains("addBtn")){
const card=e.target.closest(".card");
const name=card.dataset.name;
const price=Number(card.dataset.price);
const qty=Number(card.querySelector("input").value);

const item=cart.find(i=>i.name===name);
if(item)item.qty+=qty;
else cart.push({name,price,qty});

saveCart();showToast("Added to cart");renderProducts();
}

if(e.target.classList.contains("wishBtn")){
const name=e.target.closest(".card").dataset.name;
if(!wishlist.includes(name))wishlist.push(name);
saveWishlist();showToast("Added to wishlist");renderProducts();
}

});

function updateCart(){
cartItemsDiv.innerHTML="";
let subtotal=0;

if(cart.length===0){
cartItemsDiv.innerHTML="<p>Cart is empty</p>";
}

cart.forEach((item,i)=>{
subtotal+=item.price*item.qty;
cartItemsDiv.innerHTML+=`
<div class="cartRow">
<span>${item.name}</span>
<div class="cartQty">
<button onclick="changeQty(${i},-1)">-</button>
<span>${item.qty}</span>
<button onclick="changeQty(${i},1)">+</button>
</div>
<span>₹${item.price*item.qty}</span>
<button onclick="removeItem(${i})">X</button>
</div>`;
});

const gst=Math.floor(subtotal*0.18);
const delivery=subtotal>2000||subtotal===0?0:99;
const discount=Math.floor(subtotal*(discountPercent/100));
const total=subtotal+gst+delivery-discount;

subtotalEl.textContent=subtotal;
gstEl.textContent=gst;
deliveryEl.textContent=delivery;
discountEl.textContent=discount;
totalPriceEl.textContent=total;

cartCount.textContent=cart.reduce((a,b)=>a+b.qty,0);
}

function changeQty(i,d){cart[i].qty+=d;if(cart[i].qty<=0)cart.splice(i,1);saveCart();renderProducts()}
function removeItem(i){cart.splice(i,1);saveCart();renderProducts()}

function saveCart(){localStorage.setItem("cart21",JSON.stringify(cart));updateCart()}

function updateWishlist(){
wishlistItemsDiv.innerHTML="";
if(wishlist.length===0)wishlistItemsDiv.innerHTML="<p>No items</p>";

wishlist.forEach((name,i)=>{
wishlistItemsDiv.innerHTML+=`<div>${name}<button onclick="removeWish(${i})">X</button></div>`;
});
wishCount.textContent=wishlist.length;
}

function removeWish(i){wishlist.splice(i,1);saveWishlist();renderProducts()}
function saveWishlist(){localStorage.setItem("wishlist21",JSON.stringify(wishlist));updateWishlist()}

cartBtn.onclick=()=>toggleDrawer(cartDrawer);
wishlistBtn.onclick=()=>toggleDrawer(wishlistDrawer);

function toggleDrawer(drawer){
const isActive=drawer.classList.contains("active");
document.querySelectorAll(".drawer").forEach(d=>d.classList.remove("active"));
overlay.classList.remove("show");
if(!isActive){
drawer.classList.add("active");
overlay.classList.add("show");
}
}

overlay.onclick=()=>{
document.querySelectorAll(".drawer").forEach(d=>d.classList.remove("active"));
overlay.classList.remove("show");
};

document.addEventListener("keydown",e=>{
if(e.key==="Escape")overlay.onclick();
});

document.getElementById("applyCoupon").onclick=()=>{
const code=document.getElementById("couponInput").value;
if(code==="SAVE10")discountPercent=10;
else if(code==="SAVE20")discountPercent=20;
else discountPercent=0;
updateCart();
};

document.getElementById("clearCoupon").onclick=()=>{
discountPercent=0;
document.getElementById("couponInput").value="";
updateCart();
};

document.getElementById("clearCart").onclick=()=>{cart=[];saveCart();renderProducts()};
document.getElementById("clearWish").onclick=()=>{wishlist=[];saveWishlist();renderProducts()};

document.getElementById("searchInput").oninput=renderProducts;
document.getElementById("categoryFilter").onchange=renderProducts;
document.getElementById("sortPrice").onchange=renderProducts;

document.getElementById("darkToggle").onclick=()=>{
document.body.classList.toggle("dark");
localStorage.setItem("dark21",document.body.classList.contains("dark"));
};

if(localStorage.getItem("dark21")==="true")document.body.classList.add("dark");

updateCart();
updateWishlist();
