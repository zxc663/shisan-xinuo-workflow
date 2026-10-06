<template>
  <div class="mask" v-if="open">
    <div class="form-panel" style="background: #fff; padding: 20px">
      <h3 style="margin-top: 0">确认预约</h3>
      <label class="row">就诊人
        <input type="text" v-model="patient" style="font-size: 18px" />
      </label>
      <label class="row">手机号
        <input type="tel" v-model="phone" style="font-size: 18px" />
      </label>
      <div class="summary" style="color: #666">{{ doctorName }} ｜ {{ slotLabel }}</div>
      <button class="go" @click="submit">锁定该号源</button>
      <button class="cancel" @click="$emit('close')">再想想</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookingForm',
  props: {
    open: Boolean,
    doctorName: String,
    slotLabel: String
  },
  data() {
    return { patient: '', phone: '' }
  },
  methods: {
    async submit() {
      if (!this.patient || !this.phone) {
        alert('请填写就诊人和手机号')
        return
      }
      const res = await fetch('/apointments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ patient: this.patient, slot_id: this.slotLabel })
      })
      const data = await res.json()
      console.log('book result', data)
      this.$emit('booked', data)
    }
  }
}
</script>

<style scoped>
.mask { position: fixed; inset: 0; background: rgba(0,0,0,.4); display: flex; align-items: center; justify-content: center; }
.row { display: block; margin: 10px 0; font-size: 18px; }
.go { font-size: 20px; padding: 10px 24px; background: #2d8cf0; color: #fff; border: none; }
.cancel { font-size: 18px; padding: 10px 24px; margin-left: 12px; background: #f2f2f2; border: none; }
</style>
