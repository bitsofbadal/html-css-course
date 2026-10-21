
const heart = document.getElementById("heart");
const wish = document.getElementById("wish");
const replay = document.getElementById("replay");

function openGift() {
  wish.classList.add("show");
  heart.textContent = "💖";

  // Create floating hearts
  for (let i = 0; i < 16; i++) {
    const particle = document.createElement("span");

    particle.textContent = ["💗", "💕", "✨", "💖"][
      Math.floor(Math.random() * 4)
    ];

    particle.style.position = "fixed";
    particle.style.left = Math.random() * 90 + 5 + "%";
    particle.style.bottom = "-30px";
    particle.style.fontSize = 20 + Math.random() * 18 + "px";
    particle.style.pointerEvents = "none";
    particle.style.zIndex = "10";

    document.body.appendChild(particle);

    const animation = particle.animate(
      [
        { transform: "translateY(0) rotate(0deg)", opacity: 1 },
        {
          transform: `translateY(-${window.innerHeight + 100}px) rotate(240deg)`,
          opacity: 0
        }
      ],
      {
        duration: 2500 + Math.random() * 2000,
        easing: "ease-out"
      }
    );

    animation.onfinish = () => particle.remove();
  }
}

heart.addEventListener("click", openGift);

replay.addEventListener("click", () => {
  wish.classList.remove("show");
  heart.textContent = "💗";
  openGift();
});