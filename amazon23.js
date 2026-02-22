
const productList = document.getElementById("productList");
const cartBtn = document.getElementById("cartBtn");
const wishlistBtn = document.getElementById("wishlistBtn");
const cartDrawer = document.getElementById("cartDrawer");
const wishlistDrawer = document.getElementById("wishlistDrawer");
const cartItemsDiv = document.getElementById("cartItems");
const wishlistItemsDiv = document.getElementById("wishlistItems");
const cartCount = document.getElementById("cartCount");
const wishCount = document.getElementById("wishCount");
const subtotalEl = document.getElementById("subtotal");
const gstEl = document.getElementById("gst");
const deliveryEl = document.getElementById("delivery");
const discountEl = document.getElementById("discount");
const totalPriceEl = document.getElementById("totalPrice");
const toast = document.getElementById("toast");
const searchInput = document.getElementById("searchInput");


let cart = JSON.parse(localStorage.getItem("cart23")) || [];
let wishlist = JSON.parse(localStorage.getItem("wishlist23")) || [];
let discount = 0;
let currentCategory = "all";
let currentSort = "";


const products = [
{name:"Smartphone",price:9999,cat:"electronics",stock:5},
{name:"Headphones",price:1999,cat:"electronics",stock:10},
{name:"Smart Watch",price:2499,cat:"electronics",stock:0},
{name:"Keyboard",price:699,cat:"electronics",stock:6},
{name:"Mouse",price:499,cat:"electronics",stock:8},
{name:"Power Bank",price:1299,cat:"electronics",stock:4},
{name:"T-Shirt",price:499,cat:"fashion",stock:15},
{name:"Shoes",price:2199,cat:"fashion",stock:7},
{name:"Backpack",price:999,cat:"fashion",stock:3},
{name:"Handbag",price:1499,cat:"fashion",stock:2},
{name:"Desk Lamp",price:899,cat:"home",stock:9},
{name:"Office Chair",price:5499,cat:"home",stock:1},
{name:"Coffee Mug",price:199,cat:"home",stock:20},
{name:"Water Bottle",price:299,cat:"home",stock:12},
{name:"Bedsheet",price:1299,cat:"home",stock:0}
];

function randomRating(){ return (Math.random()*2+3).toFixed(1) }


function showToast(msg){
  toast.textContent = msg;
  toast.classList.add("show");
  setTimeout(()=>toast.classList.remove("show"),1500);
}


function createProducts(){
  let filtered = [...products];


  if(currentCategory !== "all"){
    filtered = filtered.filter(p => p.cat === currentCategory);
  }


  const q = searchInput.value.toLowerCase();
  filtered = filtered.filter(p => p.name.toLowerCase().includes(q));


  if(currentSort === "priceLow") filtered.sort((a,b)=>a.price-b.price);
  if(currentSort === "priceHigh") filtered.sort((a,b)=>b.price-a.price);
  if(currentSort === "rating") filtered.sort(()=>Math.random()-0.5);

  productList.innerHTML = "";

  filtered.forEach(p=>{
    const discountP = Math.floor(Math.random()*40)+10;
    const mrp = Math.floor(p.price*(1+discountP/100));

    productList.innerHTML += `
    <div class="card" data-name="${p.name}" data-price="${p.price}">
      <span class="badge">${discountP}% off</span>
      <img src="https://via.placeholder.com/200">
      <h3>${p.name}</h3>
      <div class="rating">⭐ ${randomRating()}</div>
      <div class="price">₹${p.price} <span class="mrp">₹${mrp}</span></div>
      <div class="free">${p.stock>0 ? "Free Delivery" : "Out of Stock"}</div>

      <div class="qtyBox">
        <button class="qtyMinus">-</button>
        <input type="number" value="1" min="1">
        <button class="qtyPlus">+</button>
      </div>

      <button class="addBtn" ${p.stock===0?"disabled":""}>Add to Cart</button>
      <button class="wishBtn">Wishlist</button>
    </div>`;
  });
}
createProducts();


