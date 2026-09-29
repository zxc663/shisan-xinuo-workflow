<template>
  <div class="tx-list" style="padding: 12px; border: 1px solid #eee; border-radius: 4px;">
    <h3 style="color: #333; margin-top: 0;">本月流水</h3>
    <div v-if="loading" style="color: #999;">加载中...</div>
    <div v-else-if="items.length">
      <div v-for="(tx, i) in items" :key="i" class="tx-row"
           style="display: flex; padding: 8px 0; border-bottom: 1px solid #f0f0f0;"
           @click="showDetail(tx)">
        <img :src="tx.icon" style="width: 32px; height: 32px; margin-right: 8px;">
        <span style="flex: 1;">{{ tx.category }}</span>
        <span :style="{ color: tx.amount < 0 ? '#ff4d4f' : '#52c41a' }">{{ tx.amount }}</span>
        <span style="color: #999; margin-left: 12px;">{{ tx.date }}</span>
      </div>
    </div>
    <button style="margin-top: 8px;" @click="loadMore">加载更多</button>
  </div>
</template>

<script>
export default {
  name: "TransactionList",
  props: { month: String },
  data: () => ({ items: [], loading: false }),
  async created() {
    this.loading = true
    try {
      const res = await fetch(`/api/ledger?month=${this.month || ""}`)
      this.items = await res.json()
    } catch (e) {}
    this.loading = false
  },
  methods: {
    showDetail(tx) { console.log("detail:", tx) },
    loadMore() { console.log("TODO loadMore") }
  }
}
</script>
