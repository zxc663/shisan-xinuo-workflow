<template>
  <div class="stats" style="padding: 16px;">
    <h3 style="color: #333;">月度统计</h3>
    <canvas ref="cv" width="360" height="240"></canvas>
  </div>
</template>

<script>
export default {
  name: "StatsChart",
  props: { month: String },
  async mounted() {
    const res = await fetch(`/api/ledger/stats?month=${this.month || ""}`)
    const data = await res.json()
    const ctx = this.$refs.cv.getContext("2d")
    console.log("chart data", data, ctx)
  }
}
</script>
