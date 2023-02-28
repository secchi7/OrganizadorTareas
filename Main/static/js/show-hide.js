const password = document.querySelector("#pass");
let i = document.getElementById("togglePassword");

togglePassword.addEventListener("click", function () {
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);

    if (i.classList.value == "bi bi-eye-fill") {
        i.classList="bi bi-eye-slash-fill"
    } else {
        i.classList="bi bi-eye-fill"
    };
})