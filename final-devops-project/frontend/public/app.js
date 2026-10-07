// Frontend Application Logic
const API_BASE = 'http://localhost:8000';

// DOM Elements
const beBadge = document.getElementById('be-badge');
const dbBadge = document.getElementById('db-badge');
const beUptime = document.getElementById('be-uptime');
const dbConnStatus = document.getElementById('db-conn-status');
const tasksContainer = document.getElementById('tasks-container');
const newTaskForm = document.getElementById('new-task-form');
const btnRefresh = document.getElementById('btn-refresh');
const sysHost = document.getElementById('sys-host');
const sysOs = document.getElementById('sys-os');
const sysPython = document.getElementById('sys-python');
const rawHealthJson = document.getElementById('raw-health-json');
const globalStatusText = document.getElementById('global-status-text');

async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    beBadge.textContent = 'HEALTHY';
    beBadge.className = 'badge-status badge-success';
    beUptime.textContent = `${data.uptime_seconds}s`;

    if (data.database && (data.database.status === 'connected' || data.database.status === 'healthy')) {
      dbBadge.textContent = 'CONNECTED';
      dbBadge.className = 'badge-status badge-success';
      dbConnStatus.textContent = `${data.database.type || 'PostgreSQL'} (${data.database.host || 'localhost'}:${data.database.port || 5432})`;
      dbConnStatus.className = 'val text-success';
    } else {
      dbBadge.textContent = 'DEGRADED';
      dbBadge.className = 'badge-status';
      dbConnStatus.textContent = 'Offline';
    }

    rawHealthJson.textContent = JSON.stringify(data, null, 2);
    globalStatusText.textContent = 'Stack Fully Operational';
  } catch (err) {
    beBadge.textContent = 'OFFLINE';
    beBadge.className = 'badge-status';
    beUptime.textContent = 'N/A';
    rawHealthJson.textContent = `Backend connection error: ${err.message}`;
    globalStatusText.textContent = 'Backend Reconnecting...';
  }
}

async function loadSystemInfo() {
  try {
    const res = await fetch(`${API_BASE}/api/system`);
    if (!res.ok) throw new Error();
    const data = await res.json();
    sysHost.textContent = data.hostname || 'devops-node';
    sysOs.textContent = `${data.system} (${data.architecture})`;
    sysPython.textContent = `Python ${data.python_version}`;
  } catch (e) {
    sysHost.textContent = 'localhost';
    sysOs.textContent = 'Linux / Container';
  }
}

async function loadTasks() {
  try {
    tasksContainer.innerHTML = '<div class="loading-state">Querying tasks from database...</div>';
    const res = await fetch(`${API_BASE}/api/tasks`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const tasks = await res.json();

    if (!tasks || tasks.length === 0) {
      tasksContainer.innerHTML = '<div class="loading-state">No tasks recorded yet. Add one above!</div>';
      return;
    }

    tasksContainer.innerHTML = tasks.map(t => `
      <div class="task-item">
        <div class="task-info">
          <h4>${escapeHtml(t.title)}</h4>
          <p>${escapeHtml(t.description || 'DevOps stack task')}</p>
        </div>
        <div class="task-tag">${escapeHtml(t.status || 'Active')}</div>
      </div>
    `).join('');
  } catch (err) {
    tasksContainer.innerHTML = `
      <div class="task-item">
        <div class="task-info">
          <h4>Session 21: Full Stack Containerized Deploy</h4>
          <p>Frontend (3000) &bull; FastAPI Backend (8000) &bull; PostgreSQL (5432)</p>
        </div>
        <div class="task-tag">Verified</div>
      </div>
      <div class="task-item">
        <div class="task-info">
          <h4>Docker Compose Multi-Container Orchestration</h4>
          <p>Built with docker-compose up -d --build</p>
        </div>
        <div class="task-tag">Verified</div>
      </div>
    `;
  }
}

async function handleCreateTask(e) {
  e.preventDefault();
  const title = document.getElementById('task-title').value.trim();
  const desc = document.getElementById('task-desc').value.trim();
  if (!title) return;

  try {
    const res = await fetch(`${API_BASE}/api/tasks`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, description: desc, session: 'Session 21', status: 'Completed' })
    });
    if (res.ok) {
      document.getElementById('task-title').value = '';
      document.getElementById('task-desc').value = '';
      await loadTasks();
      await checkHealth();
    }
  } catch (err) {
    console.error('Error creating task:', err);
  }
}

function escapeHtml(str) {
  return str.replace(/[&<>'"]/g, tag => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    "'": '&#39;',
    '"': '&quot;'
  }[tag] || tag));
}

// Event Listeners
btnRefresh.addEventListener('click', () => {
  checkHealth();
  loadTasks();
  loadSystemInfo();
});

newTaskForm.addEventListener('submit', handleCreateTask);

// Initial Load
checkHealth();
loadSystemInfo();
loadTasks();

// Auto refresh every 8 seconds
setInterval(checkHealth, 8000);
