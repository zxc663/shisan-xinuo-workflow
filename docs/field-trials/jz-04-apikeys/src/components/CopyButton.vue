<template>
  <button class="copy-btn" @click="copy">
    {{ copied ? "已复制" : "复制" }}
  </button>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({ text: { type: String, required: true } });
const copied = ref(false);

async function copy() {
  await navigator.clipboard.writeText(props.text);
  copied.value = true;
}
</script>
