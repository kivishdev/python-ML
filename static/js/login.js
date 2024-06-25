const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();  // Prevent default form submission

  const username = form.username.value;
  const password = form.password.value;

  // Replace with your actual username and password for successful login
  const validUsername = "ABCDEF";
  const validPassword = "123456";

  if (username === validUsername && password === validPassword) {
    alert("Login successful!");
    window.location.href = "/prediction form";  // Redirect on successful login
  } else {
    alert("Login failed. Please try again.");
  }
});


function submitFormAndRedirect() {
  // ... (your validation logic)
  alert("Login successful!");
  setTimeout(() => {
    window.location.href = "/prediction_form";
  }, 1000); // Redirect after 1 second delay (adjust as needed)
}



