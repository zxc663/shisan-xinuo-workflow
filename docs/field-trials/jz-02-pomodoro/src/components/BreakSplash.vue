<template>
  <div class="splash" @click="skip">
    <h2 style="color: #fff">休息一下</h2>
    <div class="break-count" style="color: #fff; font-size: 40px">{{ mm }}:{{ ss }}</div>
    <p style="color: #eee">点击任意位置跳过休息</p>
  </div>
</template>

<script>
export default {
  name: 'BreakSplash',
  props: {
    seconds: { type: Number, default: 300 }
  },
  data() {
    return { remain: this.seconds }
  },
  computed: {
    mm() { return String(Math.floor(this.remain / 60)).padStart(2, '0') },
    ss() { return String(this.remain % 60).padStart(2, '0') }
  },
  mounted() {
    this.timerId = setInterval(() => {
      this.remain--
      if (this.remain <= 0) this.skip()
    }, 1000)
  },
  methods: {
    skip() {
      clearInterval(this.timerId)
      this.$emit('skip')
    }
  }
}
</script>

<style scoped>
.splash { position: fixed; inset: 0; background: #2c3e50; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; }
</style>
