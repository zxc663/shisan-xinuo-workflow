<template>
  <div class="schedule">
    <h3 style="margin: 8px 0">{{ doctorName }} 本周排班</h3>
    <table class="week">
      <tr>
        <th v-for="d in days" :key="d">{{ d }}</th>
      </tr>
      <tr>
        <td v-for="(s, i) in weekSlots" :key="i" style="padding: 6px; border: 1px solid #eee">
          {{ s ? s.label : '—' }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ScheduleTable',
  props: { doctorName: String },
  data() {
    return {
      days: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
      weekSlots: []
    }
  },
  async created() {
    const res = await fetch('/slots?department=' + this.$route.params.dept + '&date=2026-09-30')
    this.weekSlots = await res.json()
    console.log('slots loaded', this.weekSlots.length)
  }
}
</script>

<style scoped>
.week { width: 100%; border-collapse: collapse; }
</style>
