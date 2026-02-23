const productList = document.getElementById("productList");

const products = [
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

function randomRating(){return (Math.random()*2+3).toFixed(1)}

function createProducts(filteredProducts = products){
  productList.innerHTML="";
  filteredProducts.forEach(p=>{
    const discount = Math.floor(Math.random()*40)+10;
    const mrp = Math.floor(p.price*(1+discount/100));
    const rating = randomRating();
    productList.innerHTML+=`
      <div class="card" data-name="${p.name}" data-category="${p.cat}" data-price="${p.price}" data-rating="${rating}">
        <span class="badge">${discount}% off</span>
        <img src="https://via.placeholder.com/200">
        <h3>${p.name}</h3>
        <div class="rating">⭐ ${rating}</div>
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

createProducts();

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
const deliveryEl = document.getElementById("delivery");
const discountEl = document.getElementById("discount");
const toast = document.getElementById("toast");

let cart = JSON.parse(localStorage.getItem("cart23"))||[];
let wishlist = JSON.parse(localStorage.getItem("wishlist23"))||[];
let discount = 0;

// ---- TOAST ----
function showToast(msg){
  toast.textContent = msg;
  toast.classList.add("show");
  setTimeout(()=>toast.classList.remove("show"),1500);
}

// ---- CART & WISHLIST ACTIONS ----
document.addEventListener("click", e=>{
  if(e.target.classList.contains("qtyPlus")) e.target.previousElementSibling.value++;
  if(e.target.classList.contains("qtyMinus")){
    const input = e.target.nextElementSibling;
    if(input.value>1) input.value--;
  }

  if(e.target.classList.contains("addBtn")){
    const card = e.target.closest(".card");
    const name = card.dataset.name;
    const price = Number(card.dataset.price);
    const qty = Number(card.querySelector("input").value);
    const item = cart.find(i=>i.name===name);
    if(item) item.qty+=qty;
    else cart.push({name,price,qty});
    saveCart();
    showToast("Added to cart");
  }

  if(e.target.classList.contains("wishBtn")){
    const name = e.target.closest(".card").dataset.name;
    if(!wishlist.includes(name)){
      wishlist.push(name);
      saveWishlist();
      showToast("Added to wishlist");
    }
  }
});


function updateCart(){
  cartItemsDiv.innerHTML="";
  let subtotal=0;

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

  const gst = Math.floor(subtotal*0.18);
  const delivery = subtotal>2000?0:99;
  const total = subtotal+gst+delivery-discount;

  subtotalEl.textContent=subtotal;
  gstEl.textContent=gst;
  deliveryEl.textContent=delivery;
  discountEl.textContent=discount;
  totalPriceEl.textContent=total;
  cartCount.textContent=cart.reduce((a,b)=>a+b.qty,0);
}


function changeQty(i,d){cart[i].qty+=d;if(cart[i].qty<=0)cart.splice(i,1);saveCart()}
function removeItem(i){cart.splice(i,1);saveCart()}

function saveCart(){localStorage.setItem("cart23",JSON.stringify(cart));updateCart()}


function updateWishlist(){
  wishlistItemsDiv.innerHTML="";
  wishlist.forEach((name,i)=>{
    wishlistItemsDiv.innerHTML+=`
      <div>${name} 
        <button onclick="moveToCart(${i})">🛒</button>
        <button onclick="removeWish(${i})">X</button>
      </div>`;
  });
  wishCount.textContent=wishlist.length;
}
function removeWish(i){wishlist.splice(i,1);saveWishlist()}
function moveToCart(i){
  const name = wishlist[i];
  const itemInCart = cart.find(x=>x.name===name);
  const price = products.find(x=>x.name===name).price;
  if(itemInCart) itemInCart.qty++;
  else cart.push({name,price,qty:1});
  wishlist.splice(i,1);
  saveWishlist();
  saveCart();
  showToast("Moved to cart");
}
function saveWishlist(){localStorage.setItem("wishlist23",JSON.stringify(wishlist));updateWishlist()}


cartBtn.onclick=()=>cartDrawer.classList.toggle("active");
wishlistBtn.onclick=()=>wishlistDrawer.classList.toggle("active");


document.getElementById("applyCoupon").onclick=()=>{
  const code = document.getElementById("couponInput").value.toUpperCase();
  if(code==="SAVE10") discount = Math.floor(Number(subtotalEl.textContent)*0.1);
  else if(code==="SAVE20") discount = Math.floor(Number(subtotalEl.textContent)*0.2);
  else if(code==="FREESHIP") discount = Number(deliveryEl.textContent); // free delivery
  else discount = 0;
  updateCart();
  showToast(`Coupon ${code} applied`);
};


document.getElementById("clearCart").onclick=()=>{cart=[];saveCart()};
document.getElementById("clearWish").onclick=()=>{wishlist=[];saveWishlist()};


const darkToggle = document.getElementById("darkToggle");
darkToggle.onclick = () => {
  document.body.classList.toggle("dark");
  darkToggle.textContent = document.body.classList.contains("dark")?"☀️":"🌙";
}


const searchInput = document.getElementById("searchInput");
searchInput.oninput = () => {
  const query = searchInput.value.toLowerCase();
  const filtered = products.filter(p=>p.name.toLowerCase().includes(query));
  createProducts(filtered);
}


const sortSelect = document.getElementById("sortSelect");
if(sortSelect){
  sortSelect.onchange = ()=>{
    let filtered = [...products];
    if(sortSelect.value==="priceAsc") filtered.sort((a,b)=>a.price-b.price);
    if(sortSelect.value==="priceDesc") filtered.sort((a,b)=>b.price-a.price);
    if(sortSelect.value==="ratingDesc") filtered.sort((a,b)=>Number(b.rating)-Number(a.rating));
    createProducts(filtered);
  }
}

updateCart();
updateWishlist();
