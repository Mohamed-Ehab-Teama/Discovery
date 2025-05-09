// Initialize product list
window.onload = displayProducts;

// Create: Add product to local storage
function addProduct() {
  let productName = document.getElementById("productName").value;
  if (productName) {
    let products = JSON.parse(localStorage.getItem("products")) || [];
    products.push(productName);
    localStorage.setItem("products", JSON.stringify(products));
    document.getElementById("productName").value = ""; // Clear input
    displayProducts();
  } else {
    alert("Please enter a product name!");
  }
}

// Display: Show all products in the list
function displayProducts() {
  let products = JSON.parse(localStorage.getItem("products")) || [];
  let productList = document.getElementById("productList");
  productList.innerHTML = ""; // Clear the list before re-rendering

  products.forEach((product, index) => {
    let li = document.createElement("li");
    li.textContent = `${index + 1}. ${product}`;
    productList.appendChild(li);
  });
}

// Clear all products from Local storage
function clearProducts() {
  localStorage.clear();
  displayProducts();
}
