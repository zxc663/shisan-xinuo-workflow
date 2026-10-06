<template>
  <div class="mine">
    <h3 style="border-bottom: 1px solid #eee">我的预约</h3>
    <div v-for="a in list" :key="a.id" class="appt" style="padding: 10px 0">
      <span style="font-size: 18px">{{ a.dept }} {{ a.doctor }} ｜ {{ a.time }}</span>
      <button class="del" @click="cancel(a)">✕</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyAppointmentList',
  data() {
    return { list: [] }
  },
  async created() {
    const res = await fetch('/appointments/mine?patient=' + localStorage.getItem('patient'))
    this.list = await res.json()
    console.log('mine', this.list)
  },
  methods: {
    async cancel(a) {
      if (!confirm('确定取消该预约？')) return
      await fetch('/appointments/' + a.id, { method: 'DELETE' })
      this.list = this.list.filter(x => x.id !== a.id)
    }
  }
}
</script>

<style scoped>
.del { background: none; border: none; font-size: 20px; color: #e74c3c; cursor: pointer; }
</style>
