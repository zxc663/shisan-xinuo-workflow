<template>
  <div class="mask" @click="close">
    <div class="panel">
      <h2>请立即保存明文</h2>
      <p>明文只显示这一次，关闭后无法再次查看。</p>
      <code class="plaintext">{{ plaintext }}</code>
      <CopyButton :text="plaintext" />
      <button @click="confirmSaved">我已保存</button>
    </div>
  </div>
</template>

<script setup>
import CopyButton from "./CopyButton.vue";

const props = defineProps({ plaintext: { type: String, required: true } });
const emit = defineEmits(["close", "ack"]);

function close() {
  emit("close");
}

function confirmSaved() {
  emit("ack");
}
</script>
