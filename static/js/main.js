// STEP 1: Motion is the vanilla build of Framer Motion, so no React is needed.
// STEP 1.1: The global is provided by the CDN script in base.html.
const Motion = window.Motion;

if (Motion) {
  const { animate, inView } = Motion;
  const stagger = Motion.stagger || ((step) => (index) => index * step);
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const luxeEase = [0.16, 1, 0.3, 1];

  // STEP 2: With reduced motion, show everything immediately and skip movement.
  if (reduced) {
    document.querySelectorAll("[data-animate='hero'], [data-reveal]").forEach((node) => {
      node.style.opacity = "1";
      node.style.transform = "none";
    });
  } else {
    // STEP 3: Introduce the hero in a soft staggered cascade.
    const heroBits = document.querySelectorAll("[data-animate='hero']");
    if (heroBits.length) {
      animate(
        heroBits,
        { opacity: [0, 1], y: [28, 0], filter: ["blur(8px)", "blur(0px)"] },
        {
          duration: 0.95,
          delay: stagger(0.075, { start: 0.08 }),
          ease: luxeEase,
        }
      );
    }

    // STEP 4: Reveal grouped content as each group scrolls into view.
    document.querySelectorAll("[data-reveal-group]").forEach((group) => {
      const items = group.querySelectorAll("[data-reveal]");
      const targets = items.length ? items : [group];
      inView(
        group,
        () => {
          animate(
            targets,
            { opacity: [0, 1], y: [30, 0] },
            { duration: 0.8, delay: stagger(0.065), ease: luxeEase }
          );
        },
        { amount: 0.16 }
      );
    });

    // STEP 5: Count hero proof numbers up when they first appear.
    document.querySelectorAll("[data-count]").forEach((node) => {
      const target = Number(node.dataset.count);
      if (!Number.isFinite(target)) return;
      inView(
        node,
        () => {
          animate(0, target, {
            duration: 1.5,
            ease: luxeEase,
            onUpdate(value) {
              node.textContent = String(Math.round(value));
            },
          });
        },
        { amount: 0.7 }
      );
    });

    // STEP 6: Give the hero preview a gentle pointer-driven parallax.
    const hero = document.querySelector("[data-parallax]");
    if (hero) {
      const depthNodes = hero.querySelectorAll("[data-depth]");
      hero.addEventListener("pointermove", (event) => {
        const rect = hero.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        depthNodes.forEach((node) => {
          const depth = Number(node.dataset.depth) || 0;
          animate(node, { x: x * depth, y: y * depth }, { duration: 0.5, ease: "easeOut" });
        });
      });
      hero.addEventListener("pointerleave", () => {
        depthNodes.forEach((node) => {
          animate(node, { x: 0, y: 0 }, { duration: 0.7, ease: luxeEase });
        });
      });
    }

    // STEP 7: Add a subtle 3D tilt to interactive cards.
    document.querySelectorAll("[data-tilt]").forEach((card) => {
      card.addEventListener("pointermove", (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        animate(card, {
          rotateX: -y * 7,
          rotateY: x * 9,
          transformPerspective: 900,
        }, { duration: 0.45, ease: "easeOut" });
      });
      card.addEventListener("pointerleave", () => {
        animate(card, { rotateX: 0, rotateY: 0 }, { duration: 0.65, ease: luxeEase });
      });
    });

    // STEP 8: Make primary buttons feel magnetic without breaking layout.
    document.querySelectorAll("[data-magnetic]").forEach((button) => {
      button.addEventListener("pointermove", (event) => {
        const rect = button.getBoundingClientRect();
        const dx = event.clientX - (rect.left + rect.width / 2);
        const dy = event.clientY - (rect.top + rect.height / 2);
        animate(button, { x: dx * 0.16, y: dy * 0.16 }, { duration: 0.35, ease: "easeOut" });
      });
      button.addEventListener("pointerleave", () => {
        animate(button, { x: 0, y: 0 }, { duration: 0.55, ease: luxeEase });
      });
    });
  }

  // STEP 9: Deepen the sticky header shadow once the page is scrolled.
  const header = document.querySelector(".site-header");
  if (header && animate) {
    const updateShadow = () => {
      const lifted = window.scrollY > 8;
      animate(header, {
        boxShadow: lifted
          ? "0 16px 40px rgba(23, 23, 23, 0.08)"
          : "0 0 0 rgba(23, 23, 23, 0)",
      }, { duration: 0.25 });
    };
    window.addEventListener("scroll", updateShadow, { passive: true });
    updateShadow();
  }
}