document.addEventListener("click", e=>{


  if(e.target.classList.contains("qtyPlus")){
    const input = e.target.previousElementSibling;
    input.value = Number(input.value)+1;
  }


  if(e.target.classList.contains("qtyMinus")){
    const input = e.target.nextElementSibling;
    if(input.value > 1) input.value--;
  }


  if(e.target.classList.contains("addBtn")){
    const card = e.target.closest(".card");
    const name = card.dataset.name;
    const price = Number(card.dataset.price);
    const qty = Number(card.querySelector("input").value);

    const item = cart.find(i=>i.name===name);
    if(item) item.qty += qty;
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
  cartItemsDiv.innerHTML = "";

  if(cart.length===0){
    cartItemsDiv.innerHTML = "<p>Your cart is empty</p>";
  }

  let subtotal = 0;

  cart.forEach((item,i)=>{
    subtotal += item.price * item.qty;

    cartItemsDiv.innerHTML += `
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
  const delivery = subtotal>2000 ? 0 : 99;
  const total = subtotal + gst + delivery - discount;

  subtotalEl.textContent = subtotal;
  gstEl.textContent = gst;
  deliveryEl.textContent = delivery;
  discountEl.textContent = discount;
  totalPriceEl.textContent = total;
  cartCount.textContent = cart.reduce((a,b)=>a+b.qty,0);
}

function changeQty(i,d){
  cart[i].qty += d;
  if(cart[i].qty<=0) cart.splice(i,1);
  saveCart();
}
function removeItem(i){
  cart.splice(i,1);
  saveCart();
}
function saveCart(){
  localStorage.setItem("cart23",JSON.stringify(cart));
  updateCart();
}


function updateWishlist(){
  wishlistItemsDiv.innerHTML = "";

  if(wishlist.length===0){
    wishlistItemsDiv.innerHTML = "<p>Your wishlist is empty</p>";
  }

  wishlist.forEach((name,i)=>{
    wishlistItemsDiv.innerHTML += `
    <div class="cartRow">
      <span>${name}</span>
      <button onclick="moveToCart('${name}')">Move to Cart</button>
      <button onclick="removeWish(${i})">X</button>
    </div>`;
  });

  wishCount.textContent = wishlist.length;
}

function moveToCart(name){
  const product = products.find(p=>p.name===name);
  if(!product || product.stock===0){
    showToast("Out of stock");
    return;
  }

  const item = cart.find(i=>i.name===name);
  if(item) item.qty += 1;
  else cart.push({name,price:product.price,qty:1});

  saveCart();
  showToast("Moved to cart");
}

function removeWish(i){
  wishlist.splice(i,1);
  saveWishlist();
}
function saveWishlist(){
  localStorage.setItem("wishlist23",JSON.stringify(wishlist));
  updateWishlist();
}


cartBtn.onclick = ()=>{
  cartDrawer.classList.toggle("active");
  wishlistDrawer.classList.remove("active");
};

wishlistBtn.onclick = ()=>{
  wishlistDrawer.classList.toggle("active");
  cartDrawer.classList.remove("active");
};


document.addEventListener("click", e=>{
  if(!cartDrawer.contains(e.target) && !cartBtn.contains(e.target)){
    cartDrawer.classList.remove("active");
  }
  if(!wishlistDrawer.contains(e.target) && !wishlistBtn.contains(e.target)){
    wishlistDrawer.classList.remove("active");
  }
});


document.getElementById("applyCoupon").onclick = ()=>{
  const code = document.getElementById("couponInput").value;

  const subtotal = cart.reduce((a,b)=>a+b.price*b.qty,0);

  if(code==="SAVE10") discount = 10;
  else if(code==="SAVE20") discount = 20;
  else if(code==="BIG50" && subtotal>=1000) discount = 50;
  else discount = 0;

  updateCart();
};


searchInput.addEventListener("input",createProducts);


const darkToggle = document.getElementById("darkToggle");
if(localStorage.getItem("dark23")==="on") document.body.classList.add("dark");

darkToggle.onclick = ()=>{
  document.body.classList.toggle("dark");
  localStorage.setItem("dark23",
    document.body.classList.contains("dark") ? "on" : "off"
  );
};


updateCart();
updateWishlist();
