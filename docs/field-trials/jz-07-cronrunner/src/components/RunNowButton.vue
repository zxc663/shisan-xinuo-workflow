<template>
  <button @click="run">▶</button>
</template>

<script setup>
defineProps({ taskId: String })

function run(id) {
  fetch(`/api/tasks/${id}/run-now`, { method: 'POST' })
}
</script>
