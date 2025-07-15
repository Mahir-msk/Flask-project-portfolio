// Typing Effect
function initTypingText() {
  const texts = [
    "AI Engineer.",
    "Machine Learning Enthusiast.",
    "Open Source Contributor.",
    "Lifelong Learner."
  ];
  const typingText = document.getElementById("typingText");
  let index = 0;
  let charIndex = 0;
  let isDeleting = false;

  function type() {
    const current = texts[index];
    if (isDeleting) {
      charIndex--;
    } else {
      charIndex++;
    }

    typingText.textContent = current.substring(0, charIndex);

    if (!isDeleting && charIndex === current.length) {
      setTimeout(() => isDeleting = true, 1500);
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      index = (index + 1) % texts.length;
    }

    const delay = isDeleting ? 50 : 100;
    setTimeout(type, delay);
  }

  type();
}

// Load Tech News
function loadTechNews(newsData) {
  const container = document.getElementById('newsContainer');
  if (!container) return;

  container.innerHTML = '';

  newsData.forEach(news => {
    const card = document.createElement('div');
    card.className = 'news-card animate-on-scroll';
    card.innerHTML = `
      <h3 class="news-title">${news.title}</h3>
      <p class="news-meta">📰 ${news.source} | 📅 ${news.date}</p>
      <a href="${news.link}" class="btn btn-secondary" target="_blank">Read More</a>
    `;
    container.appendChild(card);
  });
}

// Load Blogs
function initBlogCards() {
  const container = document.getElementById('blogsContainer');
  if (!container) return;

  fetch('/api/blogs')
    .then(res => res.json())
    .then(blogs => {
      container.innerHTML = '';
      blogs.forEach(blog => {
        const card = document.createElement('div');
        card.className = 'blog-card animate-on-scroll';
        card.innerHTML = `
          <h3 class="blog-title">${blog.title}</h3>
          <p class="blog-desc">${blog.description}</p>
          <p class="blog-date">${new Date(blog.date).toDateString()}</p>
          <a href="${blog.link}" class="btn btn-outline" target="_blank">Read More</a>
        `;
        container.appendChild(card);
      });
    })
    .catch(err => console.error('Error loading blogs:', err));
}

// Scroll Reveal Animation
function initScrollAnimations() {
  const animatedElems = document.querySelectorAll('.animate-on-scroll');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  animatedElems.forEach(el => observer.observe(el));
}

// Theme Toggle
function initThemeToggle() {
  const toggle = document.getElementById('themeToggle');
  if (!toggle) return;

  toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
  });
}

// Init Tech News
function initTechNews() {
  fetch('/api/tech-news')
    .then(res => res.json())
    .then(data => loadTechNews(data))
    .catch(err => console.error("Error loading news:", err));
}

// Initialize All Animations
function initAllAnimations() {
  initTypingText();
  initScrollAnimations();
  initBlogCards();
  initTechNews();
  initThemeToggle();
}

// Run on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  initAllAnimations();
});
document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
      name: contactForm.name.value,
      email: contactForm.email.value,
      message: contactForm.message.value
    };

    try {
      const res = await fetch('/contact/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      const result = await res.json();
      if (result.success) {
        contactForm.reset();
        formSuccess.classList.add('active');
        setTimeout(() => formSuccess.classList.remove('active'), 3000);
      } else {
        alert('Message not sent. Try again.');
      }
    } catch (err) {
      alert('Something went wrong.');
      console.error(err);
    }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const formData = new FormData(contactForm);

      fetch('/contact/submit', {
        method: 'POST',
        body: formData
      })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            formSuccess.style.display = 'block';
            contactForm.reset();
            setTimeout(() => {
              formSuccess.style.display = 'none';
            }, 3000);
          } else {
            alert("Error: " + data.error || "Form submission failed.");
          }
        })
        .catch(err => {
          console.error('Error submitting form:', err);
          alert("Something went wrong!");
        });
    });
  }
});
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 30) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});
