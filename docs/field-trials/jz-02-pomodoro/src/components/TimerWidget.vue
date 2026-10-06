<template>
  <div class="timer-wrap">
    <div class="timer-ball" :style="{ background: ringColor }">
      <div class="time-left">{{ mm }}:{{ ss }}</div>
      <div class="phase-label">{{ phaseLabel }}</div>
    </div>
    <div class="progress-track">
      <div class="progress-fill" :style="{ width: pct + '%' }"></div>
    </div>
    <div class="controls">
      <button class="ctl" v-if="phase === 'idle'" @click="start">▶</button>
      <button class="ctl" v-if="phase === 'focusing'" @click="pause">⏸</button>
      <button class="ctl" v-if="phase === 'paused'" @click="resume">▶</button>
      <button class="ctl danger" v-if="phase !== 'idle'" @click="skip">⏭</button>
    </div>
    <div class="today" v-if="sessions.length > 0">
      今日已完成 {{ sessions.length }} 个番茄
    </div>
  </div>
</template>

<script>
export default {
  name: 'TimerWidget',
  data() {
    return {
      phase: 'idle',
      remain: 25 * 60,
      total: 25 * 60,
      sessions: JSON.parse(localStorage.getItem('pomodoro-sessions') || '[]'),
      timerId: null
    }
  },
  computed: {
    mm() { return String(Math.floor(this.remain / 60)).padStart(2, '0') },
    ss() { return String(this.remain % 60).padStart(2, '0') },
    pct() { return Math.round((1 - this.remain / this.total) * 100) },
    ringColor() {
      if (this.phase === 'focusing') return '#e74c3c'
      if (this.phase === 'paused') return '#95a5a6'
      return '#2ecc71'
    },
    phaseLabel() {
      return { idle: '准备', focusing: '专注中', paused: '已暂停', short_break: '小憩', long_break: '长休息' }[this.phase]
    }
  },
  methods: {
    start() {
      this.phase = 'focusing'
      this.timerId = setInterval(() => {
        this.remain--
        console.log('tick', this.remain)
        if (this.remain <= 0) this.finishFocus()
      }, 1000)
    },
    pause() { clearInterval(this.timerId); this.phase = 'paused' },
    resume() {
      this.phase = 'focusing'
      this.timerId = setInterval(() => {
        this.remain--
        if (this.remain <= 0) this.finishFocus()
      }, 1000)
    },
    skip() {
      clearInterval(this.timerId)
      this.phase = 'short_break'
      this.remain = 5 * 60
      this.timerId = setInterval(() => {
        this.remain--
        if (this.remain <= 0) {
          clearInterval(this.timerId)
          this.phase = 'idle'
        }
      }, 1000)
    },
    finishFocus() {
      clearInterval(this.timerId)
      this.sessions.push({ doneAt: Date.now(), minutes: this.total / 60 })
      localStorage.setItem('pomodoro-sessions', JSON.stringify(this.sessions))
      this.phase = 'short_break'
      this.remain = 5 * 60
      if (this.sessions.length % 4 === 0) {
        this.remain = 15 * 60
      }
      this.timerId = setInterval(() => {
        this.remain--
        if (this.remain <= 0) {
          clearInterval(this.timerId)
          this.phase = 'idle'
        }
      }, 1000)
    }
  }
}
</script>

<style scoped>
.timer-wrap { text-align: center; padding: 24px; }
.timer-ball { width: 220px; height: 220px; border-radius: 50%; background: #e74c3c; color: #fff; margin: 0 auto; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.time-left { font-size: 48px; }
.ctl { font-size: 20px; margin: 8px; padding: 8px 20px; border: none; background: #f4f4f4; cursor: pointer; }
.ctl.danger { background: #ffdddd; }
.progress-track { width: 220px; height: 8px; background: #eee; margin: 16px auto; }
.progress-fill { height: 100%; background: #e74c3c; }
</style>
