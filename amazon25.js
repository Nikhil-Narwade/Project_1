
let cart = JSON.parse(localStorage.getItem("cart")) || [];
let wishlist = JSON.parse(localStorage.getItem("wishlist")) || [];


function saveState() {
  localStorage.setItem("cart", JSON.stringify(cart));
  localStorage.setItem("wishlist", JSON.stringify(wishlist));
}


function showToast(msg) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerText = msg;
  document.body.appendChild(toast);

  setTimeout(() => toast.classList.add("show"), 100);
  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => toast.remove(), 300);
  }, 2000);
}

function updateCartCount() {
  const count = cart.reduce((acc, item) => acc + item.qty, 0);
  document.getElementById("cart-count").innerText = count;
}

function addToCart(id, name, price, image) {
  const item = cart.find(p => p.id === id);

  if (item) {
    item.qty++;
  } else {
    cart.push({ id, name, price, image, qty: 1 });
  }

  saveState();
  updateCartUI();
  updateCartCount();
  showToast("Added to Cart");
}

function removeFromCart(id) {
  cart = cart.filter(item => item.id !== id);
  saveState();
  updateCartUI();
  updateCartCount();
}

function changeQty(id, delta) {
  const item = cart.find(p => p.id === id);
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {
    removeFromCart(id);
  }

  saveState();
  updateCartUI();
  updateCartCount();
}

function addToWishlist(id, name, price, image) {
  if (!wishlist.find(p => p.id === id)) {
    wishlist.push({ id, name, price, image });
    saveState();
    updateWishlistUI();
    showToast("Added to Wishlist");
  }
}

function removeFromWishlist(id) {
  wishlist = wishlist.filter(item => item.id !== id);
  saveState();
  updateWishlistUI();
}

function moveToCartFromWishlist(id) {
  const item = wishlist.find(p => p.id === id);
  if (!item) return;

  addToCart(item.id, item.name, item.price, item.image);
  removeFromWishlist(id);
}

function updateCartUI() {
  const cartContainer = document.getElementById("cart-items");
  const totalContainer = document.getElementById("cart-total");

  if (!cartContainer) return;

  cartContainer.innerHTML = "";

  if (cart.length === 0) {
    cartContainer.innerHTML = "<p>Your cart is empty</p>";
    totalContainer.innerText = "₹0";
    return;
  }

  let total = 0;

  cart.forEach(item => {
    total += item.price * item.qty;

    cartContainer.innerHTML += `
      <div class="cart-item">
        <img src="${item.image}" />
        <div>
          <h4>${item.name}</h4>
          <p>₹${item.price}</p>
          <div class="qty-controls">
            <button onclick="changeQty(${item.id}, -1)">-</button>
            <span>${item.qty}</span>
            <button onclick="changeQty(${item.id}, 1)">+</button>
          </div>
          <button onclick="removeFromCart(${item.id})">Remove</button>
        </div>
      </div>
    `;
  });

  totalContainer.innerText = `₹${total}`;
}

function updateWishlistUI() {
  const container = document.getElementById("wishlist-items");

  if (!container) return;

  container.innerHTML = "";

  if (wishlist.length === 0) {
    container.innerHTML = "<p>Your wishlist is empty</p>";
    return;
  }

  wishlist.forEach(item => {
    container.innerHTML += `
      <div class="wishlist-item">
        <img src="${item.image}" />
        <div>
          <h4>${item.name}</h4>
          <p>₹${item.price}</p>
          <button onclick="moveToCartFromWishlist(${item.id})">
            Move to Cart
          </button>
          <button onclick="removeFromWishlist(${item.id})">
            Remove
          </button>
        </div>
      </div>
    `;
  });
}

function searchProducts() {
  const input = document.getElementById("search-input").value.toLowerCase();
  const products = document.querySelectorAll(".product");

  products.forEach(product => {
    const name = product
      .querySelector(".product-title")
      .innerText.toLowerCase();

    product.style.display = name.includes(input) ? "block" : "none";
  });
}

function sortProducts(order) {
  const container = document.getElementById("products");
  const items = Array.from(container.getElementsByClassName("product"));

  items.sort((a, b) => {
    const priceA = parseInt(a.dataset.price);
    const priceB = parseInt(b.dataset.price);

    return order === "low" ? priceA - priceB : priceB - priceA;
  });

  container.innerHTML = "";
  items.forEach(item => container.appendChild(item));
}

document.addEventListener("DOMContentLoaded", () => {
  updateCartCount();
  updateCartUI();
  updateWishlistUI();
});
