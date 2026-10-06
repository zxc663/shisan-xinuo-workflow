<template>
  <div class="waiting">
    <h4 style="margin: 6px 0">候补队列</h4>
    <div class="wrow" v-for="w in queue" :key="w.pos" style="font-size: 16px">
      第 {{ w.pos }} 位 ｜ {{ w.slot_label }}
    </div>
    <button class="join" @click="join">加入候补</button>
  </div>
</template>

<script>
export default {
  name: 'WaitingList',
  props: { slotId: String },
  data() {
    return { queue: [] }
  },
  methods: {
    join() {
      this.queue.push({ pos: this.queue.length + 1, slot_label: this.slotId })
      console.log('joined waiting', this.slotId)
    }
  }
}
</script>

<style scoped>
.join { margin-top: 8px; font-size: 16px; }
</style>
