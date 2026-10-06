<template>
  <form class="add-task-form" @submit.prevent="submit">
    <label for="task-name">任务名称</label>
    <input id="task-name" v-model="name" type="text" placeholder="如：更新部署脚本" />
    <button type="submit">新建任务</button>
  </form>
</template>

<script setup>
import { ref } from "vue";

const name = ref("");
const emit = defineEmits(["create"]);

function submit() {
  const v = name.value.trim();
  if (!v) return;
  emit("create", v);
  name.value = "";
}
</script>
