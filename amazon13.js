const searchInput = document.getElementById("searchInput");
const cards = document.querySelectorAll(".card");
const sortSelect = document.getElementById("sortSelect");
const cartCount = document.getElementById("cartCount");
const cartBtn = document.getElementById("cartBtn");
const cartSidebar = document.getElementById("cartSidebar");
const cartItemsDiv = document.getElementById("cartItems");
const totalPriceEl = document.getElementById("totalPrice");
const darkToggle = document.getElementById("darkToggle");

const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modalTitle");
const modalPrice = document.getElementById("modalPrice");
const closeModal = document.getElementById("closeModal");

let cart = JSON.parse(localStorage.getItem("cart13")) || [];

updateCart();

searchInput.addEventListener("keyup", () => {
    const value = searchInput.value.toLowerCase();
    cards.forEach(card => {
        card.style.display = card.dataset.name.includes(value) ? "block" : "none";
    });
});

sortSelect.addEventListener("change", () => {
    const sorted = [...cards].sort((a,b) => {
        return sortSelect.value === "low"
            ? a.dataset.price - b.dataset.price
            : b.dataset.price - a.dataset.price;
    });
    const container = document.getElementById("productList");
    container.innerHTML = "";
    sorted.forEach(c => container.appendChild(c));
});

document.querySelectorAll(".filters button").forEach(btn => {
    btn.onclick = () => {
        const filter = btn.dataset.filter;
        cards.forEach(card => {
            card.style.display = filter === "all" || card.dataset.category === filter
                ? "block" : "none";
        });
    };
});

document.querySelectorAll(".addBtn").forEach(btn => {
    btn.onclick = e => {
        const card = e.target.closest(".card");
        const name = card.querySelector("h3").textContent;
        const price = Number(card.dataset.price);

        const item = cart.find(i => i.name === name);
        if (item) item.qty++;
        else cart.push({name, price, qty:1});

        saveCart();
    };
});

function updateCart(){
    cartItemsDiv.innerHTML = "";
    let total = 0;

    cart.forEach((item,i)=>{
        total += item.price * item.qty;
        cartItemsDiv.innerHTML += `
            <div>
                ${item.name} x${item.qty}
                <button onclick="removeItem(${i})">X</button>
            </div>
        `;
    });

    cartCount.textContent = cart.reduce((a,b)=>a+b.qty,0);
    totalPriceEl.textContent = total;
}

function removeItem(i){
    cart.splice(i,1);
    saveCart();
}

function saveCart(){
    localStorage.setItem("cart13", JSON.stringify(cart));
    updateCart();
}

cartBtn.onclick = ()=> cartSidebar.classList.toggle("active");

darkToggle.onclick = ()=> document.body.classList.toggle("dark");

document.querySelectorAll(".viewBtn").forEach(btn=>{
    btn.onclick = e=>{
        const card = e.target.closest(".card");
        modalTitle.textContent = card.querySelector("h3").textContent;
        modalPrice.textContent = "₹"+card.dataset.price;
        modal.style.display = "block";
    };
});

closeModal.onclick = ()=> modal.style.display="none";
window.onclick = e => { if(e.target==modal) modal.style.display="none"; };
