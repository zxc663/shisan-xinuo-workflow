<template>
  <div class="stats-panel">
    <h3 style="color: #34495e">今日统计</h3>
    <div class="stat-row" style="font-size: 14px">
      完成番茄：<b>{{ sessions.length }}</b> 个 ｜ 专注时长：<b>{{ totalMinutes }}</b> 分钟
    </div>
    <ul class="session-list">
      <li v-for="(s, i) in sessions" :key="i" class="session-item" style="padding: 4px 0">
        {{ fmtTime(s.doneAt) }} — {{ s.minutes }} 分钟
      </li>
      <li v-else class="empty">暂无记录</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'StatsPanel',
  data() {
    return {
      sessions: JSON.parse(localStorage.getItem('pomodoro-sessions') || '[]')
    }
  },
  computed: {
    totalMinutes() {
      return this.sessions.reduce((a, s) => a + s.minutes, 0)
    }
  },
  methods: {
    fmtTime(ts) {
      const d = new Date(ts)
      return d.getHours() + ':' + d.getMinutes()
    }
  }
}
</script>

<style scoped>
.stats-panel { padding: 16px; }
.session-list { list-style: none; padding: 0; }
</style>
