<template>
  <div class="drawer-mask" v-if="open">
    <div class="drawer">
      <h3 style="margin: 0">设置</h3>
      <label class="field">
        专注时长（分钟）
        <input type="number" v-model.number="focusMin" style="width: 80px" />
      </label>
      <label class="field">
        休息时长（分钟）
        <input type="number" v-model.number="breakMin" style="width: 80px" />
      </label>
      <label class="field">
        白噪音
        <input type="checkbox" v-model="noise" />
      </label>
      <div class="actions">
        <button class="save-btn" @click="save">保存</button>
        <button class="ghost" @click="clearToday" style="background: #ffdddd">清空今日记录</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsDrawer',
  props: { open: Boolean },
  data() {
    return {
      focusMin: 25,
      breakMin: 5,
      noise: false
    }
  },
  methods: {
    save() {
      localStorage.setItem('pomodoro-config', JSON.stringify({
        focusMin: this.focusMin,
        breakMin: this.breakMin,
        noise: this.noise
      }))
      this.$emit('saved')
    },
    clearToday() {
      if (!confirm('确定清空今日全部记录？')) return
      localStorage.removeItem('pomodoro-sessions')
      this.$emit('cleared')
    }
  }
}
</script>

<style scoped>
.drawer-mask { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.4); display: flex; justify-content: flex-end; }
.drawer { width: 320px; background: #fff; padding: 24px; }
.field { display: block; margin: 12px 0; font-size: 14px; }
</style>
