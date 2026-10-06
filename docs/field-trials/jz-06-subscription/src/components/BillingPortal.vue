<template>
  <section class="billing-portal">
    <h2>订阅状态</h2>
    <p>当前状态：{{ statusText }}</p>
    <button @click="cancel">取消订阅（期末生效）</button>
  </section>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({ status: { type: String, default: "trialing" } });
const emit = defineEmits(["cancel"]);

const statusText = computed(() =>
  ({ trialing: "试用中", active: "已订阅", canceled: "已取消", expired: "已过期" }[props.status] || props.status)
);

function cancel() {
  emit("cancel");
}
</script>
