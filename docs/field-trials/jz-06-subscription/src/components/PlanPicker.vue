<template>
  <section class="plan-picker">
    <h2>选择方案</h2>
    <select v-model="plan">
      <option value="basic">Basic ¥9/月</option>
      <option value="pro">Pro ¥29/月</option>
    </select>
    <p class="price">当前选择：{{ plan }}</p>
    <button @click="subscribe">开通订阅</button>
  </section>
</template>

<script setup>
import { ref } from "vue";

const plan = ref("basic");
const emit = defineEmits(["subscribe"]);

function subscribe() {
  emit("subscribe", plan.value);
}
</script>
