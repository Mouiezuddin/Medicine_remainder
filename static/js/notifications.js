const alertedReminders = new Set();

function requestNotifPermission() {
  if ('Notification' in window && Notification.permission === 'default') {
    Notification.requestPermission();
  }
}

function checkReminders() {
  const now = new Date();
  const hh = String(now.getHours()).padStart(2, '0');
  const mm = String(now.getMinutes()).padStart(2, '0');
  const currentTime = `${hh}:${mm}`;

  document.querySelectorAll('[data-reminder-time]').forEach(el => {
    const remTime = el.dataset.reminderTime;
    const remId = el.dataset.reminderId;
    const medName = el.dataset.medicineName;

    if (remTime === currentTime && !alertedReminders.has(`${remId}-${currentTime}`)) {
      alertedReminders.add(`${remId}-${currentTime}`);
      showNotification(medName);
      flashCard(el);
    }
  });
}

function showNotification(medicineName) {
  if ('Notification' in window && Notification.permission === 'granted') {
    new Notification('💊 Medicine Reminder', {
      body: `Time to take ${medicineName}`,
      icon: '/static/images/pill-icon.png',
      badge: '/static/images/pill-icon.png',
      tag: medicineName,
      requireInteraction: true,
    });
  } else {
    showToast(`💊 Time to take ${medicineName}`);
  }
}

function flashCard(el) {
  const card = el.closest('.reminder-card');
  if (card) {
    card.style.transition = 'box-shadow 0.3s, transform 0.3s';
    card.style.boxShadow = '0 0 40px rgba(99,102,241,0.8), 0 0 80px rgba(99,102,241,0.4)';
    card.style.transform = 'translateY(-8px) scale(1.03)';
    setTimeout(() => {
      card.style.boxShadow = '';
      card.style.transform = '';
    }, 3000);
  }
}

function showToast(msg) {
  const container = document.getElementById('msg-container');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'msg msg-info';
  toast.textContent = msg;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 5000);
}

function toggleNotifPanel() {
  const panel = document.getElementById('notif-panel');
  if (panel) {
    panel.classList.toggle('active');
  }
}

// Auto-dismiss messages
document.addEventListener('DOMContentLoaded', () => {
  requestNotifPermission();

  // Close notif panel when clicking outside
  document.addEventListener('click', (e) => {
    const panel = document.getElementById('notif-panel');
    const btn = document.querySelector('.notif-btn');
    if (panel && panel.classList.contains('active') && !panel.contains(e.target) && !btn.contains(e.target)) {
      panel.classList.remove('active');
    }
  });
  setInterval(checkReminders, 60000);
  checkReminders(); // immediate check

  // Auto hide flash messages after 4s
  document.querySelectorAll('.msg').forEach(msg => {
    setTimeout(() => {
      msg.style.transition = 'opacity 0.5s';
      msg.style.opacity = '0';
      setTimeout(() => msg.remove(), 500);
    }, 4000);
  });

  // 3D tilt effect on cards
  document.querySelectorAll('.glass-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(1000px) rotateX(${-y * 8}deg) rotateY(${x * 8}deg) translateY(-6px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
});
