<template>
  <form class="create-key-form" @submit.prevent="submit">
    <h2>生成密钥</h2>
    <label for="key-name">密钥名称</label>
    <input id="key-name" v-model="name" type="text" placeholder="如：ci-deploy" />
    <p v-if="nameError" class="error">{{ nameError }}</p>
    <button type="submit">生成</button>
    <button type="button" @click="cancel">取消</button>
  </form>
</template>

<script setup>
import { ref, computed } from "vue";

const name = ref("");
const emit = defineEmits(["create", "cancel"]);

const nameError = computed(() =>
  name.value.trim().length === 0 ? "名称不能为空" : ""
);

function submit() {
  if (nameError.value) return;
  emit("create", name.value.trim());
}

function cancel() {
  emit("cancel");
}
</script>
