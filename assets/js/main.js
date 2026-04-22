(() => {
  const filterButtons = document.querySelectorAll(".filter");
  const cards = document.querySelectorAll("#portfolio-grid .project-card");

  if (filterButtons.length && cards.length) {
    filterButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const filter = button.dataset.filter || "all";
        filterButtons.forEach((item) => item.classList.remove("active"));
        button.classList.add("active");

        cards.forEach((card) => {
          const tags = card.dataset.tags || "";
          const show = filter === "all" || tags.includes(filter);
          card.classList.toggle("hide-card", !show);
        });
      });
    });
  }

  const form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const name = form.elements.name.value.trim();
      const email = form.elements.email.value.trim();
      const message = form.elements.message.value.trim();
      const text = [
        "Ola, Carlos!",
        "Nome: " + name,
        "Email: " + email,
        "Mensagem: " + message
      ].join("\n");
      window.open("https://wa.me/5511986395283?text=" + encodeURIComponent(text), "_blank");
    });
  }
})();
