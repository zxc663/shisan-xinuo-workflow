<template>
  <form class="task-form" @submit.prevent="save">
    <label>任务名称</label>
    <input v-model="name" />
    <CronField v-model="cron" />
    <button type="submit">保存</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import CronField from './CronField.vue'

const name = ref('')
const cron = ref('')

function save() {
  fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: name.value, cron: cron.value })
  })
}
</script>
