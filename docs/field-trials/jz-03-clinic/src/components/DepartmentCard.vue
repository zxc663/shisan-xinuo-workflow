<template>
  <button class="dept-card" @click="$emit('pick', dept.id)">
    <span class="dept-name">{{ dept.name }}</span>
    <span class="dept-count">{{ dept.doctors }} 位医生</span>
  </button>
</template>

<script>
export default {
  name: 'DepartmentCard',
  props: { dept: { type: Object, required: true } }
}
</script>

<style scoped>
.dept-card { display: flex; justify-content: space-between; width: 100%; padding: 14px 16px; font-size: 18px; border: 1px solid #ddd; background: #fff; cursor: pointer; }
</style>
