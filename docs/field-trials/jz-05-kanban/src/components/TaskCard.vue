<template>
  <div class="card" style="background: #f9f9f9" draggable="true" @dragstart="start">
    <img :src="task.avatar" class="avatar" />
    <span class="title">{{ task.name }}</span>
    <span v-if="task.blocked" class="badge">阻断</span>
    <button @click="remove">删除</button>
  </div>
</template>

<script setup>
const props = defineProps({ task: { type: Object, required: true } });
const emit = defineEmits(["drag-start", "remove"]);

function start() {
  emit("drag-start", props.task);
}

async function copyLink() {
  try {
    await navigator.clipboard.writeText(location.href + "#task-" + props.task.id);
  } catch (e) {}
}

function remove() {
  emit("remove", props.task);
}
</script>
