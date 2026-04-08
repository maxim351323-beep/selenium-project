// Tech_world — script.js
// All validations and requirements for working with the site

const VALID_USER = "admin";
const VALID_PASS = "@Dm1n";

document.addEventListener("DOMContentLoaded", function () {

  // ── LOGIN ────────────────────────────────────────────────────────────
  const loginBtn   = document.getElementById("login-btn");
  const loginError = document.getElementById("login-error");

  loginBtn.addEventListener("click", function () {
    const u = document.getElementById("username").value.trim();
    const p = document.getElementById("password").value;

    if (!u || !p) {
      loginError.textContent = "Please fill in both fields.";
      return;
    }
    if (u !== VALID_USER || p !== VALID_PASS) {
      loginError.textContent = "Invalid username or password.";
      return;
    }
    loginError.textContent = "";
    document.getElementById("login-screen").style.display = "none";
    document.getElementById("app-screen").style.display   = "block";
  });

  // Also allow Enter key on password field
  document.getElementById("password").addEventListener("keydown", function (e) {
    if (e.key === "Enter") loginBtn.click();
  });

  // ── TABS ─────────────────────────────────────────────────────────────
  const tabLinks  = document.querySelectorAll(".tab-link");
  const tabPanels = document.querySelectorAll(".tab-panel");

  tabLinks.forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = link.getAttribute("href").replace("#", "");

      tabLinks.forEach(function (l)  { l.classList.remove("active"); });
      tabPanels.forEach(function (p) { p.classList.remove("active"); });

      link.classList.add("active");
      document.getElementById(targetId).classList.add("active");
    });
  });

  // ── CONTACT FORM — SEND MESSAGE ──────────────────────────────────────
  document.getElementById("send-btn").addEventListener("click", function () {
    const name  = document.getElementById("contact-name").value.trim();
    const email = document.getElementById("contact-email").value.trim();
    const pwd   = document.getElementById("contact-password").value;
    const msg   = document.getElementById("send-message");

    if (!name || !email || !pwd) {
      msg.style.color = "#c0392b";
      msg.textContent = "Please fill in all fields.";
      return;
    }
    if (!email.includes("@")) {
      msg.style.color = "#c0392b";
      msg.textContent = "Please enter a valid email address.";
      return;
    }

    msg.style.color = "#2e7d32";
    msg.textContent = "Message sent successfully!";

    // Reset form after 3 seconds
    setTimeout(function () {
      document.getElementById("contact-name").value     = "";
      document.getElementById("contact-email").value    = "";
      document.getElementById("contact-password").value = "";
      msg.textContent = "";
    }, 3000);
  });

  // ── LOGOUT ────────────────────────────────────────────────────────────
  document.getElementById("logout-btn").addEventListener("click", function () {
    document.getElementById("app-screen").style.display   = "none";
    document.getElementById("login-screen").style.display = "flex";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("login-error").textContent = "";
  });

});
