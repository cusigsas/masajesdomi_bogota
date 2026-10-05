/* =========================================================
   Thera+Vida — main.js
   WhatsApp, header, menú, contadores y año dinámico.
   ========================================================= */
const WHATSAPP_NUMBER = "573170121268";
const DEFAULT_WA_MSG = "Hola Thera+Vida, quiero agendar una cita a domicilio en Bogotá.";

/* Cada enlace con data-wa abre WhatsApp.
   Mensaje: el del propio enlace (data-wa="...") o el de la página (body data-wa-msg). */
function initWhatsApp() {
  const pageMsg = document.body.dataset.waMsg || DEFAULT_WA_MSG;
  document.querySelectorAll("[data-wa]").forEach((link) => {
    if (link.dataset.waReady) return;
    const msg = link.dataset.wa || pageMsg;
    link.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
    link.target = "_blank";
    link.rel = "noopener";
    link.dataset.waReady = "1";
    link.addEventListener("click", () => {
      const label = document.title;
      if (typeof gtag === "function") gtag("event", "click_whatsapp", { pagina: label });
      if (typeof fbq === "function") fbq("track", "Contact", { pagina: label });
    });
  });
}

/* Año actual en cualquier elemento con data-year */
function initYear() {
  const y = new Date().getFullYear();
  document.querySelectorAll("[data-year]").forEach((el) => { el.textContent = y; });
}

/* Header transparente → blanco */
function initHeader() {
  const header = document.getElementById("masthead");
  if (!header) return;
  const toggle = header.querySelector(".menu-toggle");
  const nav = header.querySelector(".main-nav");
  const update = () => {
    const open = toggle && toggle.getAttribute("aria-expanded") === "true";
    header.classList.toggle("is-scrolled", window.scrollY > 20 || open);
  };
  update();
  window.addEventListener("scroll", update, { passive: true });

  // Menú móvil
  if (toggle && nav) {
    const label = toggle.querySelector(".visually-hidden");
    const setOpen = (open) => {
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
      if (label) label.textContent = open ? "Cerrar menú" : "Abrir menú";
      update();
    };
    toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"));
    nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
  }

  // Submenú de servicios
  header.querySelectorAll(".has-sub").forEach((item) => {
    const btn = item.querySelector(".sub-toggle");
    const menu = item.querySelector(".sub-menu");
    const setSub = (open) => {
      btn.setAttribute("aria-expanded", String(open));
      menu.classList.toggle("is-open", open);
    };
    btn.addEventListener("click", () => setSub(btn.getAttribute("aria-expanded") !== "true"));
    const desktop = window.matchMedia("(min-width: 901px)");
    item.addEventListener("mouseenter", () => { if (desktop.matches) setSub(true); });
    item.addEventListener("mouseleave", () => { if (desktop.matches) setSub(false); });
    document.addEventListener("click", (e) => { if (!item.contains(e.target)) setSub(false); });
    item.addEventListener("keydown", (e) => { if (e.key === "Escape") { setSub(false); btn.focus(); } });
  });

  // Marca la página actual en el menú
  const here = location.pathname.split("/").pop() || "index.html";
  header.querySelectorAll(".main-nav a[href]").forEach((a) => {
    if (a.getAttribute("href").split("/").pop() === here) a.setAttribute("aria-current", "page");
  });
}

/* Contadores animados */
function initCounters() {
  const counters = document.querySelectorAll(".counter-number[data-end]");
  if (!counters.length) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const show = (el) => { el.textContent = el.dataset.end + (el.dataset.suffix || ""); };
  const run = (el) => {
    if (reduce) return show(el);
    const end = Number(el.dataset.end) || 0;
    const suffix = el.dataset.suffix || "";
    const start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / 2200, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (!("IntersectionObserver" in window)) return counters.forEach(show);
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } });
  }, { threshold: 0.6 });
  counters.forEach((c) => io.observe(c));
}

/* Lo que no depende de los componentes */
initCounters();
initWhatsApp();
initYear();

/* Lo que vive dentro de los componentes */
const afterComponents = () => { initHeader(); initWhatsApp(); initYear(); };
if (window.__componentsLoaded) afterComponents();
else document.addEventListener("components:loaded", afterComponents);
