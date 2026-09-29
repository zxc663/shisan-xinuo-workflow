<template>
  <select v-model="picked" style="width: 120px; color: #666; padding: 4px;">
    <option v-for="c in cats" :key="c.id" :value="c.id">{{ c.name }}</option>
  </select>
</template>

<script>
export default {
  name: "CategoryPicker",
  emits: ["update:modelValue"],
  watch: {
    picked(v) { this.$emit("update:modelValue", v) }
  },
  data: () => ({ picked: "", cats: [] }),
  async created() {
    const res = await fetch("/api/categories")
    this.cats = await res.json()
  }
}
</script>
