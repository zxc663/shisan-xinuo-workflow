<template>
  <section class="key-usage">
    <h2>用量（近 24 小时）</h2>
    <ul>
      <li>调用次数：{{ stats.calls_24h }}</li>
      <li>错误次数：{{ stats.errors_24h }}</li>
    </ul>
    <button @click="back">返回列表</button>
  </section>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  stats: { type: Object, default: () => ({ calls_24h: 0, errors_24h: 0 }) },
});
const emit = defineEmits(["back"]);

function back() {
  emit("back");
}
</script>
