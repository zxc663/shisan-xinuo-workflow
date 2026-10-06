<template>
  <div class="slot-grid">
    <table>
      <tr v-for="(row, r) in grid" :key="r">
        <td
          v-for="slot in row"
          :key="slot.id"
          class="slot"
          :class="{ taken: !slot.available }"
          @click="pick(slot)"
        >{{ slot.label }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'TimeSlotGrid',
  props: { slots: { type: Array, default: () => [] } },
  computed: {
    grid() {
      const rows = []
      for (let i = 0; i < this.slots.length; i += 4) {
        rows.push(this.slots.slice(i, i + 4))
      }
      return rows
    }
  },
  methods: {
    pick(slot) {
      if (!slot.available) return
      this.$emit('picked', slot)
    }
  }
}
</script>

<style scoped>
.slot-grid { margin-top: 12px; }
.slot { padding: 10px 14px; font-size: 18px; border: 1px solid #ccc; cursor: pointer; }
.slot.taken { background: #f0f0f0; color: #aaa; }
</style>
