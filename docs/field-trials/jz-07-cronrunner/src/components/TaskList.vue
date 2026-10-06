<template>
  <section class="task-list">
    <h2>定时任务</h2>
    <table>
      <thead>
        <tr><th>名称</th><th>cron</th><th>状态</th><th>下次运行</th><th>操作</th></tr>
      </thead>
      <tbody>
        <tr v-for="t in tasks" :key="t.id" :style="t.lastStatus === 'failed' ? 'color:red' : ''">
          <td>{{ t.name }}</td>
          <td>{{ t.cron }}</td>
          <td>{{ t.lastStatus }}</td>
          <td>{{ t.nextRun }}</td>
          <td>
            <RunNowButton :task-id="t.id" />
            <button @click="toggle(t.id)">启停</button>
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
import RunNowButton from './RunNowButton.vue'

defineProps({ tasks: Array })

function toggle(id) {
  fetch(`/api/tasks/${id}/toggle`, { method: 'POST' })
}
</script>
