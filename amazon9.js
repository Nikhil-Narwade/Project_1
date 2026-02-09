const searchInput = document.getElementById("searchInput");
const cards = document.querySelectorAll(".card");
const cartCount = document.getElementById("cartCount");
const cartDiv = document.querySelector(".cart");
const cartDropdown = document.getElementById("cartDropdown");

let cart = [];
searchInput.addEventListener("keyup", function () {
    const value = searchInput.value.toLowerCase().trim();
    cards.forEach(card => {
        const name = card.getAttribute("data-name").toLowerCase();
        if (name.includes(value)) card.style.display = "block";
        else card.style.display = "none";
    });
});

document.querySelectorAll(".menu a").forEach(link => {
    link.addEventListener("click", function(e){
        e.preventDefault();
        const filter = this.getAttribute("data-filter");
        cards.forEach(card => {
            const category = card.getAttribute("data-category");
            if (filter === "all" || category === filter) card.style.display = "block";
            else card.style.display = "none";
        });
    });
});

cards.forEach(card => {
    const btn = card.querySelector("button");
    btn.addEventListener("click", () => {
        const name = card.querySelector("h3").textContent;
        const price = card.getAttribute("data-price");
        cart.push({name, price});
        cartCount.textContent = cart.length;
        updateCartDropdown();
    });
});

cartDiv.addEventListener("click", () => {
    cartDropdown.style.display = cartDropdown.style.display === "block" ? "none" : "block";
});

function updateCartDropdown(){
    if(cart.length === 0){
        cartDropdown.innerHTML = "<p>Cart is empty</p>";
        return;
    }
    let html = "<h4>Your Cart</h4>";
    cart.forEach((item, index) => {
        html += `<div class="cart-item">${item.name} - ₹${item.price} <button onclick="removeItem(${index})">x</button></div>`;
    });
    cartDropdown.innerHTML = html;
}

function removeItem(index){
    cart.splice(index, 1);
    cartCount.textContent = cart.length;
    updateCartDropdown();
}
