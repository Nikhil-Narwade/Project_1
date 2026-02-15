const products = [
  {name: "Smartphone", price: 9999, category: "electronics", img: "https://via.placeholder.com/200"},
  {name: "Laptop Bag", price: 799, category: "fashion", img: "https://via.placeholder.com/200"},
  {name: "Book", price: 499, category: "books", img: "https://via.placeholder.com/200"},
  {name: "Headphones", price: 1999, category: "electronics", img: "https://via.placeholder.com/200"}
];

let cart = JSON.parse(localStorage.getItem("cart17")) || [];

const productList = document.getElementById("productList");
const cartItems = document.getElementById("cartItems");
const cartCount = document.getElementById("cartCount");
const totalPrice = document.getElementById("totalPrice");

function displayProducts(data) {
  productList.innerHTML = "";
  data.forEach(p => {
    productList.innerHTML += `
      <div class="card">
        <img src="${p.img}">
        <h3>${p.name}</h3>
        <p>₹${p.price}</p>
        <button onclick='addToCart(${JSON.stringify(p)})'>Add to Cart</button>
      </div>
    `;
  });
}

displayProducts(products);

function addToCart(product) {
  const item = cart.find(i => i.name === product.name);
  if (item) item.qty++;
  else cart.push({...product, qty: 1});

  saveCart();
}

function saveCart() {
  localStorage.setItem("cart17", JSON.stringify(cart));
  updateCart();
}

function updateCart() {
  cartItems.innerHTML = "";
  let total = 0;
  let count = 0;

  cart.forEach((item, index) => {
    total += item.price * item.qty;
    count += item.qty;

    cartItems.innerHTML += `
      <li>
        ${item.name} x${item.qty}
        <button onclick="changeQty(${index},1)">+</button>
        <button onclick="changeQty(${index},-1)">-</button>
        <button onclick="removeItem(${index})">❌</button>
      </li>
    `;
  });

  cartCount.textContent = count;
  totalPrice.textContent = total;
}

function changeQty(index, val) {
  cart[index].qty += val;
  if (cart[index].qty <= 0) cart.splice(index, 1);
  saveCart();
}

function removeItem(index) {
  cart.splice(index, 1);
  saveCart();
}

document.getElementById("cartBtn").onclick = () => {
  document.getElementById("cartSidebar").classList.add("open");
};

function closeCart() {
  document.getElementById("cartSidebar").classList.remove("open");
}

document.getElementById("searchBox").addEventListener("input", e => {
  const value = e.target.value.toLowerCase();
  displayProducts(products.filter(p => p.name.toLowerCase().includes(value)));
});

document.getElementById("categoryFilter").addEventListener("change", e => {
  const value = e.target.value;
  if (value === "all") displayProducts(products);
  else displayProducts(products.filter(p => p.category === value));
});

document.getElementById("sortPrice").addEventListener("change", e => {
  const sorted = [...products];
  if (e.target.value === "low") sorted.sort((a,b)=>a.price-b.price);
  if (e.target.value === "high") sorted.sort((a,b)=>b.price-a.price);
  displayProducts(sorted);
});

document.getElementById("darkToggle").onclick = () => {
  document.body.classList.toggle("dark");
};

updateCart();
