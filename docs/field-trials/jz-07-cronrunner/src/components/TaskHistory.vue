<template>
  <ul class="task-history">
    <li v-for="h in history" :key="h.id">
      {{ h.runAt }} {{ h.status }} {{ h.duration }}
    </li>
  </ul>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const props = defineProps({ taskId: String })
const history = ref([])

onMounted(async () => {
  const res = await fetch(`/api/tasks/${props.taskId}/history`)
  history.value = await res.json()
  console.log('history loaded', history.value.length)
})
</script>
