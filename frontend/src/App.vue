<script setup>
import { ref } from 'vue';
import './assets/App.css';
import Dashboard from './components/Dashboard.vue';

const username = ref('');
const password = ref('');
const message = ref('');
const token = ref('');
const loading = ref(false);
const currentUser = ref(null);

const API_BASE = 'http://localhost:8000';

async function handleLogin() {
  loading.value = true;
  message.value = '';
  
  try {
    const response = await fetch(`${API_BASE}/api/v1/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    });
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Login failed');
    }
    
    const data = await response.json();
    token.value = data.access_token;
    message.value = 'Login successful!';
    
    // Fetch user info
    await fetchUserInfo();
  } catch (error) {
    message.value = `Error: ${error.message}`;
    console.error('Login error:', error);
  } finally {
    loading.value = false;
  }
}

async function fetchUserInfo() {
  try {
    const response = await fetch(`${API_BASE}/api/v1/auth/me?token=${token.value}`);
    
    if (!response.ok) {
      throw new Error('Failed to fetch user info');
    }
    
    const data = await response.json();
    currentUser.value = data;
  } catch (error) {
    message.value = `Error: ${error.message}`;
    console.error('Fetch user error:', error);
  }
}

function handleLogout() {
  token.value = '';
  currentUser.value = null;
  username.value = '';
  password.value = '';
  message.value = 'Logged out successfully';
}
</script>

<template>
  <div class="container">
    <div class="login-card">
      <h1>Portal22</h1>
      <p class="subtitle">SSH Connection Manager</p>
      
      <div v-if="!token" class="login-form">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="username"
            type="text"
            placeholder="Enter username"
            @keyup.enter="handleLogin"
          />
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <input
            id="password"
            v-model="password"
            type="password"
            placeholder="Enter password"
            @keyup.enter="handleLogin"
          />
        </div>
        
        <button 
          @click="handleLogin" 
          :disabled="loading || !username || !password"
          class="btn-primary"
        >
          {{ loading ? 'Logging in...' : 'Login' }}
        </button>
        
        <div v-if="message" :class="['message', token ? 'success' : 'error']">
          {{ message }}
        </div>
        
        <div class="hint">
          <p>Default credentials:</p>
          <p><strong>Username:</strong> admin</p>
          <p><strong>Password:</strong> Portal22Admin!</p>
        </div>
      </div>
      
      <Dashboard v-else :username="currentUser?.username" @logout="handleLogout" />
    </div>
  </div>
</template>
