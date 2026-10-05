/* =========================================================
   Thera+Vida — script
   ========================================================= */

/* ---------- Configuración de WhatsApp ----------
   Número en formato internacional, sin "+" ni espacios.
   Cada botón tiene su propio mensaje para saber desde qué
   sección escribió la persona. */
const WHATSAPP_NUMBER = "573170121268";

const WHATSAPP_MESSAGES = {
  header:          "Hola Thera+Vida, quiero agendar una cita a domicilio.",
  hero:            "Hola Thera+Vida, quiero información sobre sus servicios a domicilio en Bogotá.",
  enfermeria:      "Hola Thera+Vida, quiero información sobre los servicios de enfermería a domicilio.",
  terapia:         "Hola Thera+Vida, quiero información sobre las terapias y drenajes a domicilio.",
  "como-funciona": "Hola Thera+Vida, quiero agendar una visita. ¿Qué datos necesitan?",
  contacto:        "Hola Thera+Vida, quiero agendar una cita a domicilio."
};

document.querySelectorAll("[data-wa]").forEach((link) => {
  const key = link.dataset.wa;
  const message = WHATSAPP_MESSAGES[key] || WHATSAPP_MESSAGES.header;
  link.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

  // Evento para Analytics / Meta Pixel (si están activos)
  link.addEventListener("click", () => {
    if (typeof gtag === "function") {
      gtag("event", "click_whatsapp", { boton: key });
    }
    if (typeof fbq === "function") {
      fbq("track", "Contact", { boton: key });
    }
  });
});

/* ---------- Header: transparente → blanco al hacer scroll ---------- */
const header = document.getElementById("masthead");
const updateHeader = () => {
  header.classList.toggle("is-scrolled", window.scrollY > 20);
};
updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });

/* ---------- Menú móvil ---------- */
const toggle = document.querySelector(".menu-toggle");
const nav = document.getElementById("menu-principal");

const closeMenu = () => {
  toggle.setAttribute("aria-expanded", "false");
  toggle.querySelector(".visually-hidden").textContent = "Abrir menú";
  nav.classList.remove("is-open");
  updateHeader();
};

toggle.addEventListener("click", () => {
  const open = toggle.getAttribute("aria-expanded") === "true";
  if (open) {
    closeMenu();
  } else {
    toggle.setAttribute("aria-expanded", "true");
    toggle.querySelector(".visually-hidden").textContent = "Cerrar menú";
    nav.classList.add("is-open");
    header.classList.add("is-scrolled");
  }
});

nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", closeMenu));
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeMenu();
});

/* ---------- Contadores animados ---------- */
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const runCounter = (el) => {
  const end = Number(el.dataset.end) || 0;
  const suffix = el.dataset.suffix || "";
  const duration = 2200;

  if (reduceMotion) {
    el.textContent = end + suffix;
    return;
  }

  const start = performance.now();
  const step = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.round(end * eased) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
};

const counters = document.querySelectorAll(".counter-number");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        runCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.6 });
  counters.forEach((c) => observer.observe(c));
} else {
  counters.forEach((c) => {
    c.textContent = c.dataset.end + (c.dataset.suffix || "");
  });
}

/* ---------- Año del footer ---------- */
document.getElementById("year").textContent = new Date().getFullYear();
