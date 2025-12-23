<template>
  <div class="dashboard">
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo">
          <img src="../assets/ssh-logo.svg" alt="SSH Logo" class="logo-icon" />
          <span class="logo-text">Portal22</span>
        </div>
        <button class="collapse-btn">⋮⋮</button>
      </div>

      <div class="search-box">
        <input type="text" placeholder="Search for..." />
      </div>

      <nav class="nav-menu">
        <div class="nav-section">
          <button class="nav-item active" @click="activeSection = 'dashboard'">
            <span class="icon">📊</span>
            <span class="label">Dashboard</span>
            <span class="arrow">›</span>
          </button>
          <div v-if="activeSection === 'dashboard'" class="submenu">
            <a href="#" class="submenu-item">All pages</a>
            <a href="#" class="submenu-item">Reports</a>
            <a href="#" class="submenu-item">Products</a>
            <a href="#" class="submenu-item">Task</a>
          </div>
        </div>

        <button class="nav-item" @click="activeSection = 'features'">
          <span class="icon">⭐</span>
          <span class="label">Features</span>
          <span class="arrow">›</span>
        </button>

        <button class="nav-item" @click="activeSection = 'users'">
          <span class="icon">👥</span>
          <span class="label">Users</span>
          <span class="arrow">›</span>
        </button>

        <button class="nav-item" @click="activeSection = 'pricing'">
          <span class="icon">💰</span>
          <span class="label">Pricing</span>
          <span class="arrow">›</span>
        </button>

        <button class="nav-item" @click="activeSection = 'integrations'">
          <span class="icon">🔌</span>
          <span class="label">Integrations</span>
          <span class="arrow">›</span>
        </button>
      </nav>

      <div class="sidebar-footer">
        <button class="nav-item" @click="activeSection = 'settings'">
          <span class="icon">⚙️</span>
          <span class="label">Settings</span>
          <span class="arrow">›</span>
        </button>
      </div>
    </aside>

    <main class="main-content">
      <header class="top-bar">
        <div class="breadcrumb">
          <span>Dashboard</span>
        </div>
        <div class="user-menu">
          <span class="username">{{ username }}</span>
          <button @click="$emit('logout')" class="logout-btn">Logout</button>
        </div>
      </header>

      <div class="content-area">
        <h1>Welcome to Portal22</h1>
        <p class="subtitle">SSH Connection Manager Dashboard</p>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">🖥️</div>
            <div class="stat-info">
              <h3>0</h3>
              <p>SSH Connections</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">🔐</div>
            <div class="stat-info">
              <h3>0</h3>
              <p>Saved Credentials</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">📁</div>
            <div class="stat-info">
              <h3>0</h3>
              <p>Active Sessions</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">⚡</div>
            <div class="stat-info">
              <h3>Ready</h3>
              <p>System Status</p>
            </div>
          </div>
        </div>

        <div class="quick-actions">
          <h2>Quick Actions</h2>
          <div class="action-buttons">
            <button class="action-btn">
              <span class="btn-icon">➕</span>
              <span>New Connection</span>
            </button>
            <button class="action-btn">
              <span class="btn-icon">📋</span>
              <span>View Connections</span>
            </button>
            <button class="action-btn">
              <span class="btn-icon">🔑</span>
              <span>Manage Keys</span>
            </button>
            <button class="action-btn">
              <span class="btn-icon">⚙️</span>
              <span>Settings</span>
            </button>
          </div>
        </div>

        <div class="recent-activity">
          <h2>Recent Activity</h2>
          <div class="activity-list">
            <p class="empty-state">No recent activity</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import '../assets/Dashboard.css';

defineProps({
  username: {
    type: String,
    required: true
  }
});

defineEmits(['logout']);

const activeSection = ref('dashboard');
</script>
